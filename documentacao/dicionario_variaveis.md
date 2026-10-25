# Dicionário de variáveis

Bases: `dados/tratados/base_municipios.csv` (9 capitais do Nordeste, 2016–2025, 90 linhas; foco em Natal/RN e Teresina/PI, coluna `foco`) `dados/tratados/base_ucrania.csv` (Ucrânia, 2011–2025, 15 linhas) e `dados/tratados/base_ucrania_local_2021_2025.csv` (orçamentos locais ucranianos, 5 linhas). A mesma informação está em `dados/tratados/base_p2_241003384.xlsx`.

## Convenções gerais

| Item | Regra |
|---|---|
| Unidade das variáveis fiscais municipais | R$ correntes (sem sufixo); `_real` = R$ de 2025; `_real_pc` = R$ de 2025 por habitante |
| Deflator | IPCA (IBGE, SIDRA tabela 1737, número-índice dez/1993 = 100), **média anual**; `fator_real_2025 = IPCA_médio_2025 / IPCA_médio_ano`. Valor real = nominal × fator |
| Conceito de receita | "Receitas Brutas Realizadas" da DCA – Anexo I-C (antes das deduções para o FUNDEB) |
| Conceito de despesa | "Despesas Empenhadas" da DCA – Anexos I-D e I-E, **exceto intraorçamentárias** |
| Ausentes | Mantidos vazios (NA). Nenhum ausente foi substituído por zero |
| Per capita | Dividido pela variável `pop` (série compatibilizada; ver abaixo) |
| Códigos dos entes | IBGE: Natal 2408102; Teresina 2211001 (foco). Comparação: São Luís 2111300; Fortaleza 2304400; João Pessoa 2507507; Recife 2611606; Maceió 2704302; Aracaju 2800308; Salvador 2927408 (lista em `codigo/entes.py`) |

## Fontes

| Fonte | Endereço | Uso |
|---|---|---|
| Siconfi/Finbra – DCA (Tesouro Nacional) | API: https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca · consulta: https://siconfi.tesouro.gov.br | Receitas (Anexo I-C), despesas por natureza (I-D) e por função (I-E), 2014–2025 |
| IBGE/SIDRA | https://apisidra.ibge.gov.br · https://sidra.ibge.gov.br | População (t6579, t4709, t202), PIB municipal (t5938), IPCA (t1737) |
| FMI – Fiscal Decentralization (FD) | https://data.imf.org/en/datasets/IMF.STA:FD · API: https://api.imf.org/external/sdmx/2.1/data/IMF.STA,FD/UKR...A | Indicadores de descentralização da Ucrânia (governo local, 2001–2020) |
| Banco Mundial – WDI | https://data.worldbank.org · API: https://api.worldbank.org/v2/country/UKR/indicator/{código} | PIB, inflação, população, câmbio e finanças do governo central da Ucrânia |

## Municípios – variáveis fiscais (R$ correntes)

