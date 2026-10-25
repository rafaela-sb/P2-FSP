"""Tratamento: transforma os dados brutos em bases analíticas.

Uso: python codigo/04_tratamento.py   (executar a partir da raiz do repositório)

Entradas : dados/brutos/siconfi, dados/brutos/ibge, dados/brutos/ucrania, dados/original
Saídas   : dados/tratados/
  - base_original_consolidada.csv   planilhas do trabalho anterior (P1) empilhadas, com checagem do deflator
  - siconfi_nominal_longo.csv        variáveis fiscais em R$ correntes, formato longo
  - base_municipios.csv              base analítica (nominal, real, per capita, indicadores)
  - base_ucrania.csv                 base analítica da Ucrânia (FMI-FD + WDI)
  - base_ucrania_local_2021_2025.csv orçamentos locais da Ucrânia (Ministério das Finanças), série separada
  - checagens.csv                    testes de consistência (somatórios, cobertura)

Regras gerais (ver documentacao/dicionario_variaveis.md):
  * Valores fiscais = "Receitas Brutas Realizadas" (receita) e "Despesas Empenhadas" (despesa) da DCA.
  * Ausência de dado = NA (nunca zero): conta não declarada na DCA permanece vazia.
  * Deflator: IPCA médio anual (IBGE, tabela 1737), ano-base 2025.
"""
import glob
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from entes import ENTES as _ENTES, FOCO

RAIZ = Path(".")
BRUTO = RAIZ / "dados/brutos"
TRAT = RAIZ / "dados/tratados"
TRAT.mkdir(parents=True, exist_ok=True)
ANOS = list(range(2016, 2026))
ANO_BASE = 2025
ENTES = {slug: nome for slug, nome in _ENTES.values()}

# ---------------------------------------------------------------------------
# 1. Base original (trabalho anterior)
# ---------------------------------------------------------------------------
def base_original():
    linhas = []
    for f in sorted(glob.glob(str(RAIZ / "dados/original/prova finanças publicas/*/*.xlsx"))):
        ano = int(re.search(r"(\d{4})\.xlsx$", f).group(1))
        grupo = "corrente" if "correntes" in f else "capital"
        x = pd.read_excel(f)
        x = x.iloc[:, :3]
        x.columns = ["descricao", "arrecadado_nominal", "coluna_ipca_original"]
        for _, r in x.iterrows():
            linhas.append(dict(municipio="Teresina/PI", ano=ano, grupo=grupo, descricao=r.descricao,
                               arrecadado_nominal=r.arrecadado_nominal,
                               coluna_ipca_original=r.coluna_ipca_original,
                               arquivo_origem=str(Path(f).relative_to(RAIZ))))
    d = pd.DataFrame(linhas)
    d["fator_implicito"] = d.coluna_ipca_original / d.arrecadado_nominal
    med = d.groupby("ano").fator_implicito.transform("median")
    d["fator_mediano_ano"] = med
    d["inconsistencia_deflator"] = (d.fator_implicito / med - 1).abs() > 0.02
    d["ano_incompleto"] = d.ano == 2026
    d.to_csv(TRAT / "base_original_consolidada.csv", index=False)
    return d

# ---------------------------------------------------------------------------
# 2. Siconfi – leitura e mapeamento de contas
# ---------------------------------------------------------------------------
def sig(cod):
    """Segmentos significativos do código de conta (sem zeros finais) – usado para hierarquia."""
    s = re.sub(r"^[A-Z]+", "", cod).split(".")
    while s and set(s[-1]) <= {"0"}:
        s.pop()
    return tuple(int(p) for p in s if p.isdigit())

def eh_descendente(a, b):
    return len(a) > len(b) and a[: len(b)] == b

def soma_sem_dupla_contagem(df):
    """Soma linhas que casaram com um padrão, descartando as que são filhas de outra linha casada."""
    if df.empty:
        return None
    codigos = [sig(c) for c in df.cod_conta]
    manter = [not any(eh_descendente(c, o) for o in codigos if o != c) for c in codigos]
    return float(df[manter].valor.sum())

