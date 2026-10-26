# P2 – Finanças do Setor Público (CCA0169) – Matrícula 241003384

**Rafaela de Sousa Barbosa** · **Universidade de Brasília** · Prof. Lucas Oliveira Gomes Ferreira · 2026/2  
**Unidades:** Natal/RN e Teresina/PI (municípios; demais capitais do Nordeste como grupo de comparação) · Ucrânia (país)  
**Tema:** transferências intergovernamentais, autonomia fiscal e efeito flypaper

Este repositório reúne os dois produtos da P2: (1) a base de dados atualizada e ampliada a partir do trabalho anterior e (2) o artigo científico.

## Organização

```
artigo/                     Artigo: 241003384_artigo.pdf (entrega), .docx editável, fonte em Markdown e script gerar_pdf.sh
dados/
  original/                 Cópia intocada do trabalho anterior (P1, Cleiton S. Costa)
  brutos/
    siconfi/                DCA (Anexos I-C, I-D, I-E) das 9 capitais do Nordeste, 2014–2025, como a API devolve
    ibge/                   População, PIB municipal e IPCA (SIDRA)
    ucrania/                FMI (Fiscal Decentralization), Banco Mundial (WDI) e Ministério das Finanças (transcrição com fontes)
  tratados/
    base_municipios.csv     Base analítica dos municípios (nominal, real, per capita, indicadores)
    base_ucrania.csv        Base analítica da Ucrânia (FMI 2011–2020 + Banco Mundial)
    base_ucrania_local_2021_2025.csv   Orçamentos locais ucranianos na guerra (Ministério das Finanças)
    siconfi_nominal_longo.csv
    base_original_consolidada.csv   Planilhas da P1 empilhadas, com verificação do deflator
    checagens.csv           Testes de consistência contábil
    base_p2_241003384.xlsx  Todas as bases e resultados em uma planilha
codigo/                     Scripts de coleta, tratamento e análise (executar em ordem)
resultados/                 Estatísticas descritivas, regressões, comparação com a P1
figuras/                    Figuras do artigo
bibliometria/               Base Scopus (scopus.zip → scopus.csv, 1.444 artigos; o script descompacta), script do bibliometrix, figuras e resultados (Tabela 1 no estilo de Baker et al., 2022)
documentacao/
  dicionario_variaveis.md   Conceito, fonte, endereço, cobertura, unidade, ausentes e fórmulas de cada variável
  registro_alteracoes.md    O que foi atualizado, corrigido e ampliado em relação à P1
```

## Como reproduzir

Requisitos: Python ≥ 3.10 com `pandas`, `matplotlib`, `statsmodels`, `linearmodels`, `openpyxl` (`pip install -r requirements.txt`) e R com `bibliometrix` para a bibliometria. Execute a partir da raiz do repositório:

```bash
python codigo/01_coleta_siconfi.py    # baixa as DCA do Siconfi (API do Tesouro)
python codigo/02_coleta_ibge.py       # baixa população, PIB e IPCA (API SIDRA)
python codigo/03_coleta_ucrania.py    # baixa dados do FMI e do Banco Mundial
python codigo/04_tratamento.py        # gera dados/tratados/
python codigo/05_analise.py           # gera resultados/ e figuras/
python codigo/06_exportar_excel.py    # consolida tudo em .xlsx
Rscript bibliometria/bibliometria.R   # estudo bibliométrico (bibliometrix) sobre bibliometria/scopus.csv
cd artigo && ./gerar_pdf.sh           # monta o artigo (pandoc + xelatex)
```

As etapas 4 a 6 rodam só com os arquivos já incluídos em `dados/brutos/`. Repetir as etapas 1 a 3 pode trazer pequenas diferenças se as fontes revisarem os dados (acesso original em 22/10/2026).

## Principais decisões metodológicas

- **Período:** 2016–2025 para os municípios, os dez anos mais recentes com DCA completa. Ucrânia: 2011–2020 para a descentralização (FMI), 2021–2025 para os orçamentos locais (Ministério das Finanças, série não emendada à do FMI) e 2016–2025 para indicadores macrofiscais.
- **Valores reais:** IPCA médio anual, R$ de 2025. Ucrânia: CPI, UAH de 2025, ou razões sobre o PIB.
- **Receita bruta** (antes da dedução do FUNDEB) e **despesa empenhada exceto intraorçamentária**.
- **Ausentes nunca viram zero.** Quebras de série e problemas das fontes estão documentados e sinalizados com colunas `flag_*`.

## Trabalho anterior

COSTA, Cleiton Santana. *P1 – Finanças do Setor Público*. UnB, 2026/1. https://github.com/snakecs/Prova-Finan-as-setor-p-blico. Os materiais reaproveitados estão identificados em `documentacao/registro_alteracoes.md`.

## Principais resultados

- Autonomia média (receita tributária/receita corrente, 2016–2025): Natal 30,4%; Teresina 18,5% (a menor entre as 9 capitais do Nordeste).
- Efeitos fixos de município: R$ 1,28 de despesa por R$ 1,00 de transferência per capita; PIB per capita sem efeito (Wald p < 0,001). Com efeitos fixos de ano, a associação desaparece (não causal).
- Sem evidência de substituição do esforço fiscal: a receita própria cresceu mais que as transferências.
- Ucrânia: a razão transferências/receita própria local caiu de 143,9% (2015) para 48,6% (2020) e ficou entre 34% e 58% durante a guerra (2021–2025).