| Variável | Definição | Origem na DCA (Anexo; identificação) | Cobertura | Observações |
|---|---|---|---|---|
| `rec_corrente` | Receitas correntes | I-C; conta 1.0.0.0 | 2016–2025, ambos | – |
| `rec_capital` | Receitas de capital | I-C; conta 2.0.0.0 | 2016–2025 | – |
| `rec_total` | Receita orçamentária total | `rec_corrente + rec_capital` | 2016–2025 | Igual ao total declarado em 2019–2025 (testado em `checagens.csv`) |
| `rec_total_declarada` | Total "Receitas exceto intraorçamentárias" | I-C; linha `ReceitasExcetoIntraOrcamentarias` | 2019–2025 | Linha inexistente até 2018 |
| `rec_tributaria` (= `arrecadacao_propria`) | Impostos, taxas e contribuições de melhoria | I-C; conta 1.1 | 2016–2025 | Medida principal de arrecadação própria |
| `iptu`, `itbi`, `iss`, `irrf`, `taxas` | Componentes da receita tributária | I-C; identificados pelo **nome** da conta dentro de 1.1 | 2016–2025 | O código mudou em 2018 e 2022; regra de hierarquia evita dupla contagem |
| `rec_contribuicoes` | Contribuições (inclui RPPS e COSIP) | I-C; conta 1.2 | 2016–2025 | Não entra na arrecadação própria tributária |
| `transf_correntes` | Transferências correntes | I-C; conta 1.7 | 2016–2025 | – |
| `fpm` | Cota-parte do FPM (inclui cotas extraordinárias de 1%) | I-C; nome "Fundo de Participação dos Municípios" em 1.7 | 2016–2025 | Bruto, antes da dedução de 20% ao FUNDEB |
| `icms_cota`, `ipva_cota` | Cotas-partes estaduais | I-C; nomes "Cota-Parte do ICMS/IPVA" em 1.7 | 2016–2025 | Brutos |
| `sus` | Transferências do SUS (União e Estado) | I-C; nomes com "Sistema Único de Saúde"/"SUS" em 1.7 | 2016–2025 | **Natal 2023–2024**: parte do repasse registrada em outras contas (ver `flag_sus_reclassificado`) |
| `fundeb` | Retorno do FUNDEB + complementação da União | I-C; nomes "Manutenção e Desenvolvimento da Educação Básica"/"FUNDEB" em 1.7 | 2016–2025 | – |
| `fnde` | Transferências do FNDE (salário-educação, PNAE, PNATE) | I-C; nomes em 1.7 | 2016–2025 | – |
| `operacoes_credito`, `transf_capital` | Componentes da receita de capital | I-C; contas 2.1 e 2.4 | 2016–2025 | – |
| `deducao_fundeb` | Dedução da receita para formação do FUNDEB | I-C; coluna "Deduções – FUNDEB", conta 1.0 | 2016–2025 | **Natal 2016–2018 inconsistente** (valor ínfimo, ausente ou negativo) |
| `desp_total` | Despesa empenhada total, exceto intraorçamentária | I-E; linha "Despesas Exceto Intraorçamentárias" | 2016–2025 | Medida oficial de despesa |
| `desp_corrente`, `desp_pessoal`, `desp_juros`, `desp_outras_correntes`, `desp_capital`, `desp_investimentos`, `desp_amortizacao` | Despesa por grupo de natureza | I-D; grupos 3, 3.1, 3.2, 3.3, 4, 4.4, 4.6 menos a modalidade 91 (intra) | 2016–2025 | Natal 2017–2018 declarou o anexo só no nível de grupo ("A definir"); `flag_natureza_agregada` |
| `desp_intra_natureza` | Despesa intraorçamentária (modalidade 91) descontada | I-D; linhas "DI" | 2016–2025 | – |
| `desp_total_natureza` | Soma corrente + capital após descontar intra | I-D | 2016–2025 | Confere com `desp_total` em 14 de 20 casos; diferenças em `checagens.csv` |
| `desp_saude`, `desp_educacao`, `desp_assistencia`, `desp_previdencia`, `desp_administracao`, `desp_urbanismo` | Despesa por função (10, 12, 08, 09, 04, 15) | I-E | 2016–2025 | – |

## Municípios – população, atividade econômica e deflator

| Variável | Definição | Fonte | Cobertura | Tratamento |
|---|---|---|---|---|
| `pop_oficial` | População oficial do IBGE no ano | t6579 (estimativas), t4709 (Censo 2022) | 2016–2025 | 2023 sem estimativa → interpolação linear Censo 2022–estimativa 2024 |
| `pop` | **População compatibilizada** (usada no per capita) | t202 (Censo 2010) + t4709 (Censo 2022) | 2016–2025 | 2016–2021: interpolação geométrica entre os Censos 2010 e 2022, porque as estimativas daquele período (base Censo 2010) superestimaram Natal em ~19%; 2022–2025 = `pop_oficial`. Sensibilidade com `pop_oficial` em `resultados/regressoes.txt` |
| `pib` | PIB municipal a preços correntes (R$) | t5938, var. 37 (mil R$ × 1.000) | 2016–2023 | **2024–2025 não divulgados** → NA (`flag_pib_indisponivel`) |
| `vab_servicos`, `impostos_produto` | VAB de serviços; impostos líquidos de subsídios | t5938, var. 6575 e 543 | 2016–2023 | – |
| `ipca_indice_medio` | Média anual do número-índice do IPCA | t1737, var. 2266 | 2014–2025 | – |
| `fator_real_2025` | Fator de conversão para R$ de 2025 | calculado | 2016–2025 | `IPCA_médio_2025 / IPCA_médio_ano` |

