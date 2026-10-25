"""Coleta IBGE/SIDRA: população (estimativas e Censos), PIB municipal e IPCA.
Uso: python codigo/02_coleta_ibge.py  (a partir da raiz). Saída: dados/brutos/ibge/*.csv"""
import csv, json, sys, urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from entes import ENTES
OUT = Path("dados/brutos/ibge")
MUN = ",".join(str(c) for c in ENTES)
CONSULTAS = {
    "populacao_estimada_t6579": f"6579/n6/{MUN}/v/9324/p/all",
    "populacao_censo2022_t4709": f"4709/n6/{MUN}/v/93/p/all",
    "populacao_censo2010_t202": f"202/n6/{MUN}/v/93/p/2010/c2/0/c1/0",
    "pib_municipal_t5938": f"5938/n6/{MUN}/v/37,513,517,6575,525,543/p/all",
    "ipca_indice_mensal_t1737": "1737/n1/all/v/2266/p/201401-202512",
}
def sidra(q):
    with urllib.request.urlopen(f"https://apisidra.ibge.gov.br/values/t/{q}", timeout=120) as r:
        d = json.load(r)
    cab = d[0]; return [{cab[k]: v for k, v in linha.items()} for linha in d[1:]]
if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for nome, q in CONSULTAS.items():
        linhas = sidra(q)
        with open(OUT / f"{nome}.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(linhas[0].keys())); w.writeheader(); w.writerows(linhas)
        print(f"ok {nome}: {len(linhas)} linhas")
