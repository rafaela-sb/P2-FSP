"""Exporta as bases tratadas e os resultados para uma planilha Excel única (formato editável).
Uso: python codigo/06_exportar_excel.py  (a partir da raiz). Saída: dados/tratados/base_p2_241003384.xlsx"""
from pathlib import Path
import pandas as pd

T, R = Path("dados/tratados"), Path("resultados")
abas = {
    "municipios": T / "base_municipios.csv",
    "ucrania": T / "base_ucrania.csv",
    "ucrania_local_2021_2025": T / "base_ucrania_local_2021_2025.csv",
    "siconfi_nominal_longo": T / "siconfi_nominal_longo.csv",
    "original_P1": T / "base_original_consolidada.csv",
    "checagens": T / "checagens.csv",
    "descritivas": R / "estatisticas_descritivas.csv",
    "regressoes": R / "regressoes_coeficientes.csv",
    "comparacao_P1": R / "comparacao_trabalho_anterior.csv",
}
with pd.ExcelWriter(T / "base_p2_241003384.xlsx") as w:
    for nome, f in abas.items():
        pd.read_csv(f).to_excel(w, sheet_name=nome, index=False)
print("ok base_p2_241003384.xlsx")
