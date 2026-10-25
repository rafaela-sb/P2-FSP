# Registro de atualizações e correções

**Trabalho anterior:** COSTA, Cleiton Santana. *P1 – Finanças do Setor Público* (Ucrânia; Natal/RN; Teresina/PI). UnB, 2026/1. Repositório: https://github.com/snakecs/Prova-Finan-as-setor-p-blico. A cópia integral e intocada está em `dados/original/`.

## 1. O que havia no trabalho anterior

| Item | Situação na P1 |
|---|---|
| Teresina – receitas | 22 planilhas (`Receita Arrecadada por Natureza AAAA.xlsx`), 2016–2026, só grupos de receita corrente e de capital, extraídas do portal da transparência da prefeitura, com uma coluna "IPCA" |
| Teresina – despesas | Ausente (só citada no texto) |
| Natal | Nenhum arquivo de dados (só citada no texto) |
| Transferências desagregadas (FPM, ICMS, FUNDEB, SUS) | Ausentes |
| População e PIB | Ausentes (o `Metodologia.docx` cita o IBGE, mas não há arquivo) |
| Ucrânia | Só descrição institucional, sem dados |
| Deflator | Coluna "IPCA" sem ano-base nem fórmula documentados |
| Códigos/procedimentos | Ausentes |
| Arquivo `prova finanças publicas.rar` | Duplica as planilhas acima |

## 2. Conferência dos valores nominais da P1 contra o Siconfi

Os valores nominais de Teresina na P1 foram comparados com a DCA do Siconfi (`resultados/comparacao_trabalho_anterior.csv`). Em 2016–2025, **todos os grupos conferem exatamente** (diferença 0,00%), exceto "Impostos, Taxas e Contribuições de Melhoria" de 2021, que difere em +0,23%. A divergência é atribuível à diferença entre o portal municipal e a DCA homologada.

## 3. Inconsistências encontradas e corrigidas

| # | Problema na P1 | Evidência | Correção na P2 |
|---|---|---|---|
| 1 | Coluna "IPCA" com fator errado em 5 células | Fator implícito (IPCA ÷ nominal) muito diferente da mediana do ano: Transf. de capital 2020 (×13,75 contra ×1,38), Transf. correntes 2021 (×0,12 contra ×1,24), Impostos 2018 (×1,00 contra ×1,48), Impostos 2024 (×0,064 contra ×1,07) e Alienação de bens 2024 (×0,011 contra ×1,07) | Deflacionamento refeito por fórmula única e reproduzível (IPCA médio anual, base 2025). As células com erro estão marcadas em `base_original_consolidada.csv` (`inconsistencia_deflator`) |
| 2 | Ano-base do deflator não informado | Os fatores medianos da P1 são cerca de 2% maiores que os da P2, o que sugere base em 2026 (ano incompleto) | Ano-base 2025, último ano completo |
| 3 | Inclusão de 2026 (ano incompleto) | Planilhas de 2026 com valores parciais | 2026 excluído; período 2016–2025 |
| 4 | Fonte não padronizada (portal da prefeitura) | Impede a comparação com Natal | Siconfi/DCA para os dois municípios |
| 5 | Ausência de Natal, despesas, transferências, população, PIB e dados da Ucrânia | Ver item 1 | Base reconstruída a partir das fontes oficiais (seção 4) |

## 4. Inclusões (dados brutos atualizados)

| Conjunto | Arquivos em `dados/brutos/` | Linhas | Script |
|---|---|---|---|
| DCA Anexo I-C, I-D, I-E – Natal, Teresina e as demais 7 capitais do Nordeste (comparação), 2014–2025 | `siconfi/dca_*.csv` (324 arquivos) | ~80 mil | `codigo/01_coleta_siconfi.py` |
| População (estimativas, Censos 2010 e 2022), PIB municipal, IPCA | `ibge/*.csv` (5 arquivos) | 456 | `codigo/02_coleta_ibge.py` |
| Ucrânia – FMI Fiscal Decentralization; Banco Mundial WDI | `ucrania/imf_fd_ucrania.csv`, `ucrania/wdi_ucrania.csv` | 2.248 | `codigo/03_coleta_ucrania.py` |
| Ucrânia – orçamentos locais 2021–2025 (Ministério das Finanças) | `ucrania/mof_orcamentos_locais_2021_2025.csv` | 41 | Transcrição manual documentada (fonte e URL por linha), porque não há API |

Os anos 2014–2015 foram baixados para conferência, mas a análise usa 2016–2025, os dez anos mais recentes com DCA completa para os dois entes. Dados acessados em 22/10/2026.

## 5. Quebras de série, mudanças de classificação e problemas nas fontes