# Variáveis por código (nível agregado, idêntico nas três versões do ementário 2016–2025)
POR_CODIGO = {
    "rec_corrente": (1,),
    "rec_tributaria": (1, 1),       # Impostos, taxas e contribuições de melhoria
    "rec_contribuicoes": (1, 2),
    "transf_correntes": (1, 7),
    "rec_capital": (2,),
    "operacoes_credito": (2, 1),
    "transf_capital": (2, 4),
}
# Variáveis por nome da conta (o código mudou em 2018 e 2022). Restritas às receitas correntes (1.x).
POR_NOME = {
    "iptu": (r"Propriedade Predial", (1, 1)),
    "itbi": (r"Transmiss.o .?Inter Vivos", (1, 1)),
    "iss": (r"Impostos? sobre Servi[çc]os|ISSQN", (1, 1)),
    "irrf": (r"Impostos? sobre a Renda", (1, 1)),
    "taxas": (r"^Taxas$", (1, 1)),
    "fpm": (r"Fundo de Participa..o dos Munic", (1, 7)),
    "icms_cota": (r"Cota-Parte do ICMS", (1, 7)),
    "ipva_cota": (r"Cota-Parte do IPVA", (1, 7)),
    "sus": (r"Sistema .nico de Sa.de|\bSUS\b|Programas de Sa.de", (1, 7)),
    "fundeb": (r"Manuten..o e Desenvolvimento da Educa..o B.sica|FUNDEB", (1, 7)),
    "fnde": (r"Fundo Nacional do Desenvolvimento da Educa|Sal.rio.Educa|Alimenta..o Escolar|Transporte Escolar", (1, 7)),
}

def nome_limpo(conta):
    return re.sub(r"^[\d.]+\s*-\s*", "", conta).strip()

def ler(anexo, ente, ano):
    f = BRUTO / f"siconfi/dca_{anexo}_{ente}_{ano}.csv"
    if not f.exists():
        return None
    d = pd.read_csv(f, dtype={"cod_conta": str})
    d["valor"] = pd.to_numeric(d.valor, errors="coerce")
    return d

def receitas(ente, ano):
    d = ler("receitas", ente, ano)
    if d is None:
        return {}
    bruto = d[d.coluna.str.startswith("Receitas Brutas")].copy()
    ded = d[d.coluna.str.contains("FUNDEB", case=False)].copy()
    ro = bruto[bruto.cod_conta.str.startswith("RO")].copy()
    ro["s"] = ro.cod_conta.map(sig)
    ro["nome"] = ro.conta.map(nome_limpo)
    out = {}
    for var, cod in POR_CODIGO.items():
        linha = ro[ro.s.map(lambda s: s == cod)]
        out[var] = float(linha.valor.sum()) if len(linha) else None
    for var, (padrao, raiz) in POR_NOME.items():
        cand = ro[ro.nome.str.contains(padrao, case=False, regex=True)
                  & ro.s.map(lambda s: s[: len(raiz)] == raiz)
                  & ~ro.nome.str.contains("Dedu", case=False)]
        if var == "fundeb":  # exclui convênios/FNDE que mencionam "educação básica" de forma genérica
            cand = cand[~cand.nome.str.contains("Fundo Nacional", case=False)]
        out[var] = soma_sem_dupla_contagem(cand)
    tot = bruto[bruto.cod_conta == "ReceitasExcetoIntraOrcamentarias"]
    out["rec_total_declarada"] = float(tot.valor.sum()) if len(tot) else None  # só existe a partir de 2019
    if out["rec_corrente"] is not None and out["rec_capital"] is not None:
        out["rec_total"] = out["rec_corrente"] + out["rec_capital"]
    dt = ded[ded.cod_conta.str.startswith("RO")]
    dt = dt.assign(s=dt.cod_conta.map(sig))
    dfund = dt[dt.s.map(lambda s: s == (1,))] if len(dt) else dt
    out["deducao_fundeb"] = float(dfund.valor.sum()) if len(dfund) else None
    return out

