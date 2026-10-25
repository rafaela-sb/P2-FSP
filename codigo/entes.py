"""Entes analisados. FOCO = municípios atribuídos (Natal e Teresina); demais capitais do Nordeste = grupo de comparação."""
ENTES = {  # código IBGE: (identificador de arquivo, nome)
    2408102: ("natal", "Natal/RN"),
    2211001: ("teresina", "Teresina/PI"),
    2111300: ("sao_luis", "São Luís/MA"),
    2304400: ("fortaleza", "Fortaleza/CE"),
    2507507: ("joao_pessoa", "João Pessoa/PB"),
    2611606: ("recife", "Recife/PE"),
    2704302: ("maceio", "Maceió/AL"),
    2800308: ("aracaju", "Aracaju/SE"),
    2927408: ("salvador", "Salvador/BA"),
}
FOCO = {"Natal/RN", "Teresina/PI"}