## Municípios – indicadores (razões; invariantes ao deflator)

| Variável | Fórmula |
|---|---|
| `ind_autonomia_rc` | `rec_tributaria / rec_corrente` |
| `ind_dependencia_transf` | `transf_correntes / rec_corrente` |
| `ind_fpm_rc`, `ind_icms_rc` | `fpm / rec_corrente`; `icms_cota / rec_corrente` |
| `ind_transf_incondicionais_rc` | `(fpm + icms_cota + ipva_cota) / rec_corrente` |
| `ind_transf_vinculadas_rc` | `(sus + fundeb + fnde) / rec_corrente` |
| `ind_cobertura_despesa_propria` | `rec_tributaria / desp_total` |
| `ind_pessoal_rc` | `desp_pessoal / rec_corrente` (não é o indicador da LRF, que usa a RCL) |
| `ind_investimento_desp` | `desp_investimentos / desp_total` |
| `ind_resultado_orcamentario_rt` | `(rec_total − desp_total) / rec_total` |
| `ind_rec_tributaria_pib`, `ind_transf_correntes_pib` | razões sobre o PIB municipal (2016–2023) |
| `ind_iss_vab_servicos` | `iss / vab_servicos` (2016–2023) |
| `flag_*` | Sinalizações de qualidade (verdadeiro/falso), descritas no registro de alterações; `flag_qualquer` = qualquer sinalização (usada na robustez P6) |
| `foco` | Verdadeiro para Natal e Teresina; falso para as demais capitais do Nordeste (grupo de comparação) |

## Ucrânia (`base_ucrania.csv`)

| Variável | Definição | Fonte (código) | Cobertura | Unidade |
|---|---|---|---|---|
| `fmi_descentralizacao_receita_pct` | Receita do governo local / receita do governo geral | FMI-FD `RD_PT`, setor S1313X | 2011–2020 | % |
| `fmi_descentralizacao_despesa_pct` | Despesa do governo local / despesa do governo geral | FMI-FD `G2MD_PT` | 2011–2020 | % |
| `fmi_descentralizacao_tributaria_pct` | Receita tributária local / receita tributária do governo geral | FMI-FD `TAXD_S13RSHR_PT` | 2011–2020 | % |
| `fmi_dependencia_transf_receita_propria_pct` | Transferências líquidas recebidas / receita própria local | FMI-FD `TRANSFERDEP2_R_NT_OR_PT` | 2011–2020 | % |
| `fmi_dependencia_transf_despesa_propria_pct` | Transferências líquidas / despesa própria local | FMI-FD `TRANSFERDEP1_R_NT_OS_PT` | 2011–2020 | % |
| `fmi_desequilibrio_vertical_pct` | Desequilíbrio fiscal vertical | FMI-FD `VFI_PT` | 2011–2020 | % |
| `fmi_local_share_*` | Participação do governo local no total do governo geral (imposto de renda, propriedade, educação, saúde, investimento) | FMI-FD | 2011–2020 | % |
| `pib_uah` | PIB a preços correntes | WDI `NY.GDP.MKTP.CN` | 2011–2025 | UAH |
| `crescimento_pib_real_pct` | Crescimento real do PIB | WDI `NY.GDP.MKTP.KD.ZG` | 2011–2025 | % a.a. |
| `cpi_2010_100`, `inflacao_pct` | Índice de preços ao consumidor e inflação | WDI `FP.CPI.TOTL`, `FP.CPI.TOTL.ZG` | 2011–2025 | índice; % a.a. |
| `populacao` | População total | WDI `SP.POP.TOTL` | 2011–2025 | pessoas |
| `cambio_uah_usd` | Taxa de câmbio oficial | WDI `PA.NUS.FCRF` | 2011–2025 | UAH/US$ |
| `gc_receita_exc_doacoes_pib`, `gc_receita_tributaria_pib`, `gc_despesa_pib`, `gc_resultado_pib`, `gc_divida_pib` | Finanças do **governo central** | WDI `GC.*` | até 2023–2024 (dívida até 2020) | % do PIB |
| `gc_doacoes_outras_pct_receita` | Doações e outras receitas / receita | WDI `GC.REV.GOTR.ZS` | 2011–2024 | % |
| `despesa_militar_pib` | Despesa militar | WDI `MS.MIL.XPND.GD.ZS` | 2011–2025 | % do PIB |
| `pib_uah_real_2025`, `pib_per_capita_uah_real_2025` | PIB em UAH de 2025 (deflator: CPI) | calculado | 2011–2025 | UAH de 2025 |
| `periodo` | Pré-reforma (2011–2014); reforma de descentralização (2015–2021); guerra em larga escala (2022–2025) | classificação do autor | – | – |