def despesas(ente, ano):
    out = {}
    d = ler("despesas_natureza", ente, ano)
    if d is not None:
        emp = d[d.coluna == "Despesas Empenhadas"].copy()
        emp["s"] = emp.cod_conta.map(sig)
        e = emp[emp.cod_conta.str.startswith("DO")]
        # Os agregados "DO" do Anexo I-D incluem as despesas intraorçamentárias (modalidade 91, linhas "DI").
        # Elas são descontadas para manter o conceito "exceto intraorçamentárias" do Anexo I-E.
        intra = emp[emp.cod_conta.str.startswith("DI")]
        intra = intra[[len(s) == 3 and s[2] == 91 for s in intra.s]] if len(intra) else intra
        def intra_de(prefixo):
            if intra.empty:
                return 0.0
            x = intra[[s[: len(prefixo)] == prefixo for s in intra.s]]
            return float(x.valor.sum())
        for var, cod in {"desp_corrente": (3,), "desp_pessoal": (3, 1), "desp_juros": (3, 2),
                         "desp_outras_correntes": (3, 3), "desp_capital": (4,), "desp_investimentos": (4, 4),
                         "desp_amortizacao": (4, 6)}.items():
            linha = e[e.s.map(lambda s: s == cod)]
            out[var] = float(linha.valor.sum()) - intra_de(cod) if len(linha) else None
        out["desp_intra_natureza"] = float(intra.valor.sum()) if len(intra) else 0.0
        if out.get("desp_corrente") is not None and out.get("desp_capital") is not None:
            out["desp_total_natureza"] = out["desp_corrente"] + out["desp_capital"]
    d = ler("despesas_funcao", ente, ano)
    if d is not None:
        e = d[d.coluna == "Despesas Empenhadas"].reset_index(drop=True)
        # Só o bloco "exceto intraorçamentárias" (antes da linha que abre o bloco intra)
        corte = e.index[e.conta.str.contains(r"^Despesas \(?Intra", regex=True)]
        if len(corte):
            e = e.loc[: corte[0] - 1]
        tot = e[e.conta.str.contains(r"Exceto Intra", case=False)]
        out["desp_total_funcao"] = float(tot.valor.iloc[0]) if len(tot) else None
        out["desp_total"] = out["desp_total_funcao"]  # despesa total oficial = Anexo I-E, exceto intraorçamentárias
        fun = e[e.conta.str.match(r"^\d{2} - ")]
        for cod, var in {"04": "desp_administracao", "08": "desp_assistencia", "09": "desp_previdencia",
                         "10": "desp_saude", "12": "desp_educacao", "15": "desp_urbanismo"}.items():
            linha = fun[fun.conta.str.startswith(cod + " - ")]
            out[var] = float(linha.valor.sum()) if len(linha) else None
        out["soma_funcoes"] = float(fun.valor.sum()) if len(fun) else None
    return out

# ---------------------------------------------------------------------------
# 3. IBGE
# ---------------------------------------------------------------------------
def ibge():
    est = pd.read_csv(BRUTO / "ibge/populacao_estimada_t6579.csv")
    c22 = pd.read_csv(BRUTO / "ibge/populacao_censo2022_t4709.csv")
    c10 = pd.read_csv(BRUTO / "ibge/populacao_censo2010_t202.csv")
    pib = pd.read_csv(BRUTO / "ibge/pib_municipal_t5938.csv")
    ipca = pd.read_csv(BRUTO / "ibge/ipca_indice_mensal_t1737.csv")
    cod = {c: nome for c, (_, nome) in _ENTES.items()}

    pops = []
    for c, nome in cod.items():
        e = est[est["Município (Código)"] == c].set_index("Ano").Valor.astype(float)
        p22 = float(c22[c22["Município (Código)"] == c].Valor.iloc[0])
        p10 = float(c10[c10["Município (Código)"] == c].Valor.iloc[0])
        for ano in ANOS:
            if ano == 2022:
                oficial, fonte = p22, "Censo 2022 (t4709)"
            elif ano == 2023:
                oficial, fonte = (p22 + float(e.loc[2024])) / 2, "interpolação linear Censo 2022–estimativa 2024"
            else:
                oficial, fonte = float(e.loc[ano]), "estimativa IBGE (t6579)"
            # Série compatibilizada: 2016–2021 por interpolação geométrica entre os Censos 2010 e 2022
            if ano <= 2021:
                ajust = p10 * (p22 / p10) ** ((ano - 2010) / 12)
                fonte_aj = "interpolação geométrica Censos 2010–2022"
            else:
                ajust, fonte_aj = oficial, fonte
            pops.append(dict(municipio=nome, ano=ano, pop_oficial=round(oficial), fonte_pop_oficial=fonte,
                             pop=round(ajust), fonte_pop=fonte_aj))
    pops = pd.DataFrame(pops)

    p = pib[pib["Variável (Código)"].isin([37, 6575, 543])].copy()
    p["Valor"] = pd.to_numeric(p.Valor, errors="coerce") * 1000  # mil reais -> reais
    p["var"] = p["Variável (Código)"].map({37: "pib", 6575: "vab_servicos", 543: "impostos_produto"})
    p["municipio"] = p["Município (Código)"].map(cod)
    p = p.pivot_table(index=["municipio", "Ano"], columns="var", values="Valor").reset_index().rename(columns={"Ano": "ano"})

    ipca["ano"] = ipca["Mês (Código)"].astype(str).str[:4].astype(int)
    ipca_a = ipca.groupby("ano").Valor.mean().rename("ipca_indice_medio").reset_index()
    base = float(ipca_a.loc[ipca_a.ano == ANO_BASE, "ipca_indice_medio"].iloc[0])
    ipca_a["fator_real_2025"] = base / ipca_a.ipca_indice_medio
    return pops, p, ipca_a

