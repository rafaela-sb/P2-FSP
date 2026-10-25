"""Análises: estatísticas descritivas, gráficos, regressões e comparação com o trabalho anterior.

Uso: python codigo/05_analise.py   (a partir da raiz; requer pandas, matplotlib, statsmodels)
Saídas: resultados/*.csv, resultados/regressoes.txt, figuras/*.png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.stattools import durbin_watson, jarque_bera

TRAT = Path("dados/tratados")
RES = Path("resultados"); RES.mkdir(exist_ok=True)
FIG = Path("figuras"); FIG.mkdir(exist_ok=True)

COR = {"Natal/RN": "#2a78d6", "Teresina/PI": "#eb6834"}
MARCA = {"Natal/RN": "o", "Teresina/PI": "s"}
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.color": "#e4e3df", "grid.linewidth": 0.6,
                     "axes.edgecolor": "#8a8984", "axes.labelcolor": "#3d3d3a", "xtick.color": "#5f5e5a",
                     "ytick.color": "#5f5e5a", "legend.frameon": False, "figure.dpi": 150})

bt = pd.read_csv(TRAT / "base_municipios.csv")      # 9 capitais do Nordeste
b = bt[bt.foco].copy()                                 # foco: Natal e Teresina
u = pd.read_csv(TRAT / "base_ucrania.csv")
orig = pd.read_csv(TRAT / "base_original_consolidada.csv")

# ---------------------------------------------------------------------------
# 1. Estatísticas descritivas (R$ de 2025, per capita)
# ---------------------------------------------------------------------------
VARS_DESC = {
    "rec_corrente_real_pc": "Receita corrente per capita",
    "rec_tributaria_real_pc": "Arrecadação própria (tributária) per capita",
    "iptu_real_pc": "IPTU per capita", "iss_real_pc": "ISS per capita",
    "transf_correntes_real_pc": "Transferências correntes per capita",
    "fpm_real_pc": "FPM per capita", "icms_cota_real_pc": "Cota-parte ICMS per capita",
    "desp_total_real_pc": "Despesa total per capita", "desp_pessoal_real_pc": "Despesa com pessoal per capita",
    "desp_investimentos_real_pc": "Investimentos per capita",
    "pib_real_pc": "PIB per capita",
    "ind_autonomia_rc": "Autonomia (rec. tributária / rec. corrente)",
    "ind_dependencia_transf": "Dependência (transf. correntes / rec. corrente)",
    "ind_transf_incondicionais_rc": "Transf. incondicionais (FPM+ICMS+IPVA) / rec. corrente",
    "ind_transf_vinculadas_rc": "Transf. vinculadas (SUS+FUNDEB+FNDE) / rec. corrente",
    "ind_rec_tributaria_pib": "Rec. tributária / PIB",
}
linhas = []
for mun, g in bt.groupby("municipio"):
    for v, rot in VARS_DESC.items():
        s = g[v].dropna()
        cagr = None
        if v.endswith("_pc") and len(s) >= 2:
            a0, a1 = g.loc[s.index[0], "ano"], g.loc[s.index[-1], "ano"]
            cagr = (s.iloc[-1] / s.iloc[0]) ** (1 / (a1 - a0)) - 1
        linhas.append(dict(municipio=mun, variavel=v, descricao=rot, n=len(s), media=s.mean(), dp=s.std(),
                           minimo=s.min(), maximo=s.max(), primeiro_ano=g.loc[s.index[0], "ano"],
                           ultimo_ano=g.loc[s.index[-1], "ano"], valor_inicial=s.iloc[0], valor_final=s.iloc[-1],
                           taxa_crescimento_anual=cagr))
desc = pd.DataFrame(linhas)
desc.to_csv(RES / "estatisticas_descritivas.csv", index=False)

# Tabela de composição da receita corrente (médias do período)
comp = bt.groupby("municipio")[["ind_autonomia_rc", "ind_fpm_rc", "ind_icms_rc", "ind_transf_vinculadas_rc",
                              "ind_dependencia_transf"]].mean().T
comp.to_csv(RES / "composicao_receita_media.csv")

# ---------------------------------------------------------------------------
# 2. Gráficos
# ---------------------------------------------------------------------------
def linha(ax, var, escala=1.0, rotulo_final=True, fmt="{:,.0f}"):
    for mun, g in b.groupby("municipio"):
        g = g.dropna(subset=[var])
        ax.plot(g.ano, g[var] * escala, color=COR[mun], marker=MARCA[mun], lw=2, ms=5, label=mun)
        if rotulo_final and len(g):
            ax.annotate(fmt.format(g[var].iloc[-1] * escala).replace(",", "."), (g.ano.iloc[-1], g[var].iloc[-1] * escala),
                        xytext=(6, 0), textcoords="offset points", va="center", fontsize=8, color="#3d3d3a")
    ax.set_xticks(range(2016, 2026)); ax.tick_params(axis="x", rotation=45)

fig, axs = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
linha(axs[0], "rec_tributaria_real_pc"); axs[0].set_title("Arrecadação própria (tributária)", fontsize=10)
linha(axs[1], "transf_correntes_real_pc"); axs[1].set_title("Transferências correntes", fontsize=10)
axs[0].set_ylabel("R$ de 2025 por habitante"); axs[0].legend(loc="upper left")
axs[0].set_ylim(bottom=0)
fig.suptitle("Receita própria e transferências per capita, 2016–2025 (R$ de 2025)", fontsize=11)
fig.tight_layout(); fig.savefig(FIG / "fig1_receita_propria_transferencias_pc.png"); plt.close(fig)

fig, axs = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
linha(axs[0], "ind_autonomia_rc", 100, fmt="{:.1f}%"); axs[0].set_title("Autonomia: rec. tributária / rec. corrente", fontsize=10)
linha(axs[1], "ind_dependencia_transf", 100, fmt="{:.1f}%"); axs[1].set_title("Dependência: transf. correntes / rec. corrente", fontsize=10)
axs[0].set_ylabel("% da receita corrente"); axs[0].legend(loc="center left"); axs[0].set_ylim(0, 80)
fig.suptitle("Autonomia e dependência fiscal, 2016–2025", fontsize=11)
fig.tight_layout(); fig.savefig(FIG / "fig2_autonomia_dependencia.png"); plt.close(fig)

# Composição das transferências (pequenos múltiplos, um por município – nunca eixo duplo)
comps = {"fpm_real_pc": "FPM", "icms_cota_real_pc": "ICMS", "fundeb_real_pc": "FUNDEB", "sus_real_pc": "SUS"}
cores_c = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]
fig, axs = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
for ax, (mun, g) in zip(axs, b.groupby("municipio")):
    for (v, rot), c in zip(comps.items(), cores_c):
        ax.plot(g.ano, g[v], color=c, lw=2, marker="o", ms=4, label=rot)
    ax.set_title(mun, fontsize=10); ax.set_xticks(range(2016, 2026)); ax.tick_params(axis="x", rotation=45)
    if mun == "Natal/RN":
        ax.annotate("2023–2024: parte do repasse SUS\nregistrada em outras contas da DCA", (2023, g.loc[g.ano == 2023, "sus_real_pc"].iloc[0]),
                    xytext=(-150, -40), textcoords="offset points", fontsize=7, color="#5f5e5a",
                    arrowprops=dict(arrowstyle="-", color="#8a8984", lw=0.6))
axs[0].set_ylabel("R$ de 2025 por habitante"); axs[0].legend(ncol=2, fontsize=8, loc="upper left"); axs[0].set_ylim(bottom=0)
fig.suptitle("Principais transferências per capita (R$ de 2025)", fontsize=11)
fig.tight_layout(); fig.savefig(FIG / "fig3_composicao_transferencias.png"); plt.close(fig)

fig, axs = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
linha(axs[0], "desp_total_real_pc"); axs[0].set_title("Despesa total (exceto intra)", fontsize=10)
linha(axs[1], "desp_pessoal_real_pc"); axs[1].set_title("Pessoal e encargos", fontsize=10)
axs[0].set_ylabel("R$ de 2025 por habitante"); axs[0].legend(loc="upper left"); axs[0].set_ylim(bottom=0)
fig.suptitle("Despesa per capita, 2016–2025 (R$ de 2025)", fontsize=11)
fig.tight_layout(); fig.savefig(FIG / "fig4_despesa_pc.png"); plt.close(fig)

# Dispersão transferências x despesa (flypaper descritivo)
fig, ax = plt.subplots(figsize=(6, 4.5))
for mun, g in b.groupby("municipio"):
    ax.scatter(g.transf_correntes_real_pc, g.desp_total_real_pc, color=COR[mun], marker=MARCA[mun], s=40, label=mun,
               edgecolor="white", linewidth=1)
    for _, r in g.iterrows():
        if r.ano in (2016, 2025):
            ax.annotate(int(r.ano), (r.transf_correntes_real_pc, r.desp_total_real_pc), xytext=(5, -3),
                        textcoords="offset points", fontsize=7, color="#5f5e5a")
ax.set_xlabel("Transferências correntes per capita (R$ de 2025)"); ax.set_ylabel("Despesa total per capita (R$ de 2025)")
ax.legend(); ax.set_title("Transferências e despesa per capita, 2016–2025", fontsize=10)
fig.tight_layout(); fig.savefig(FIG / "fig5_dispersao_transf_despesa.png"); plt.close(fig)

# Ucrânia
uu = u.set_index("ano")
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
ax = axs[0]
for v, rot, c in [("fmi_descentralizacao_receita_pct", "Receita local / receita do gov. geral", "#2a78d6"),
                  ("fmi_descentralizacao_despesa_pct", "Despesa local / despesa do gov. geral", "#eb6834")]:
    s = uu[v].dropna(); ax.plot(s.index, s.values, color=c, lw=2, marker="o", ms=4, label=rot)
ax.axvline(2015, color="#8a8984", lw=0.8, ls="--"); ax.text(2015.1, ax.get_ylim()[1] * 0.97, "reforma 2015", fontsize=7, color="#5f5e5a", va="top")
ax.set_ylabel("%"); ax.set_title("Descentralização (FMI, governo local)", fontsize=10); ax.legend(fontsize=7, loc="lower left"); ax.set_ylim(bottom=0)
ax = axs[1]
s = uu["fmi_dependencia_transf_receita_propria_pct"].dropna()
ax.plot(s.index, s.values, color="#2a78d6", lw=2, marker="o", ms=4)
ax.axvline(2015, color="#8a8984", lw=0.8, ls="--")
ax.set_ylabel("% da receita própria"); ax.set_title("Transferências líquidas / receita própria local", fontsize=10); ax.set_ylim(bottom=0)
fig.suptitle("Ucrânia: descentralização fiscal e dependência de transferências, 2011–2020", fontsize=11)
fig.tight_layout(); fig.savefig(FIG / "fig6_ucrania_descentralizacao.png"); plt.close(fig)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
for ax, v, tit in [(axs[0], "gc_despesa_pib", "Despesa do governo central, % PIB"),
                   (axs[1], "gc_doacoes_outras_pct_receita", "Doações e outras receitas, % da receita")]:
    s = uu.loc[2016:, v].dropna(); ax.plot(s.index, s.values, color="#2a78d6", lw=2, marker="o", ms=4)
    ax.axvspan(2021.5, 2025.5, color="#e4e3df", alpha=0.6, lw=0); ax.set_title(tit, fontsize=10); ax.set_ylim(bottom=0)
    ax.set_xticks(range(2016, 2026)); ax.tick_params(axis="x", rotation=45)
axs[0].text(2021.7, axs[0].get_ylim()[1] * 0.95, "guerra em\nlarga escala", fontsize=7, color="#5f5e5a", va="top")
fig.suptitle("Ucrânia: choque fiscal da guerra (Banco Mundial/WDI)", fontsize=11)
fig.tight_layout(); fig.savefig(FIG / "fig7_ucrania_macro.png"); plt.close(fig)


# Ucrânia – orçamentos locais 2021–2025 (Ministério das Finanças; série distinta da do FMI)
ul = pd.read_csv(TRAT / "base_ucrania_local_2021_2025.csv").set_index("ano")
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
ax = axs[0]
ax.plot(ul.index, ul.receita_propria_fg_real_2025, color="#2a78d6", lw=2, marker="o", ms=5, label="Receita própria (fundo geral)")
ax.plot(ul.index, ul.transferencias_real_2025, color="#eb6834", lw=2, marker="s", ms=5, label="Transferências do Estado")
ax.axvline(2023.5, color="#8a8984", lw=0.8, ls="--")
ax.text(2023.55, 80, "a partir de 2024: ПДФО de\nmilitares vai ao orçamento\ndo Estado", fontsize=7, color="#5f5e5a")
ax.set_ylabel("bilhões de UAH de 2025"); ax.set_ylim(0, 700); ax.legend(fontsize=8, loc="upper center", ncol=2)
ax.set_title("Receita própria e transferências (valores reais)", fontsize=10); ax.set_xticks(ul.index)
ax = axs[1]
ax.plot(ul.index, ul.transf_sobre_receita_propria_pct, color="#2a78d6", lw=2, marker="o", ms=5)
for a, v in ul.transf_sobre_receita_propria_pct.items():
    ax.annotate(f"{v:.0f}%", (a, v), xytext=(0, 7), textcoords="offset points", ha="center", fontsize=8, color="#3d3d3a")
ax.axvline(2023.5, color="#8a8984", lw=0.8, ls="--")
ax.set_ylim(0, 80); ax.set_ylabel("%"); ax.set_xticks(ul.index)
ax.set_title("Transferências / receita própria local", fontsize=10)
fig.suptitle("Ucrânia: orçamentos locais durante a guerra, 2021–2025 (Ministério das Finanças)", fontsize=11)
fig.text(0.01, 0.005, "Nota: 2021 – transferências derivadas (136,8 / 0,675). Deflator: CPI (Banco Mundial). Série não comparável à do FMI (Figura 6).",
         fontsize=7, color="#5f5e5a")
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(FIG / "fig8_ucrania_orcamentos_locais_2021_2025.png"); plt.close(fig)

# ---------------------------------------------------------------------------
# 3. Regressões exploratórias (associação, não causalidade)
# ---------------------------------------------------------------------------
d = b.copy()
d["natal"] = (d.municipio == "Natal/RN").astype(int)
d["t"] = d.ano - 2016
d["covid"] = d.ano.isin([2020, 2021]).astype(int)
for v in ["desp_total", "transf_correntes", "rec_tributaria", "pib", "fpm", "icms_cota", "ipva_cota"]:
    d[v + "_k"] = d[v + "_real_pc"] / 1000 if v != "pib" else d.pib_real_pc / 1000
d["transf_incond_k"] = d.fpm_k + d.icms_cota_k + d.ipva_cota_k
d["transf_vinc_k"] = d.transf_correntes_k - d.transf_incond_k

modelos = {
    # M1 – flypaper clássico: despesa vs transferências e renda local (PIB pc); n = 16 (PIB até 2023)
    "M1_flypaper_despesa": "desp_total_k ~ transf_correntes_k + pib_k + natal",
    # M2 – idem, sem PIB, com tendência (usa os 20 anos-município)
    "M2_despesa_tendencia": "desp_total_k ~ transf_correntes_k + rec_tributaria_k + natal + t",
    # M3 – esforço fiscal (substituição/complementaridade): rec. própria vs transferências incondicionais
    "M3_esforco_fiscal": "rec_tributaria_k ~ transf_incond_k + pib_k + natal",
    # M4 – log-log (elasticidades) da despesa
    "M4_elasticidades": "np.log(desp_total_k) ~ np.log(transf_correntes_k) + np.log(rec_tributaria_k) + natal + covid",
}
saida, coefs = [], []
for nome, f in modelos.items():
    m = smf.ols(f, data=d).fit(cov_type="HC1")
    m_ols = smf.ols(f, data=d).fit()
    bp = het_breuschpagan(m_ols.resid, m_ols.model.exog)
    jb = jarque_bera(m_ols.resid)
    saida.append(f"{'=' * 90}\n{nome}: {f}\n(erros-padrão robustos HC1; n = {int(m.nobs)})\n{m.summary()}\n"
                 f"Breusch-Pagan: LM={bp[0]:.3f} p={bp[1]:.3f} | Durbin-Watson={durbin_watson(m_ols.resid):.3f} | "
                 f"Jarque-Bera p={jb[1]:.3f}\n")
    for k in m.params.index:
        coefs.append(dict(modelo=nome, termo=k, coef=m.params[k], ep_hc1=m.bse[k], p=m.pvalues[k],
                          n=int(m.nobs), r2=m.rsquared, r2_aj=m.rsquared_adj))
    if nome == "M1_flypaper_despesa":
        teste = m.t_test("transf_correntes_k - pib_k = 0")
        saida.append(f"Teste de Wald H0: efeito transferência = efeito renda (PIB pc): {teste}\n")
    if nome == "M2_despesa_tendencia":
        teste = m.t_test("transf_correntes_k - rec_tributaria_k = 0")
        saida.append(f"Teste de Wald H0: efeito transferência = efeito receita própria: {teste}\n")
# Sensibilidade: M1 com população oficial (estimativas sem compatibilização)
d2 = d.copy()
for v in ["desp_total", "transf_correntes"]:
    d2[v + "_k"] = d2[v + "_real"] / d2.pop_oficial / 1000
d2["pib_k"] = d2.pib_real / d2.pop_oficial / 1000
m = smf.ols(modelos["M1_flypaper_despesa"], data=d2).fit(cov_type="HC1")
saida.append(f"{'=' * 90}\nSENSIBILIDADE M1 com população oficial (sem compatibilização com o Censo 2022)\n{m.summary().tables[1]}\n")
for k in m.params.index:
    coefs.append(dict(modelo="M1_sens_pop_oficial", termo=k, coef=m.params[k], ep_hc1=m.bse[k], p=m.pvalues[k],
                      n=int(m.nobs), r2=m.rsquared, r2_aj=m.rsquared_adj))
(RES / "regressoes.txt").write_text("\n".join(saida), encoding="utf-8")
pd.DataFrame(coefs).to_csv(RES / "regressoes_coeficientes.csv", index=False)

# ---------------------------------------------------------------------------
# 4. Comparação com o trabalho anterior (Teresina, R$ correntes)
# ---------------------------------------------------------------------------
mapa = {"Impostos, Taxas e Contribuições de Melhoria": "rec_tributaria", "Contribuições": "rec_contribuicoes",
        "Transferências Correntes": "transf_correntes", "Transferências de Capital": "transf_capital",
        "Operações de Crédito": "operacoes_credito"}
o = orig[orig.descricao.isin(mapa)].copy()
o["variavel"] = o.descricao.map(mapa)
t = b[b.municipio == "Teresina/PI"].melt(id_vars="ano", value_vars=list(set(mapa.values())), var_name="variavel",
                                         value_name="siconfi_nominal")
cmp_ = o.merge(t, on=["ano", "variavel"], how="left")
cmp_["diferenca_pct"] = (cmp_.arrecadado_nominal / cmp_.siconfi_nominal - 1) * 100
cmp_[["ano", "descricao", "arrecadado_nominal", "siconfi_nominal", "diferenca_pct", "coluna_ipca_original",
      "fator_implicito", "inconsistencia_deflator", "ano_incompleto"]].to_csv(RES / "comparacao_trabalho_anterior.csv", index=False)

print(desc[desc.variavel.isin(["rec_tributaria_real_pc", "transf_correntes_real_pc", "ind_autonomia_rc", "ind_dependencia_transf"])]
      [["municipio", "variavel", "valor_inicial", "valor_final", "media", "taxa_crescimento_anual"]].round(3).to_string())
print(pd.DataFrame(coefs).round(3).to_string())
print(cmp_[["ano", "descricao", "diferenca_pct", "inconsistencia_deflator"]].round(2).to_string())


# ---------------------------------------------------------------------------
# 5. Painel das 9 capitais do Nordeste (grupo de comparação)
# ---------------------------------------------------------------------------
import statsmodels.api as sm
from linearmodels.panel import PanelOLS

ORDEM = (bt.groupby("municipio").ind_autonomia_rc.mean().sort_values()).index.tolist()

# Figura 9 – autonomia e dependência médias 2016–2025, por capital (Natal e Teresina destacadas)
med = bt.groupby("municipio")[["ind_autonomia_rc", "ind_dependencia_transf"]].mean().loc[ORDEM] * 100
fig, axs = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)
for ax, v, tit in [(axs[0], "ind_autonomia_rc", "Receita tributária / receita corrente"),
                   (axs[1], "ind_dependencia_transf", "Transferências correntes / receita corrente")]:
    cores = [COR.get(m, "#b4b2a9") for m in med.index]
    ax.barh(range(len(med)), med[v], color=cores, height=0.6, edgecolor="white", linewidth=2)
    for i, val in enumerate(med[v]):
        ax.text(val + 0.6, i, f"{val:.1f}%", va="center", fontsize=8, color="#3d3d3a")
    ax.set_title(tit, fontsize=10); ax.set_xlim(0, max(med[v]) * 1.18); ax.grid(axis="y", visible=False)
axs[0].set_yticks(range(len(med))); axs[0].set_yticklabels(med.index)
fig.suptitle("Capitais do Nordeste: autonomia e dependência médias, 2016–2025 (%)", fontsize=11)
fig.tight_layout(); fig.savefig(FIG / "fig9_capitais_ne_autonomia.png"); plt.close(fig)

# Figura 10 – trajetória da receita própria e das transferências per capita (Natal e Teresina vs. demais capitais)
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
for ax, v, tit in [(axs[0], "rec_tributaria_real_pc", "Arrecadação própria per capita"),
                   (axs[1], "transf_correntes_real_pc", "Transferências correntes per capita")]:
    for mun, g in bt.groupby("municipio"):
        if mun in COR:
            continue
        ax.plot(g.ano, g[v], color="#c9c7bf", lw=1)
    mediana = bt[~bt.foco].groupby("ano")[v].median()
    ax.plot(mediana.index, mediana.values, color="#5f5e5a", lw=2, ls="--", label="Mediana das outras 7 capitais")
    for mun, g in b.groupby("municipio"):
        ax.plot(g.ano, g[v], color=COR[mun], marker=MARCA[mun], ms=4, lw=2, label=mun)
    ax.set_title(tit, fontsize=10); ax.set_xticks(range(2016, 2026)); ax.tick_params(axis="x", rotation=45); ax.set_ylim(bottom=0)
axs[0].set_ylabel("R$ de 2025 por habitante"); axs[0].legend(fontsize=8, loc="upper left")
fig.suptitle("Natal e Teresina no contexto das capitais do Nordeste (R$ de 2025)", fontsize=11)
fig.tight_layout(); fig.savefig(FIG / "fig10_capitais_ne_trajetorias.png"); plt.close(fig)

# Painel: efeitos fixos de município e de ano; erros-padrão agrupados por município (9 clusters) e, por robustez,
# Driscoll-Kraay (dependência transversal). Valores em R$ mil de 2025 por habitante.
pn = bt.copy()
for v in ["desp_total", "transf_correntes", "rec_tributaria", "fpm", "icms_cota", "ipva_cota"]:
    pn[v + "_k"] = pn[v + "_real_pc"] / 1000
pn["pib_k"] = pn.pib_real_pc / 1000
pn["transf_incond_k"] = pn.fpm_k + pn.icms_cota_k + pn.ipva_cota_k
pn["transf_vinc_k"] = pn.transf_correntes_k - pn.transf_incond_k
pn["transf_x_foco"] = pn.transf_correntes_k * pn.foco.astype(int)
pn = pn.set_index(["municipio", "ano"])

PAINEL = {
    "P0_flypaper_EF_municipio": ("desp_total_k", ["transf_correntes_k", "pib_k"]),
    "P0b_esforco_EF_municipio": ("rec_tributaria_k", ["transf_incond_k", "pib_k"]),
    "P1_flypaper_TWFE": ("desp_total_k", ["transf_correntes_k", "pib_k"]),
    "P2_flypaper_sem_pib_2016_2025": ("desp_total_k", ["transf_correntes_k", "rec_tributaria_k"]),
    "P3_incond_vs_vinculadas": ("desp_total_k", ["transf_incond_k", "transf_vinc_k", "pib_k"]),
    "P4_esforco_fiscal": ("rec_tributaria_k", ["transf_incond_k", "pib_k"]),
    "P5_flypaper_foco": ("desp_total_k", ["transf_correntes_k", "transf_x_foco", "pib_k"]),
    "P6_robustez_sem_atipicos": ("desp_total_k", ["transf_correntes_k", "pib_k"]),
    "P7_robustez_sem_pandemia": ("desp_total_k", ["transf_correntes_k", "pib_k"]),
}
FILTRO = {"P6_robustez_sem_atipicos": lambda df: df[~df.flag_qualquer],
          "P7_robustez_sem_pandemia": lambda df: df[~df.index.get_level_values(1).isin([2020, 2021])]}
saida_p, coefs_p = [], []
for nome, (y, xs) in PAINEL.items():
    dd = FILTRO.get(nome, lambda df: df)(pn)[[y] + xs].dropna()
    so_ef_mun = nome.startswith("P0")
    mod = PanelOLS(dd[y], dd[xs], entity_effects=True, time_effects=not so_ef_mun)
    r_cl = mod.fit(cov_type="clustered", cluster_entity=True)
    r_dk = mod.fit(cov_type="kernel")
    efs = "EF município" if so_ef_mun else "EF município + EF ano"
    saida_p.append(f"{'=' * 90}\n{nome}: {y} ~ {' + '.join(xs)} + {efs}\n"
                   f"n = {int(r_cl.nobs)}; municípios = {dd.index.get_level_values(0).nunique()}; "
                   f"anos = {dd.index.get_level_values(1).min()}–{dd.index.get_level_values(1).max()}\n"
                   f"[Erros-padrão agrupados por município]\n{r_cl.summary.tables[1]}\n"
                   f"R² within = {r_cl.rsquared_within:.3f}\n[Erros-padrão Driscoll-Kraay]\n{r_dk.summary.tables[1]}\n")
    for k in xs:
        coefs_p.append(dict(modelo=nome, efeitos=efs, termo=k, coef=r_cl.params[k], ep_cluster=r_cl.std_errors[k],
                            p_cluster=r_cl.pvalues[k], ep_dk=r_dk.std_errors[k], p_dk=r_dk.pvalues[k],
                            n=int(r_cl.nobs), r2_within=r_cl.rsquared_within))
    if nome in ("P0_flypaper_EF_municipio", "P1_flypaper_TWFE"):
        w = r_cl.wald_test(formula="transf_correntes_k = pib_k")
        saida_p.append(f"Wald H0: efeito transferência = efeito renda (PIB pc): estat = {w.stat:.3f}, p = {w.pval:.4f}\n")
    if nome == "P2_flypaper_sem_pib_2016_2025":
        w = r_cl.wald_test(formula="transf_correntes_k = rec_tributaria_k")
        saida_p.append(f"Wald H0: efeito transferência = efeito receita própria: estat = {w.stat:.3f}, p = {w.pval:.4f}\n")
    if nome == "P3_incond_vs_vinculadas":
        w = r_cl.wald_test(formula="transf_incond_k = transf_vinc_k")
        saida_p.append(f"Wald H0: incondicionais = vinculadas: estat = {w.stat:.3f}, p = {w.pval:.4f}\n")
(RES / "regressoes_painel.txt").write_text("\n".join(saida_p), encoding="utf-8")
pd.DataFrame(coefs_p).to_csv(RES / "regressoes_painel_coeficientes.csv", index=False)
print(pd.DataFrame(coefs_p).round(3).to_string())