## Ucrânia – orçamentos locais 2021–2025 (`base_ucrania_local_2021_2025.csv`)

Fonte: Ministério das Finanças da Ucrânia (comunicados anuais e "Довідка щодо виконання доходів загального фонду місцевих бюджетів"). Os valores foram transcritos manualmente para `dados/brutos/ucrania/mof_orcamentos_locais_2021_2025.csv`, porque esses sites não oferecem API e estão inacessíveis ao ambiente de coleta automatizada. Cada linha traz o endereço do documento, o tipo (`reportado` ou `derivado`) e observações. Acesso em 22/10/2026. **Esta série não é emendada à do FMI**: o conceito é o *fundo geral* dos orçamentos locais, e não o setor "governo local" das estatísticas GFS.

| Variável | Definição | Unidade |
|---|---|---|
| `receita_propria_fg` | Receitas do fundo geral dos orçamentos locais, sem transferências | bilhões de UAH correntes |
| `pdfo`, `imposto_unico`, `pagamento_terra`, `imposto_imoveis`, `excise`, `imposto_lucro` | Principais receitas próprias (imposto de renda de pessoas físicas, imposto único, pagamento pela terra, imposto sobre imóveis, imposto especial de consumo, imposto sobre o lucro – parcela local) | bilhões de UAH |
| `outras_receitas` | `receita_propria_fg − soma dos seis componentes` | bilhões de UAH |
| `transferencias` | Transferências do orçamento do Estado aos orçamentos locais (2021: **derivada** = 136,8 / 0,675; 2022: total; 2025: fundo geral) | bilhões de UAH |
| `receita_propria_fg_comparavel_2024` | Receita de 2023 na base comparável com 2024 (sem ПДФО de militares) = 451,0 − 87,6 (derivada) | bilhões de UAH |
| `transf_sobre_receita_propria_pct` | `100 × transferencias / receita_propria_fg` | % |
| `pdfo_sobre_receita_propria_pct`, `tributos_patrimonio_sobre_receita_propria_pct` | Participações na receita própria | % |
| `receita_propria_pib_pct`, `transferencias_pib_pct` | Razões sobre o PIB (WDI `NY.GDP.MKTP.CN`) | % do PIB |
| `*_real_2025` | Valores em UAH de 2025, deflacionados pelo CPI (WDI) | bilhões de UAH de 2025 |
| `quebra_pdfo_militar` | Verdadeiro a partir de 2024: o ПДФО sobre soldos militares deixou de ir para os orçamentos locais (lei de novembro de 2023) | – |
| `transferencias_derivada` | Verdadeiro em 2021 (valor calculado, não publicado diretamente) | – |

**Por que a cobertura da Ucrânia difere da dos municípios:** a base do FMI sobre descentralização termina em 2020, e o Banco Mundial não publica todas as séries fiscais para 2024–2025. Desde 2022 várias estatísticas oficiais ucranianas tiveram a divulgação restringida por causa da lei marcial. Por isso a análise subnacional da Ucrânia usa duas séries não emendadas: a do FMI para 2011–2020 (antes e depois da reforma de 2015) e a do Ministério das Finanças para 2021–2025 (guerra). A macrofiscal cobre 2016–2025, até onde há dado. As séries de 2014 em diante excluem a Crimeia e partes ocupadas de Donetsk e Luhansk.