# ---------------------------------------------------------------------------
# 4. Ucrânia
# ---------------------------------------------------------------------------
def ucrania():
    fd = pd.read_csv(BRUTO / "ucrania/imf_fd_ucrania.csv")
    fd = fd[fd.SECTOR == "S1313X"]  # governo local
    nomes = {"RD_PT": "fmi_descentralizacao_receita_pct", "G2MD_PT": "fmi_descentralizacao_despesa_pct",
             "TRANSFERDEP2_R_NT_OR_PT": "fmi_dependencia_transf_receita_propria_pct",
             "TRANSFERDEP1_R_NT_OS_PT": "fmi_dependencia_transf_despesa_propria_pct",
             "VFI_PT": "fmi_desequilibrio_vertical_pct", "TAXD_S13RSHR_PT": "fmi_descentralizacao_tributaria_pct",
             "G111_S13RSHR_PT": "fmi_local_share_impostos_renda_pct", "G113_S13RSHR_PT": "fmi_local_share_impostos_propriedade_pct",
             "GF09_S13ESHR_PT": "fmi_local_share_educacao_pct", "GF07_S13ESHR_PT": "fmi_local_share_saude_pct",
             "CS_S13ESHR_PT": "fmi_local_share_investimento_pct"}
    fd = fd[fd.INDICATOR.isin(nomes)].copy()
    fd["OBS_VALUE"] = fd.OBS_VALUE * 100  # a API devolve frações (0,15) apesar do sufixo _PT; convertido para %
    fd = fd.assign(var=fd.INDICATOR.map(nomes)).pivot_table(index="TIME_PERIOD", columns="var", values="OBS_VALUE")
    fd.index.name = "ano"
    wdi = pd.read_csv(BRUTO / "ucrania/wdi_ucrania.csv")
    nomes_w = {"NY.GDP.MKTP.CN": "pib_uah", "NY.GDP.MKTP.KD.ZG": "crescimento_pib_real_pct",
               "FP.CPI.TOTL": "cpi_2010_100", "FP.CPI.TOTL.ZG": "inflacao_pct", "SP.POP.TOTL": "populacao",
               "PA.NUS.FCRF": "cambio_uah_usd", "GC.REV.XGRT.GD.ZS": "gc_receita_exc_doacoes_pib",
               "GC.TAX.TOTL.GD.ZS": "gc_receita_tributaria_pib", "GC.XPN.TOTL.GD.ZS": "gc_despesa_pib",
               "GC.NLD.TOTL.GD.ZS": "gc_resultado_pib", "GC.DOD.TOTL.GD.ZS": "gc_divida_pib",
               "GC.REV.GOTR.ZS": "gc_doacoes_outras_pct_receita", "GC.XPN.TRFT.ZS": "gc_subsidios_transf_pct_despesa",
               "MS.MIL.XPND.GD.ZS": "despesa_militar_pib"}
    w = wdi.assign(var=wdi.indicador.map(nomes_w)).pivot_table(index="ano", columns="var", values="valor")
    base = pd.concat([fd, w], axis=1).sort_index()
    base = base.loc[2011:2025]
    cpi25 = base.loc[2025, "cpi_2010_100"]
    base["pib_uah_real_2025"] = base.pib_uah * cpi25 / base.cpi_2010_100
    base["pib_per_capita_uah_real_2025"] = base.pib_uah_real_2025 / base.populacao
    base["periodo"] = pd.cut(base.index, [2010, 2014, 2021, 2025],
                             labels=["pré-reforma (2011–2014)", "reforma de descentralização (2015–2021)", "guerra em larga escala (2022–2025)"])
    base.reset_index().to_csv(TRAT / "base_ucrania.csv", index=False)
    return base


