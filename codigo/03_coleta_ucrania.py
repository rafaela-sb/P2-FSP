"""Coleta de dados da Ucrânia.
(1) FMI – Fiscal Decentralization (FD), indicadores de descentralização por nível de governo (2001–2020).
(2) Banco Mundial – World Development Indicators (macro e finanças do governo central, 2010–2025).
Uso: python codigo/03_coleta_ucrania.py  (a partir da raiz). Saída: dados/brutos/ucrania/*.csv"""
import csv, json, urllib.request
from pathlib import Path
OUT = Path("dados/brutos/ucrania")
IMF_FD = "https://api.imf.org/external/sdmx/2.1/data/IMF.STA,FD/UKR...A"
WDI = {
    "NY.GDP.MKTP.CN": "PIB, UAH correntes",
    "NY.GDP.MKTP.KD.ZG": "Crescimento real do PIB, % a.a.",
    "NY.GDP.DEFL.ZS": "Deflator implícito do PIB (2010=100)",
    "FP.CPI.TOTL": "Índice de preços ao consumidor (2010=100)",
    "FP.CPI.TOTL.ZG": "Inflação ao consumidor, % a.a.",
    "SP.POP.TOTL": "População total",
    "PA.NUS.FCRF": "Taxa de câmbio oficial, UAH por US$",
    "GC.REV.XGRT.GD.ZS": "Receita do governo central exceto doações, % PIB",
    "GC.TAX.TOTL.GD.ZS": "Receita tributária do governo central, % PIB",
    "GC.XPN.TOTL.GD.ZS": "Despesa do governo central, % PIB",
    "GC.NLD.TOTL.GD.ZS": "Resultado (capacidade/necessidade de financiamento) do governo central, % PIB",
    "GC.DOD.TOTL.GD.ZS": "Dívida do governo central, % PIB",
    "GC.REV.GOTR.ZS": "Doações e outras receitas, % da receita",
    "GC.XPN.TRFT.ZS": "Subsídios e outras transferências, % da despesa",
    "MS.MIL.XPND.GD.ZS": "Despesa militar, % PIB",
}
def get(url, accept=None):
    req = urllib.request.Request(url, headers={"Accept": accept} if accept else {})
    with urllib.request.urlopen(req, timeout=240) as r: return r.read().decode("utf-8")
if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    txt = get(IMF_FD, "application/vnd.sdmx.data+csv;version=1.0.0")
    linhas = [l for l in csv.DictReader(txt.splitlines()) if l.get("COUNTRY")]
    cols = ["COUNTRY", "INDICATOR", "SECTOR", "FREQUENCY", "TIME_PERIOD", "OBS_VALUE", "UNIT", "SERIES_NAME"]
    with open(OUT / "imf_fd_ucrania.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(linhas)
    print(f"ok imf_fd_ucrania.csv: {len(linhas)} linhas")
    out = []
    for cod, desc in WDI.items():
        d = json.loads(get(f"https://api.worldbank.org/v2/country/UKR/indicator/{cod}?format=json&date=2010:2025&per_page=100"))
        for o in (d[1] or []):
            out.append({"indicador": cod, "descricao_pt": desc, "descricao_wb": o["indicator"]["value"], "ano": o["date"], "valor": o["value"], "atualizado_wb": d[0].get("lastupdated")})
    with open(OUT / "wdi_ucrania.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
    print(f"ok wdi_ucrania.csv: {len(out)} linhas")