| # | Ocorrência | Tratamento |
|---|---|---|
| Q1 | **Ementário da receita mudou em 2018 e em 2022.** Exemplos: IPTU 1.1.1.2.02 → 1.1.1.8.01.1 → 1.1.1.2.50; FPM 1.7.2.1.01.02 → 1.7.1.8.01.2 → 1.7.1.1.51 | Agregados (1.0, 1.1, 1.7, 2.0) por código, que é estável; componentes pelo nome da conta, com regra de hierarquia contra dupla contagem (`04_tratamento.py`, funções `sig` e `soma_sem_dupla_contagem`) |
| Q2 | **População:** as estimativas 2016–2021 (base Censo 2010) superestimaram Natal (896,7 mil em 2021 contra 751,3 mil no Censo 2022, cerca de 19%). Não há estimativa em 2022 (ano do Censo) nem em 2023 | `pop` compatibilizada: interpolação geométrica 2010–2022 para 2016–2021; Censo em 2022; interpolação linear em 2023. Série oficial mantida em `pop_oficial` e testada como sensibilidade |
| Q3 | **PIB municipal** disponível só até 2023 | 2024–2025 = NA; modelos com PIB usam 16 observações |
| Q4 | **Natal 2023–2024 – SUS:** o repasse da Atenção Especializada (R$ 316 mi em 2022; R$ 484 mi em 2025) some da conta SUS. Em 2023 aparece R$ 404 mi em "Transferências da União a Consórcios Públicos" (1.7.1.9.52) e em 2024 R$ 476 mi em "Outras Transferências da União" (1.7.1.9.99) | Não reclassificado, porque seria inferência. `sus` fica como declarado, com `flag_sus_reclassificado`. As análises principais usam `transf_correntes` (agregado), que não é afetado |
| Q5 | **Natal 2016–2018 – dedução do FUNDEB** declarada de forma inconsistente (R$ 0,1 mi; ausente; −R$ 133,8 mi) | Toda a análise usa receita **bruta**; `flag_deducao_fundeb_inconsistente` |
| Q6 | **Natal 2017–2018 – Anexo I-D** declarado só no nível de grupo ("A definir"), sem separar a parcela intraorçamentária | `desp_total` vem do Anexo I-E; os grupos de natureza desses anos podem conter despesa intra (`flag_natureza_agregada`) |
| Q7 | Os agregados "DO" do Anexo I-D incluem a modalidade 91 (intraorçamentária) | Modalidade 91 descontada; conferência I-D × I-E em `checagens.csv` (14 de 20 casos com diferença < 0,5%) |
| Q8 | Linha "Receitas exceto intraorçamentárias" inexistente na DCA até 2018 | `rec_total = rec_corrente + rec_capital`, que confere com o total declarado em 2019–2025 |
| Q9 | API do FMI devolve as razões como fração (0,15) apesar do sufixo "_PT" | Multiplicado por 100 |
| Q12 | Demais capitais: valores declarados atípicos — João Pessoa 2018 (SUS quase zerado), FUNDEB ausente ou muito baixo em São Luís 2018, 2019 e 2021 e em João Pessoa 2019, IPTU de Salvador 2024 (R$ 2,63 bi, mais que o dobro de 2023 e 2025) | Mantidos como declarados; sinalizados (`flag_fundeb_atipico`, `flag_iptu_atipico`, `flag_sus_reclassificado`); modelo P6 os exclui |
| Q11 | Ucrânia 2021–2025: dados locais só em comunicados e notas do Ministério das Finanças. O ПДФО de militares saiu dos orçamentos locais a partir de 2024, a parcela local do ПДФО subiu de 60% para 64% em 2022, e tributos sobre terra e imóveis foram suspensos em áreas de combate ou ocupadas a partir de março de 2022 | Série separada da do FMI (conceitos diferentes); quebra de 2024 sinalizada (`quebra_pdfo_militar`); valor de 2023 em base comparável registrado; transferências de 2021 derivadas e sinalizadas |
| Q10 | Ucrânia: FMI-FD termina em 2020; WDI sem algumas séries fiscais para 2024–2025; guerra desde fev/2022; Crimeia e partes de Donetsk e Luhansk fora das estatísticas desde 2014 | Coberturas distintas justificadas no dicionário; período ucraniano dividido em três fases (`periodo`) |

## 6. Novas análises (não existiam na P1)

- Estatísticas descritivas e taxas de crescimento real per capita (`resultados/estatisticas_descritivas.csv`).
- Indicadores de autonomia, dependência e composição das transferências.
- Sete figuras (`figuras/`).
- Painel das 9 capitais do Nordeste (efeitos fixos de município e de ano; erros agrupados e Driscoll-Kraay; robustez sem valores atípicos e sem 2020–2021) em `resultados/regressoes_painel.txt`; Figuras 9 e 10.
- Quatro modelos de regressão exploratórios (efeito flypaper e esforço fiscal) com diagnósticos (Breusch-Pagan, Durbin-Watson, Jarque-Bera), testes de Wald e análise de sensibilidade à série de população (`resultados/regressoes.txt`).
- Indicadores de descentralização fiscal da Ucrânia (FMI, 2011–2020), orçamentos locais durante a guerra (Ministério das Finanças, 2021–2025) e choque fiscal da guerra (WDI).

## 7. Materiais reaproveitados do trabalho anterior

Só as planilhas de receita de Teresina, usadas para conferência (seção 2) e preservadas em `dados/original/`. Nenhum texto da P1 foi reaproveitado no artigo.

## 8. Estudo bibliométrico e artigo

- Base Scopus exportada pelo Portal de Periódicos da CAPES (acesso CAFe/UnB) em 22/10/2026: 1.444 artigos, `bibliometria/scopus.csv`; string de busca em `bibliometria/bibliometria.R`.
- Análise com bibliometrix 5.5.0 (R 4.5): resumo, produção anual, periódicos, países, palavras-chave, mapa temático, Bradford e Tabela 1 no formato de Baker, Larcker e Wang (2022).
- 94 referências de artigos científicos (80 da base Scopus, metadados do próprio Scopus; 14 conferidas no Crossref), todas citadas no texto (verificação automática em `artigo/trabalho/`).
- Formatação conforme a ABNT: NBR 6022 (artigo), 6023 (lista única de referências em ordem alfabética, alinhada à esquerda), 6024 (numeração progressiva), 6028 (resumo com até 250 palavras) e 10520:2023 (citações com sobrenome em caixa alta e baixa entre parênteses); figuras com título acima e fonte abaixo.