def ucrania_local(base_macro):
    """Orçamentos locais da Ucrânia 2021–2025 (Ministério das Finanças). Série própria: NÃO é emendada à do FMI,
    que segue o conceito de governo local das estatísticas GFS (2011–2020)."""
    d = pd.read_csv(BRUTO / "ucrania/mof_orcamentos_locais_2021_2025.csv")
    w = d.pivot(index="ano", columns="variavel", values="valor_bi_uah")
    comps = ["pdfo", "imposto_unico", "pagamento_terra", "imposto_imoveis", "excise", "imposto_lucro"]
    w["outras_receitas"] = w.receita_propria_fg - w[comps].sum(axis=1)
    w["receita_total_com_transf"] = w.receita_propria_fg + w.transferencias
    w["transf_sobre_receita_propria_pct"] = 100 * w.transferencias / w.receita_propria_fg
    w["pdfo_sobre_receita_propria_pct"] = 100 * w.pdfo / w.receita_propria_fg
    w["tributos_patrimonio_sobre_receita_propria_pct"] = 100 * (w.pagamento_terra + w.imposto_imoveis) / w.receita_propria_fg
    m = base_macro[["pib_uah", "cpi_2010_100"]]
    w = w.join(m, how="left")
    w["receita_propria_pib_pct"] = 100 * w.receita_propria_fg * 1e9 / w.pib_uah
    w["transferencias_pib_pct"] = 100 * w.transferencias * 1e9 / w.pib_uah
    cpi25 = float(base_macro.loc[2025, "cpi_2010_100"])
    for v in ["receita_propria_fg", "transferencias", "pdfo"]:
        w[v + "_real_2025"] = w[v] * cpi25 / w.cpi_2010_100
    w["quebra_pdfo_militar"] = w.index >= 2024  # ПДФО de militares retirado dos orçamentos locais a partir de 2024
    w["transferencias_derivada"] = w.index == 2021
    w = w.drop(columns=["pib_uah", "cpi_2010_100"]).reset_index()
    w.to_csv(TRAT / "base_ucrania_local_2021_2025.csv", index=False)
    return w

# ---------------------------------------------------------------------------
# 5. Montagem da base municipal
# ---------------------------------------------------------------------------
NOMINAIS = ["rec_total", "rec_corrente", "rec_tributaria", "iptu", "iss", "itbi", "irrf", "taxas",
            "rec_contribuicoes", "transf_correntes", "fpm", "icms_cota", "ipva_cota", "sus", "fundeb", "fnde",
            "rec_capital", "operacoes_credito", "transf_capital", "deducao_fundeb",
            "desp_total", "desp_corrente", "desp_pessoal", "desp_juros", "desp_outras_correntes", "desp_capital",
            "desp_investimentos", "desp_amortizacao", "desp_administracao", "desp_assistencia", "desp_previdencia",
            "desp_saude", "desp_educacao", "desp_urbanismo"]

