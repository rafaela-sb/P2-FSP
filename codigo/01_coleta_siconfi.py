"""Coleta das DCA (Siconfi/Tesouro Nacional) de Natal/RN, Teresina/PI e demais capitais do Nordeste (comparação).
Uso: python codigo/01_coleta_siconfi.py   (executar a partir da raiz do repositório)
Saída: dados/brutos/siconfi/dca_<anexo>_<ente>_<ano>.csv (exatamente como a API devolve)"""
import csv, json, sys, time, urllib.parse, urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from entes import ENTES as _E

API = "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca"
ENTES = {c: v[0] for c, v in _E.items()}
ANEXOS = {"DCA-Anexo I-C": "receitas", "DCA-Anexo I-D": "despesas_natureza", "DCA-Anexo I-E": "despesas_funcao"}
ANOS = range(2014, 2026)
OUT = Path("dados/brutos/siconfi")

def baixar(ano, anexo, ente):
    itens, offset = [], 0
    while True:
        q = urllib.parse.urlencode({"an_exercicio": ano, "no_anexo": anexo, "id_ente": ente, "offset": offset})
        for tentativa in range(4):
            try:
                with urllib.request.urlopen(f"{API}?{q}", timeout=90) as r:
                    d = json.load(r); break
            except Exception as e:
                time.sleep(3 * (tentativa + 1)); err = e
        else:
            raise err
        itens += d["items"]
        if not d.get("hasMore"): return itens
        offset += d["limit"]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for ente, nome in ENTES.items():
        for anexo, sufixo in ANEXOS.items():
            for ano in ANOS:
                arq0 = OUT / f"dca_{sufixo}_{nome}_{ano}.csv"
                if arq0.exists():
                    continue
                itens = baixar(ano, anexo, ente)
                arq = OUT / f"dca_{sufixo}_{nome}_{ano}.csv"
                if not itens:
                    print(f"SEM DADOS: {nome} {ano} {anexo}"); continue
                with open(arq, "w", newline="", encoding="utf-8") as f:
                    w = csv.DictWriter(f, fieldnames=list(itens[0].keys())); w.writeheader(); w.writerows(itens)
                print(f"ok {arq.name}: {len(itens)} linhas")