def main():
    orig = base_original()
    pops, pib, ipca = ibge()
    ucr = ucrania()
    ucr_local = ucrania_local(ucr)

    regs, longo, checks = [], [], []
    for ente, nome in ENTES.items():
        for ano in ANOS:
            r = {"municipio": nome, "ano": ano}
            r.update(receitas(ente, ano))
            r.update(despesas(ente, ano))
            regs.append(r)
            for k in NOMINAIS:
                longo.append(dict(municipio=nome, ano=ano, variavel=k, valor_nominal=r.get(k)))
            # checagens de consistência
            def chk(teste, a, b, tol=0.005):
                ok = None if a is None or b is None else abs(a - b) <= tol * max(abs(b), 1)
                checks.append(dict(municipio=nome, ano=ano, teste=teste, valor_a=a, valor_b=b, ok=ok))
            chk("rec_corrente + rec_capital = total declarado (2019+)", r.get("rec_total"), r.get("rec_total_declarada"))
            chk("soma das funções = total por função", r.get("soma_funcoes"), r.get("desp_total_funcao"))
            chk("despesa natureza (DO - intra) = despesa função", r.get("desp_total_natureza"), r.get("desp_total_funcao"))
            chk("iptu+iss+itbi+irrf+taxas <= rec_tributaria",
                sum((r.get(k) or 0) for k in ["iptu", "iss", "itbi", "irrf", "taxas"]), r.get("rec_tributaria"), tol=0.10)
    b = pd.DataFrame(regs)
    pd.DataFrame(longo).to_csv(TRAT / "siconfi_nominal_longo.csv", index=False)
    pd.DataFrame(checks).to_csv(TRAT / "checagens.csv", index=False)

    b = b.merge(pops, on=["municipio", "ano"], how="left").merge(pib, on=["municipio", "ano"], how="left")
    b = b.merge(ipca[["ano", "ipca_indice_medio", "fator_real_2025"]], on="ano", how="left")

    for k in NOMINAIS:
        b[k + "_real"] = b[k] * b.fator_real_2025
        b[k + "_real_pc"] = b[k + "_real"] / b["pop"]
    b["pib_real"] = b.pib * b.fator_real_2025
    b["pib_real_pc"] = b.pib_real / b["pop"]

    # Indicadores (razões são invariantes ao deflator)
    b["arrecadacao_propria"] = b.rec_tributaria  # impostos + taxas + contribuições de melhoria
    b["ind_autonomia_rc"] = b.rec_tributaria / b.rec_corrente
    b["ind_dependencia_transf"] = b.transf_correntes / b.rec_corrente
    b["ind_fpm_rc"] = b.fpm / b.rec_corrente
    b["ind_icms_rc"] = b.icms_cota / b.rec_corrente
    b["ind_transf_incondicionais_rc"] = (b.fpm + b.icms_cota + b.ipva_cota) / b.rec_corrente
    b["ind_transf_vinculadas_rc"] = (b.sus + b.fundeb + b.fnde) / b.rec_corrente
    b["ind_cobertura_despesa_propria"] = b.rec_tributaria / b.desp_total
    b["ind_pessoal_rc"] = b.desp_pessoal / b.rec_corrente
    b["ind_investimento_desp"] = b.desp_investimentos / b.desp_total
    b["ind_resultado_orcamentario_rt"] = (b.rec_total - b.desp_total) / b.rec_total
    b["ind_rec_tributaria_pib"] = b.rec_tributaria / b.pib
    b["ind_transf_correntes_pib"] = b.transf_correntes / b.pib
    b["ind_iss_vab_servicos"] = b.iss / b.vab_servicos

    # Sinalizações de qualidade (ver documentacao/registro_alteracoes.md)
    b["flag_sus_reclassificado"] = (b.municipio == "Natal/RN") & b.ano.isin([2023, 2024])
    b["flag_deducao_fundeb_inconsistente"] = (b.municipio == "Natal/RN") & b.ano.isin([2016, 2017, 2018])
    b["flag_natureza_agregada"] = (b.municipio == "Natal/RN") & b.ano.isin([2017, 2018])
    b["flag_pib_indisponivel"] = b.pib.isna()
    # Valores declarados atípicos nas demais capitais (mantidos como declarados; testados em robustez)
    b["flag_sus_reclassificado"] |= (b.municipio == "João Pessoa/PB") & (b.ano == 2018)
    b["flag_fundeb_atipico"] = ((b.municipio == "São Luís/MA") & b.ano.isin([2018, 2019, 2021])) | \
                               ((b.municipio == "João Pessoa/PB") & (b.ano == 2019))
    b["flag_iptu_atipico"] = (b.municipio == "Salvador/BA") & (b.ano == 2024)
    b["flag_qualquer"] = b[["flag_sus_reclassificado", "flag_deducao_fundeb_inconsistente", "flag_natureza_agregada",
                            "flag_fundeb_atipico", "flag_iptu_atipico"]].any(axis=1)
    b["foco"] = b.municipio.isin(FOCO)  # True = municípios atribuídos; False = capitais do NE (comparação)
    b = b.drop(columns=["soma_funcoes", "desp_total_funcao"])
    b.to_csv(TRAT / "base_municipios.csv", index=False)
    print(f"base_municipios.csv: {b.shape}; base_ucrania.csv: {ucr.shape}; base_original_consolidada.csv: {orig.shape}; base_ucrania_local_2021_2025.csv: {ucr_local.shape}")

if __name__ == "__main__":
    main()
