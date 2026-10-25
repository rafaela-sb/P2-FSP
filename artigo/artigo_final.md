---
title: "**Autonomia tributária sob dependência de transferências: Natal e Teresina entre as capitais do Nordeste e o contraponto da descentralização ucraniana (2016–2025)**"
author: "Rafaela de Sousa Barbosa^[Graduanda da Universidade de Brasília (UnB). Matrícula 241003384. Trabalho apresentado à disciplina Finanças do Setor Público (CCA0169), ministrada pelo Prof. Lucas Oliveira Gomes Ferreira, 2026/2. Dados e códigos disponíveis em: https://github.com/rafaela-sb/P2-FSP.]"
date: ""
lang: pt-BR
---

**RESUMO**

Este artigo examina se as transferências intergovernamentais elevam a despesa municipal mais do que a renda local (efeito *flypaper*) e se reduzem o esforço de arrecadação própria em Natal/RN e Teresina/PI, no contexto das nove capitais do Nordeste entre 2016 e 2025, e contrapõe essa evidência à reforma de descentralização fiscal da Ucrânia. A base do trabalho anterior foi conferida, corrigida e reconstruída com dados do Siconfi, do IBGE, do Fundo Monetário Internacional, do Banco Mundial e do Ministério das Finanças da Ucrânia, em reais de 2025. Um estudo bibliométrico com o *bibliometrix* sobre 1.444 artigos do Scopus situa a contribuição na literatura. Teresina tem a menor autonomia tributária entre as capitais nordestinas (18,5% da receita corrente) e Natal ocupa posição intermediária (30,4%). Com efeitos fixos de município, cada R\$ 1,00 per capita de transferência associa-se a R\$ 1,28 de despesa, enquanto o PIB per capita não tem efeito, padrão compatível com o efeito *flypaper*; a associação desaparece quando se controlam choques comuns de ano e, portanto, não permite inferência causal. Não há sinal de substituição do esforço fiscal. Na Ucrânia, a reforma de 2015 reduziu a razão transferências/receita própria local de 143,9% para 48,6% até 2020, e a razão permaneceu entre 34% e 58% durante a guerra. Conclui-se que o desenho das receitas próprias e partilhadas importa mais do que o volume de transferências.

**Palavras-chave:** autonomia fiscal municipal; transferências intergovernamentais; efeito *flypaper*; ilusão fiscal; descentralização fiscal; Ucrânia.

**TAX AUTONOMY UNDER TRANSFER DEPENDENCE: NATAL AND TERESINA AMONG THE NORTHEASTERN STATE CAPITALS AND THE UKRAINIAN DECENTRALIZATION COUNTERPOINT (2016–2025)**

**ABSTRACT**

This paper examines whether intergovernmental transfers raise municipal spending more than local income does (the flypaper effect) and whether they crowd out own-source revenue in Natal and Teresina, Brazil, within the panel of the nine Northeastern state capitals (2016–2025), and contrasts this evidence with Ukraine's fiscal decentralization reform. A bibliometric study of 1,444 Scopus articles frames the contribution. Municipality fixed-effects regressions associate each additional BRL of per capita transfers with BRL 1.28 of spending, while GDP per capita has no effect; the association vanishes once common year shocks are controlled for, so it cannot be read as causal. There is no evidence that transfers displace own-source revenue. Ukraine's 2015 reform raised the local share of general government revenue and reduced transfer dependence, which remained moderate during the war.

**Keywords:** local fiscal autonomy; intergovernmental transfers; flypaper effect; fiscal illusion; fiscal decentralization; Ukraine.

# 1 INTRODUÇÃO

O federalismo fiscal brasileiro concentra a arrecadação nos níveis superiores de governo e transfere aos municípios uma parcela expressiva dos recursos que eles executam. Nas capitais do Nordeste, as transferências correntes — Fundo de Participação dos Municípios (FPM), cotas-partes do ICMS e do IPVA, FUNDEB e repasses do SUS — financiam entre metade e dois terços da receita corrente. A teoria clássica do federalismo fiscal prevê que uma transferência incondicional deveria ter sobre o gasto local o mesmo efeito de um aumento equivalente da renda dos residentes (Bradford; Oates, 1971; Oates, 1999). A evidência empírica acumulada desde os anos 1970, contudo, mostra que o dinheiro "fica onde cai": as transferências elevam o gasto muito mais do que a renda privada. Essa anomalia recebeu o nome de efeito *flypaper* (Hines; Thaler, 1995) e tornou-se uma das manifestações mais estudadas da ilusão fiscal (Turnbull, 1992; Heyndels; Smolders, 1994).

O problema de pesquisa deste artigo situa-se nesse ponto. Natal/RN e Teresina/PI são capitais de porte semelhante (cerca de 785 mil e 906 mil habitantes em 2025) e com estruturas de receita distintas. Teresina depende mais do FPM e dos repasses estaduais; Natal tem base de serviços e turismo que sustenta maior arrecadação de ISS e IPTU. A pergunta de pesquisa é: **as transferências intergovernamentais estão associadas a um aumento da despesa municipal superior ao produzido pela renda local e a uma redução do esforço de arrecadação própria em Natal e Teresina entre 2016 e 2025, e o que a experiência de descentralização fiscal da Ucrânia sugere sobre esse dilema?**

O objetivo geral é analisar a relação entre transferências, receita própria e despesa nos dois municípios atribuídos, usando as demais capitais nordestinas como grupo de comparação. Os objetivos específicos são: (i) atualizar, corrigir e ampliar a base de dados do trabalho anterior; (ii) mapear a literatura internacional por meio de estudo bibliométrico; (iii) descrever a evolução real per capita das receitas e despesas; (iv) estimar modelos de regressão que testem as hipóteses de *flypaper* e de substituição do esforço fiscal; e (v) comparar a trajetória municipal brasileira com os indicadores de descentralização da Ucrânia.

A justificativa é dupla. Do ponto de vista substantivo, a dependência de transferências afeta a responsabilização dos governantes, a eficiência do gasto e a vulnerabilidade a choques (Rodden, 2002; Weingast, 2009). Do ponto de vista metodológico, a literatura recente mostra que estimativas com efeitos fixos bidirecionais podem ser enganosas quando o tratamento varia no tempo e os efeitos são heterogêneos (Baker; Larcker; Wang, 2022; Goodman-Bacon, 2021). Isso exige cautela na interpretação de qualquer associação entre transferências e gasto.

A análise da Ucrânia relaciona-se à dos municípios por contraste institucional. O Brasil é uma federação com municípios constitucionalmente autônomos, mas financeiramente dependentes. A Ucrânia é um Estado unitário que, a partir de 2015, promoveu uma descentralização fiscal baseada na fusão voluntária de municípios (*hromadas*) e na atribuição de parcela do imposto de renda de pessoas físicas aos orçamentos locais (Wright; Slukhai, 2021). Entre 2022 e 2025, essas finanças locais foram submetidas a um choque extremo: a guerra em larga escala. A comparação permite discutir se a forma de financiamento — transferência ou receita partilhada — altera a dependência dos governos locais. Ela não é uma comparação de magnitudes, porque moeda, escala, nível de governo e organização fiscal diferem.

A contribuição do artigo é tríplice: (a) uma base reprodutível, documentada e corrigida para as nove capitais do Nordeste; (b) uma leitura das estimativas de *flypaper* que separa a variação própria de cada município dos choques comuns; e (c) uma ponte comparativa com um caso de descentralização recente e pouco explorado na literatura brasileira.

# 2 REFERENCIAL TEÓRICO

## 2.1 Estudo bibliométrico

Para delimitar o campo, realizou-se busca no Scopus, acessado pelo Portal de Periódicos da CAPES em 22/10/2026, com a seguinte estratégia: `TITLE-ABS-KEY("flypaper effect" OR "fiscal illusion" OR "intergovernmental transfer*" OR "intergovernmental grant*" OR "fiscal decentrali*" OR "fiscal equali*") AND TITLE-ABS-KEY(municipal* OR "local government*" OR subnational OR "local public financ*") AND DOCTYPE(ar)`. A busca retornou 1.444 artigos (1964–2026), publicados em 571 periódicos, por 2.593 autores, com 55.261 referências citadas e média de 21,2 citações por documento. A base foi analisada com o pacote *bibliometrix* em R (rotina em `bibliometria/bibliometria.R`).

Seguindo a estratégia de Baker, Larcker e Wang (2022, Tabela 1), que contaram, por periódico, os artigos de finanças e contabilidade que usam diferenças em diferenças e a parcela que usa o desenho escalonado, a Tabela 1 conta, nos dez periódicos com mais artigos sobre transferências e descentralização entre 2000 e 2025, quantos tratam explicitamente de efeito *flypaper* ou ilusão fiscal.

: Tabela 1 – Artigos sobre transferências intergovernamentais e descentralização fiscal local, por periódico (Scopus, 2000–2025)

| Periódico | (1) Transferências e descentralização | (2) *Flypaper* ou ilusão fiscal | (3) = (2)/(1) |
|:--|--:|--:|--:|
| Lex Localis | 27 | 4 | 14,8% |
| Public Finance Review | 26 | 5 | 19,2% |
| Sustainability | 25 | 0 | 0,0% |
| International Tax and Public Finance | 23 | 5 | 21,7% |
| World Development | 22 | 0 | 0,0% |
| Local Government Studies | 21 | 8 | 38,1% |
| Public Choice | 20 | 3 | 15,0% |
| Environmental Science and Pollution Research | 19 | 0 | 0,0% |
| Journal of Public Economics | 19 | 2 | 10,5% |
| Regional Studies | 16 | 0 | 0,0% |
| **Subtotal (10 periódicos)** | **218** | **27** | **12,4%** |
| **Todos os periódicos** | **1.247** | **94** | **7,5%** |

\noindent\footnotesize Fonte: elaboração própria com *bibliometrix* a partir do Scopus. Nota: a coluna (2) identifica os termos "flypaper" ou "fiscal illusion" no título, resumo ou palavras-chave.\normalsize

Três padrões emergem. Primeiro, a produção cresce a uma taxa de 8,0% ao ano: eram 41 artigos em 2015 e 127 em 2025 (Figura 1). Segundo, o crescimento foi puxado pela agenda de descentralização e crescimento econômico — fortemente concentrada na China (298 artigos, contra 148 dos Estados Unidos e 29 do Brasil) e, mais recentemente, em temas ambientais —, enquanto a parcela de estudos dedicados ao efeito *flypaper* e à ilusão fiscal caiu de 30,8% dos artigos até 1999 para 5,4% em 2020–2026. Terceiro, o efeito *flypaper* permanece concentrado em periódicos de finanças públicas (*Local Government Studies*, *International Tax and Public Finance*, *Public Finance Review*, *Public Choice*), o que sugere uma agenda madura, mas não esgotada. No mapa temático (Figura 2), o agrupamento "transferências intergovernamentais / federalismo fiscal / *flypaper*" aparece com alta centralidade e densidade: é um tema estruturante do campo. As palavras-chave mais frequentes são *fiscal decentralization* (461 artigos), *intergovernmental transfers* (113) e *flypaper effect* (38). Pela lei de Bradford, 31 periódicos formam o núcleo da produção. A produção brasileira cresceu (de 1 artigo até 1999 para 35 em 2020–2026) e dialoga sobretudo com a economia política das transferências.

\begin{figure}[H]\centering
\caption*{Figura 1 – Produção científica anual sobre transferências intergovernamentais e finanças locais (Scopus)}
\includegraphics[width=0.92\linewidth]{../bibliometria/figuras/producao_anual.png}
\caption*{\footnotesize Fonte: elaboração própria com \textit{bibliometrix}.}
\end{figure}
\begin{figure}[H]\centering
\caption*{Figura 2 – Mapa temático das palavras-chave dos autores (centralidade × densidade)}
\includegraphics[width=0.72\linewidth]{../bibliometria/figuras/mapa_tematico.png}
\caption*{\footnotesize Fonte: elaboração própria com \textit{bibliometrix}.}
\end{figure}
O estudo bibliométrico orientou a seleção das referências discutidas a seguir: os artigos mais citados da base, os que tratam diretamente de *flypaper* e ilusão fiscal, os estudos brasileiros e os poucos que analisam a descentralização ucraniana.

## 2.2 Federalismo fiscal e transferências

A teoria de primeira geração do federalismo fiscal atribui aos governos locais a provisão de bens públicos cujos benefícios são locais e aos níveis superiores as funções de estabilização e redistribuição (Oates, 1999). Nesse arcabouço, as transferências corrigem desequilíbrios verticais e externalidades, e uma transferência incondicional equivale, para o eleitor mediano, a um aumento de renda — o "teorema da equivalência" de Bradford e Oates (1971). A teoria de segunda geração desloca o foco para os incentivos dos governantes: a forma como receitas e transferências são desenhadas molda o esforço de arrecadação e a prosperidade local (Oates, 2005; Weingast, 2009). Jin, Qian e Weingast (2005) mostram, para as províncias chinesas, que taxas marginais de retenção de receita mais altas associam-se a maior desenvolvimento do setor privado. Qian e Roland (1998) argumentam que a descentralização pode endurecer a restrição orçamentária ao aumentar o custo de oportunidade de socorros financeiros.

O lado sombrio da dependência aparece em Rodden (2002). Com dados de vários países, o autor mostra que déficits persistentes surgem quando os governos subnacionais dependem de transferências e, ao mesmo tempo, podem tomar crédito: o governo central não consegue se comprometer de forma crível a não socorrê-los. Inman (2001) identifica as instituições necessárias para impor disciplina fiscal local. As evidências sobre os efeitos agregados da descentralização são heterogêneas. Zhang e Zou (1998) encontram associação negativa entre descentralização do gasto e crescimento na China. Rodríguez-Pose e Ezcurra (2010) mostram que, em países de renda baixa e média, a descentralização fiscal acompanha o aumento das disparidades regionais. Arzaghi e Henderson (2005) explicam por que os países descentralizam. Martinez-Vazquez, Lago-Peñas e Sacchi (2017) sintetizam essa literatura e concluem que os efeitos dependem do desenho institucional. Bahl e Bird (2008) defendem que os governos subnacionais em países em desenvolvimento precisam de bases tributárias próprias efetivas e, ao mesmo tempo, de um sistema de transferências equalizadoras. Essa tensão está no centro deste estudo.

## 2.3 O efeito *flypaper* e suas explicações

A expressão "efeito *flypaper*" designa a constatação empírica de que transferências incondicionais em montante fixo estimulam o gasto local muito mais do que aumentos equivalentes da renda privada (Hines; Thaler, 1995). As explicações dividem-se em três famílias.

A primeira é a **ilusão fiscal**. Eleitores percebem mal o preço dos serviços públicos financiados por transferências e por isso demandam mais gasto. Turnbull (1992) mostra que o mesmo resultado pode surgir com eleitores racionais que decidem sob incerteza, e Turnbull (1998) amplia o conceito de ilusão fiscal para incluir a informação imperfeita sobre custos e serviços. Mitias e Turnbull (2001) mostram que ilusão de transferência e ilusão de tributo são interdependentes e encontram evidência de ilusão de transferência no gasto de condados americanos. Heyndels e Smolders (1994) testam simultaneamente quatro fontes de ilusão fiscal nos municípios flamengos e encontram efeitos relevantes. Dollery e Worthington (1999) encontram suporte para as hipóteses de complexidade da receita e ilusão da dívida na Austrália. Grossman (1990) mostra que transferências federais estimulam o gasto local mais do que transferências estaduais, como prevê a hipótese de que a ilusão cresce com a distância entre quem tributa e quem gasta. A ilusão também aparece na administração financeira local: Ross e Mughan (2018) mostram que reavaliações do imposto predial que reduzem a visibilidade do tributo elevam a arrecadação.

A segunda família é a **economia política e burocrática**. Wyckoff (1988) aplica um modelo burocrático à Niskanen e encontra evidência para gastos de capital. Dougan e Kenyon (1988) explicam o *flypaper* por meio da pressão de grupos de interesse, sem recorrer à ilusão do eleitor. Bae e Feiock (2004) mostram que arranjos institucionais locais moderam o efeito. Strumpf (1998) propõe um índice de despesa administrativa como medida do controle do eleitor sobre o orçamento. Bracco et al. (2015) mostram que transferências podem ser usadas como sinal de competência em favor de prefeitos alinhados ao governo central e estimam o *flypaper* com esse alinhamento como instrumento.

A terceira família é a **explicação racional pelo custo marginal dos fundos públicos**. Hamilton (1986) mostra que o *flypaper* é compatível com a maximização de utilidade quando o peso morto da tributação cresce na margem. Dahlby (2011) formaliza que a transferência tem um "efeito preço": ao permitir reduzir a alíquota, diminui o custo marginal dos fundos e torna a provisão pública relativamente mais barata. Dahlby e Ferede (2016) confirmam empiricamente essa previsão para as províncias canadenses. Aragon (2013) mostra que, no Peru, o efeito estimulador das transferências é maior onde a arrecadação local é mais custosa. Hamilton (1983) oferece outra explicação: a renda dos residentes é insumo da produção de serviços públicos e, portanto, substitui parte do gasto. A tese que serve de referência a este trabalho testa a hipótese de Dahlby para os municípios brasileiros e constrói um índice de *flypaper* para estados e municípios.

Há, por fim, uma vertente cética. Becker (1996) sustenta que o *flypaper* pode ser artefato de forma funcional inadequada. Wyckoff (1991) testa quatro explicações sem confirmar nenhuma. Worthington e Dollery (1999) não encontram o efeito no arranjo institucional australiano depois de tratar a endogeneidade das transferências, e Amusa, Mabunda e Mabugu (2008) também não o encontram nos municípios sul-africanos. Yu, Wang e Tian (2016) encontram um efeito "anti-*flypaper*" nos condados chineses quando controlam a dependência espacial.

## 2.4 Identificação, assimetrias e heterogeneidade

A principal crítica metodológica é a endogeneidade: as transferências são definidas com base em características dos próprios receptores (Knight, 2002). Os estudos mais recentes recorrem a regras de alocação. Gordon (2004) usa as mudanças de financiamento do Title I após a divulgação dos censos e encontra substituição substancial do esforço local em três anos. Dahlberg et al. (2008) exploram uma descontinuidade do sistema sueco e encontram *crowding-in* (as transferências viram gasto, não redução de impostos). Lundqvist (2015) usa diferenças em diferenças na Finlândia e encontra efeito imediato e persistente sobre o gasto. Baskaran (2016) usa descontinuidades da fórmula de equalização do estado alemão de Hesse e encontra aumento de despesa sem redução de tributos. Allers e Vermeulen (2016) mostram que, na Holanda, as transferências são capitalizadas nos preços dos imóveis, o que torna improvável a explicação burocrática. Helm e Stuhler (2024) exploram revisões censitárias da população na Alemanha e mostram que o *flypaper* pode ser fenômeno de curto prazo: no longo prazo, a resposta torna-se simétrica e mais próxima da teoria. Gennari e Messina (2014) encontram efeito expressivo nos municípios italianos, com papel relevante de variáveis políticas.

A literatura também documenta assimetrias. Heyndels (2001) encontra, nos municípios flamengos, um padrão de "substituição fiscal": o gasto acompanha as altas das transferências, mas, nas quedas, o município compensa com mais impostos. Deller e Maher (2006) encontram o mesmo padrão em Wisconsin, e Mehiriz e Marceau (2014) encontram efeitos assimétricos que variam por tipo de transferência em Quebec. Levaggi e Zanola (2003) identificam um "super *flypaper*" na saúde regional italiana sob restrição orçamentária fraca. Kjaergaard (2015) mostra assimetria na Dinamarca independentemente das instituições orçamentárias. Sobel e Crowley (2014) acrescentam que transferências temporárias criam "catracas" tributárias futuras. Masiero e Santarossa (2020) mostram respostas heterogêneas após terremotos na Itália.

A heterogeneidade também é espacial e institucional. Acosta (2010) mostra que ignorar a interdependência espacial superestima o efeito nos municípios da província de Buenos Aires. Kakamu, Yunoue e Kuramoto (2014) estimam efeitos por função de gasto no Japão. Rios, Hortas-Rico e Pascual (2022) mostram, para a Espanha, que municípios com maior eficiência arrecadatória e governos politicamente mais fortes têm *flypaper* menor. Saens, Cox e Villalobos (2026) mostram que, no Chile, a elasticidade do gasto às transferências cai de 0,92 nos municípios de menor capacidade fiscal para zero nos de maior capacidade. Cárdenas e Sharma (2011), para o México, e Yüksel (2021), para a Turquia, confirmam o efeito em países em desenvolvimento. Panao (2021) mostra que, nas Filipinas, as transferências incondicionais reduzem a geração de receita local e criam dependência. Baekgaard e Kjaergaard (2016), com um experimento com políticos dinamarqueses, mostram que a ideologia pesa mais do que a origem do dinheiro.

Do ponto de vista econométrico, a crítica de Baker, Larcker e Wang (2022) é diretamente pertinente. Regressões com efeitos fixos de unidade e de tempo (TWFE) produzem médias ponderadas de muitas comparações 2×2, algumas das quais usam unidades já tratadas como controle. Por isso, podem gerar estimativas com sinal oposto ao verdadeiro quando os efeitos variam no tempo (Goodman-Bacon, 2021; De Chaisemartin; D'Haultfœuille, 2020). Callaway e Sant'Anna (2021) e Sun e Abraham (2021) propõem estimadores alternativos. Embora este estudo não estime um desenho de diferenças em diferenças, a mesma lógica de "comparações ruins" vale para a interpretação de painéis curtos com efeitos fixos de ano.

## 2.5 Evidências para o Brasil

No Brasil, a tese de referência e o artigo de Ferreira, Serrano e Revelli (2019) encontram efeito *flypaper* em 476 municípios, intensificado pelo alinhamento político e maior nos municípios com baixa autonomia tributária. Mattos, Rocha e Arvate (2011) reinterpretam o efeito como perda de eficiência arrecadatória induzida pelas transferências. Araujo e Siqueira (2016) encontram evidências de ilusão fiscal na demanda por gasto local. Cruz e Silva (2020) encontram *flypaper* para as transferências redistributivas da educação, e Mattos, Politi e Yamaguchi (2018) mostram que transferências em bloco aumentam a dispersão do gasto educacional. Castro e Mattos (2021) mostram que cerca de 20% do efeito pode ser explicado por transbordamentos das transferências recebidas pelos vizinhos. Alves e Araujo (2024), usando os limiares populacionais do FPM em um desenho de regressão descontínua, encontram aumento do gasto administrativo e de cargos comissionados. Bernardelli et al. (2026) confirmam o *flypaper* no estado de São Paulo e uma associação negativa entre FPM e receita própria. Esse resultado contrasta com o de Litschig e Morrison (2013), que não encontram substituição da receita própria e documentam ganhos educacionais e de redução da pobreza. De Carvalho Filho e Litschig (2020) mostram que esses ganhos persistem no longo prazo.

A economia política da alocação é documentada por Brollo e Nannicini (2012) e Ferreira, Alves e Caldeira (2021): transferências discricionárias favorecem prefeitos aliados e aumentam em anos eleitorais, padrão também observado na Espanha por Solé-Ollé e Sorribas-Navarro (2008). Brollo et al. (2013) mostram ainda uma "maldição política dos recursos": receitas adicionais do FPM, determinadas pelos limiares populacionais, elevam a corrupção e reduzem a qualidade dos candidatos a prefeito. Dos Santos et al. (2025) mostram que obras com mais transferências têm menor probabilidade de paralisação. Sobre descentralização e tamanho do governo, Guedes e Gasparini (2007) concluem que a dependência de transferências anula o efeito disciplinador da descentralização. De Mello Jr. (2002) analisa a relação entre fontes de financiamento e gasto local, e Caldeira, Ehrl e Moreira (2023) mostram que a municipalização da gestão do ITR elevou a arrecadação desse imposto — evidência de que capacidade administrativa importa. Cardoso et al. (2023) documentam que as transferências emergenciais da pandemia ignoraram riscos e geraram "superávits pandêmicos" municipais em 2020.

A ilusão fiscal também se manifesta na estrutura de receitas próprias. Hendrick (2002) e Carroll (2009) discutem se a diversificação de receitas gera ilusão fiscal ou flexibilidade financeira; Carroll não encontra ilusão, mas sim maior volatilidade.

## 2.6 A descentralização ucraniana

A literatura sobre a Ucrânia é escassa no Scopus (20 artigos na base). Wright e Slukhai (2021) descrevem a reforma iniciada em 2015, apoiada em três pilares: fusão voluntária das comunidades territoriais, cooperação intermunicipal e incentivos fiscais. Os autores concluem que a fusão voluntária precisou ser substituída por uma abordagem compulsória e que a partilha de tributos não garantiu sustentabilidade financeira às unidades. Wright, Slukhai e Yakymchuk (2022) não encontram melhora significativa nas finanças das comunidades fundidas. Por outro lado, Zadorozhna e Badunenko (2026) exploram a formação escalonada das *hromadas* entre 2015 e 2020 em um desenho de estudo de evento e encontram melhora de cerca de 20% no desempenho escolar dos alunos abaixo da mediana — justamente o tipo de desenho para o qual se aplicam as cautelas de Baker, Larcker e Wang (2022). Karabin et al. (2021) analisam a reforma à luz da integração europeia; Tolkmitt, Volokhova e Ignatenko (2022) e Krainyk e Fedorchak (2022) discutem fontes de financiamento e o grau de descentralização das receitas; Vysochyna et al. (2022) propõem um índice de resiliência financeira municipal que inclui a razão entre transferências líquidas e receita própria; e Mazur et al. (2026) associam a diversificação da base tributária local à redução do desequilíbrio vertical sob a lei marcial.

## 2.7 Hipóteses

Com base nessa literatura, formulam-se duas hipóteses verificáveis:

- **H1 (*flypaper*):** a despesa municipal per capita responde mais às transferências correntes per capita do que ao PIB per capita (β₁ > β₂).
- **H2 (substituição do esforço fiscal):** as transferências incondicionais (FPM e cotas de ICMS e IPVA) associam-se negativamente à arrecadação tributária própria (δ₁ < 0), como sugerem Panao (2021), Cárdenas e Sharma (2011) e Bernardelli et al. (2026). A hipótese alternativa é a de ausência de substituição, como em Litschig e Morrison (2013) e Dahlberg et al. (2008).

# 3 METODOLOGIA

## 3.1 Delineamento, unidades e período

Trata-se de pesquisa quantitativa, descritiva e explicativa, com dados secundários em painel. As unidades de análise são Natal/RN e Teresina/PI (foco) e as demais sete capitais do Nordeste (São Luís, Fortaleza, João Pessoa, Recife, Maceió, Aracaju e Salvador), usadas como grupo de comparação. As capitais foram escolhidas por homogeneidade regional e porte. O período é 2016–2025, os dez anos mais recentes com Declarações de Contas Anuais (DCA) completas. O PIB municipal está disponível só até 2023, de modo que os modelos que o incluem usam 2016–2023. Para a Ucrânia, usam-se 2011–2020 (descentralização, FMI), 2021–2025 (orçamentos locais, Ministério das Finanças) e 2016–2025 (indicadores macrofiscais, Banco Mundial).

## 3.2 Fontes e critérios de seleção

As finanças municipais vêm do Siconfi/Finbra (Secretaria do Tesouro Nacional), coletadas por API: Anexo I-C (receitas), I-D (despesas por natureza) e I-E (despesas por função). População, PIB e IPCA vêm do IBGE/SIDRA (tabelas 6579, 4709, 202, 5938 e 1737). Os indicadores ucranianos vêm da base *Fiscal Decentralization* do FMI, dos *World Development Indicators* do Banco Mundial e dos relatórios do Ministério das Finanças da Ucrânia. Fontes, endereços e coberturas estão no dicionário de variáveis do repositório.

## 3.3 Variáveis e mensuração

| Variável | Definição e fonte |
|:--|:--|
| Despesa total (D) | Despesa empenhada exceto intraorçamentária (DCA, Anexo I-E) |
| Transferências correntes (T) | Conta 1.7 da receita (DCA, Anexo I-C), valor bruto |
| Transferências incondicionais (TI) | FPM + cota-parte do ICMS + cota-parte do IPVA |
| Transferências vinculadas (TV) | T − TI (SUS, FUNDEB, FNDE e outras) |
| Receita tributária própria (R) | Impostos, taxas e contribuições de melhoria (conta 1.1) |
| Renda local (Y) | PIB municipal a preços correntes (IBGE) |
| Autonomia | R / receita corrente |
| Dependência | T / receita corrente |

: Tabela 2 – Variáveis principais

\noindent\footnotesize Fonte: elaboração própria. Todas as variáveis monetárias estão em reais de 2025 per capita (R\$ mil nos modelos).\normalsize

## 3.4 Tratamentos

Os valores foram deflacionados pela média anual do IPCA, com ano-base 2025. A população de 2016 a 2021 foi compatibilizada por interpolação geométrica entre os Censos de 2010 e 2022, porque as estimativas oficiais daquele período, ancoradas no Censo de 2010, superestimaram a população de várias capitais (no caso de Natal, em cerca de 19%). Como sensibilidade, todos os modelos foram reestimados com a série oficial. Contas cujos códigos mudaram com as revisões do ementário de 2018 e 2022 foram identificadas pelo nome, com uma regra de hierarquia que evita dupla contagem. A despesa intraorçamentária foi excluída. Dados ausentes não foram substituídos por zero. Valores declarados atípicos — reclassificação do SUS em Natal (2023–2024) e em João Pessoa (2018), FUNDEB ausente ou muito baixo em São Luís e João Pessoa, IPTU de Salvador em 2024 — foram mantidos como declarados, sinalizados e excluídos em teste de robustez.

## 3.5 Técnicas de análise

Além de estatísticas descritivas e indicadores, estimaram-se quatro modelos para os dois municípios em foco (MQO agrupado, erros-padrão robustos HC1) e sete especificações em painel para as nove capitais:

$$D_{it} = \alpha + \beta_1 T_{it} + \beta_2 Y_{it} + \gamma\,\text{Natal}_i + \varepsilon_{it} \quad (1)$$

$$D_{it} = \mu_i + \lambda_t + \beta_1 T_{it} + \beta_2 Y_{it} + \varepsilon_{it} \quad (2)$$

$$R_{it} = \mu_i + \lambda_t + \delta_1 TI_{it} + \delta_2 Y_{it} + u_{it} \quad (3)$$

Em (2) e (3), $\mu_i$ são efeitos fixos de município e $\lambda_t$ efeitos fixos de ano. Estimaram-se versões apenas com $\mu_i$ e versões com $\mu_i$ e $\lambda_t$. Sinais esperados: β₁ > 0, β₂ > 0, e β₁ > β₂ sob H1; δ₁ < 0 sob H2. Testou-se H1 por meio do teste de Wald para β₁ = β₂. Também se estimou um modelo log-log com elasticidades. Os erros-padrão do painel são agrupados por município e, por robustez, calculados pelo estimador de Driscoll e Kraay (1998), que acomoda dependência transversal. Os diagnósticos incluem os testes de Breusch-Pagan (heteroscedasticidade), Durbin-Watson (autocorrelação) e Jarque-Bera (normalidade). Para robustez, estimaram-se também versões sem os valores atípicos, sem os anos de pandemia (2020–2021) e com interação para os municípios em foco.

## 3.6 Associação versus causalidade e comparação com a Ucrânia

As estimativas são associações condicionais, não efeitos causais. As transferências não são atribuídas aleatoriamente, e o FPM depende de faixas populacionais e do coeficiente estadual. Como mostram Gordon (2004), Dahlberg et al. (2008) e Helm e Stuhler (2024), a identificação causal exigiria explorar descontinuidades nas regras de alocação. Com nove capitais, nenhuma das quais atravessa limiares do FPM no período, esse desenho não é viável aqui.

A comparação com a Ucrânia é institucional e feita por razões adimensionais (participação local, transferências/receita própria, % do PIB). Ela reconhece diferenças de moeda, escala (a Ucrânia é um país de 38 milhões de habitantes; as capitais têm 0,6 a 2,6 milhões), organização fiscal (Estado unitário × federação), nível de governo (governo local agregado × município individual) e conceito (no Brasil, as cotas de ICMS e IPVA e o FPM são transferências; na Ucrânia, a parcela do imposto de renda é receita própria partilhada).

## 3.7 Limitações

As principais limitações são: (i) painel curto (no máximo 90 observações e 72 com PIB), com apenas nove *clusters*, o que torna frágil a inferência com erros agrupados; (ii) defasagem do PIB municipal; (iii) inconsistências declaratórias na DCA; (iv) quebra de série no ementário da receita; e (v) para a Ucrânia, a interrupção da base do FMI em 2020, a restrição de estatísticas sob lei marcial, a quebra de 2024 (o imposto de renda dos militares deixou de ir para os orçamentos locais) e a exclusão de territórios ocupados.

# 4 RESULTADOS

## 4.1 Estatísticas descritivas

: Tabela 3 – Indicadores reais per capita (R\$ de 2025) e taxas de crescimento, 2016–2025

| Indicador | Natal 2016 | Natal 2025 | Cresc. a.a. | Teresina 2016 | Teresina 2025 | Cresc. a.a. |
|:------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|
| Receita corrente | 3.929 | 5.762 | 4,3% | 4.670 | 6.015 | 2,9% |
| Receita tributária própria | 1.088 | 1.849 | 6,1% | 764 | 1.206 | 5,2% |
| IPTU | 209 | 485 | 9,8% | 119 | 184 | 4,9% |
| ISS | 540 | 819 | 4,7% | 371 | 572 | 4,9% |
| Transferências correntes | 2.359 | 3.319 | 3,9% | 3.207 | 3.899 | 2,2% |
| FPM | 601 | 955 | 5,3% | 965 | 1.436 | 4,5% |
| Cota-parte do ICMS | 606 | 461 | −3,0% | 777 | 601 | −2,8% |
| Despesa total | 4.228 | 5.558 | 3,1% | 4.655 | 5.272 | 1,4% |
| Pessoal e encargos | 1.623 | 2.318 | 4,0% | 2.300 | 2.763 | 2,1% |
| Investimentos | 345 | 305 | −1,4% | 554 | 157 | −13,1% |
| PIB per capita (2016 e 2023) | 43.823 | 44.453 | 0,2% | 35.540 | 36.493 | 0,4% |

\noindent\footnotesize Fonte: elaboração própria com dados do Siconfi e do IBGE.\normalsize

A Tabela 3 mostra que, em termos reais per capita, a receita tributária própria cresceu mais rápido do que as transferências nos dois municípios: 6,1% contra 3,9% ao ano em Natal e 5,2% contra 2,2% em Teresina. O PIB per capita ficou praticamente estagnado. Em Natal, o IPTU mais que dobrou, com salto a partir de 2018. A cota-parte do ICMS caiu em ambos, o que reflete a redução das alíquotas sobre combustíveis, energia e comunicações em 2022. O FPM, ao contrário, cresceu, impulsionado pelas cotas extraordinárias e pela arrecadação federal. A despesa com pessoal avançou mais que a despesa total, enquanto o investimento caiu. Em Teresina, o investimento per capita de 2025 foi menos de um terço do de 2016.

\begin{figure}[H]\centering
\caption*{Figura 3 – Receita própria e transferências correntes per capita, Natal e Teresina, 2016–2025 (R\$ de 2025)}
\includegraphics[width=0.95\linewidth]{../figuras/fig1_receita_propria_transferencias_pc.png}
\caption*{\footnotesize Fonte: elaboração própria com dados do Siconfi, do IBGE e do IPCA.}
\end{figure}
## 4.2 Autonomia, dependência e composição das transferências

A autonomia média de Natal foi de 30,4% da receita corrente, e a de Teresina, de 18,5%. A dependência de transferências correntes foi de 58,8% e 67,9%, respectivamente (Figura 4). Ambas as trajetórias são de leve melhora: a autonomia de Natal passou de 27,7% para 32,1%, e a de Teresina, de 16,3% para 20,0%. A receita própria cobre, em média, 30,8% da despesa de Natal e apenas 19,1% da de Teresina. A composição das transferências (Figura 5) revela que o FPM responde por 20,8% da receita corrente de Teresina, contra 14,8% em Natal, e cresceu fortemente a partir de 2021. Isso sugere que a dependência de Teresina se concentra justamente na transferência incondicional que a literatura associa ao *flypaper* (Ferreira; Serrano; Revelli, 2019).

\begin{figure}[H]\centering
\caption*{Figura 4 – Autonomia (receita tributária/receita corrente) e dependência (transferências/receita corrente), 2016–2025}
\includegraphics[width=0.95\linewidth]{../figuras/fig2_autonomia_dependencia.png}
\caption*{\footnotesize Fonte: elaboração própria.}
\end{figure}
\begin{figure}[H]\centering
\caption*{Figura 5 – Principais transferências per capita (R\$ de 2025)}
\includegraphics[width=0.95\linewidth]{../figuras/fig3_composicao_transferencias.png}
\caption*{\footnotesize Fonte: elaboração própria. Nota: em Natal, parte do repasse do SUS de 2023–2024 foi declarada em outras contas da DCA.}
\end{figure}
## 4.3 Natal e Teresina no contexto das capitais do Nordeste

Entre as nove capitais, Teresina tem a menor autonomia e a maior dependência; Natal ocupa a quarta posição em autonomia, atrás de Salvador (39,7%), Recife (38,5%) e Aracaju (32,2%) (Figura 6). A trajetória comparada (Figura 7) mostra que Natal arrecada acima da mediana das demais capitais em todo o período, com distância crescente a partir de 2018, enquanto Teresina fica sempre abaixo. Em contrapartida, Teresina recebe transferências per capita acima da mediana em todos os anos. Esse quadro está de acordo com Saens, Cox e Villalobos (2026) e Rios, Hortas-Rico e Pascual (2022): a capacidade fiscal é o eixo que diferencia as capitais.

\begin{figure}[H]\centering
\caption*{Figura 6 – Capitais do Nordeste: autonomia e dependência médias, 2016–2025}
\includegraphics[width=0.95\linewidth]{../figuras/fig9_capitais_ne_autonomia.png}
\caption*{\footnotesize Fonte: elaboração própria.}
\end{figure}
\begin{figure}[H]\centering
\caption*{Figura 7 – Natal e Teresina e a mediana das demais capitais do Nordeste (R\$ de 2025)}
\includegraphics[width=0.95\linewidth]{../figuras/fig10_capitais_ne_trajetorias.png}
\caption*{\footnotesize Fonte: elaboração própria.}
\end{figure}
## 4.4 Resultados das regressões

: Tabela 4 – Despesa e receita própria em função das transferências (R\$ mil de 2025 per capita)

| Modelo | Amostra | Transferências | PIB pc | Outros coeficientes | n | R² |
|:--------------------------------|:----------|------------:|----------:|:----------------------|---:|-----:|
| M1 Despesa, MQO | NT 16–23 | 1,536*** (0,195) | 0,057 (0,038) | Natal: 0,339 | 16 | 0,78 |
| M2 Despesa, MQO | NT 16–25 | 0,762 (0,468) | — | Rec. própria: 0,634 | 20 | 0,82 |
| M3 Rec. própria, MQO | NT 16–23 | TI: 0,844** (0,333) | −0,030 (0,024) | Natal: 1,177*** | 16 | 0,81 |
| M4 log despesa, MQO | NT 16–25 | 0,691*** (0,155) | — | Rec. própria: 0,154 | 20 | 0,85 |
| P0 Despesa, EF mun. | NE9 16–23 | 1,283*** (0,224) | −0,001 (0,025) | — | 72 | 0,49ᵂ |
| P0b Rec. própria, EF mun. | NE9 16–23 | TI: 0,663*** (0,071) | −0,029*** (0,008) | — | 72 | 0,45ᵂ |
| P1 Despesa, EF mun. e ano | NE9 16–23 | −0,304 (0,300) | −0,006 (0,012) | — | 72 | — |
| P4 Rec. própria, EF mun. e ano | NE9 16–23 | TI: −0,071 (0,083) | −0,008 (0,007) | — | 72 | — |
| P6 = P1 sem valores atípicos | NE9 16–23 | −0,408 (0,295) | 0,000 (0,015) | — | 63 | — |
| P7 = P1 sem 2020–2021 | NE9 16–23 | −0,338 (0,288) | 0,002 (0,016) | — | 54 | — |

\noindent\footnotesize Fonte: elaboração própria. NT = Natal e Teresina; NE9 = nove capitais do Nordeste; M4 em elasticidades. Erros-padrão entre parênteses: HC1 nos modelos M e agrupados por município nos modelos P. TI = transferências incondicionais. ᵂ R² *within*. \*\*\* p<0,01; \*\* p<0,05. As saídas completas, inclusive Driscoll-Kraay e diagnósticos, estão em `resultados/`.\normalsize

No modelo M1, restrito aos dois municípios, R\$ 1,00 per capita de transferência associa-se a R\$ 1,54 de despesa, contra R\$ 0,06 de PIB per capita. O teste de Wald rejeita a igualdade dos coeficientes (diferença de 1,48; p < 0,001), e os diagnósticos não indicam problemas: Breusch-Pagan com p = 0,45, Durbin-Watson de 2,05 e Jarque-Bera com p = 0,95. O resultado se mantém com a população oficial (1,41; p < 0,001). Quando a receita própria entra no lugar do PIB e se usa a série completa (M2), os dois coeficientes ficam positivos e estatisticamente indistinguíveis (Wald, p = 0,88). No modelo log-log (M4), a elasticidade da despesa às transferências é de 0,69, contra 0,15 para a receita própria.

O painel com as nove capitais confirma o padrão quando se compara cada capital consigo mesma ao longo do tempo (P0): R\$ 1,28 de despesa para cada real transferido, efeito nulo do PIB, Wald p < 0,001 e R² *within* de 0,49. **A associação, porém, desaparece quando se acrescentam efeitos fixos de ano (P1):** o coeficiente fica negativo e não significativo com erros agrupados, inclusive sem valores atípicos (P6) e sem a pandemia (P7). A interação para Natal e Teresina (P5) também não é significativa (0,239; p = 0,35). A leitura é que a relação entre transferências e despesa no período é dominada por movimentos comuns a todas as capitais — expansão do FPM, repasses emergenciais da pandemia e crescimento geral do gasto — e não pela variação específica de cada município. Esse é exatamente o tipo de cautela que Baker, Larcker e Wang (2022) e Goodman-Bacon (2021) recomendam diante de estimativas TWFE. Com nove *clusters* e oito anos, a variação idiossincrática é pequena, e as estimativas com erros de Driscoll-Kraay, ocasionalmente significativas e negativas, devem ser lidas com reserva.

Quanto a H2, não há evidência de substituição do esforço fiscal. A associação entre transferências incondicionais e receita própria é **positiva** nos modelos sem efeitos de ano (0,84 em M3 e 0,66 em P0b) e nula com efeitos de ano (P4). As duas fontes cresceram juntas no período, em linha com Litschig e Morrison (2013) e Dahlberg et al. (2008), e ao contrário de Panao (2021) e Bernardelli et al. (2026). Uma explicação plausível é a atualização das bases imobiliárias e a recuperação do ISS nas capitais — em Natal, o IPTU real per capita mais que dobrou —, que não guardam relação mecânica com o FPM.

Em síntese, H1 é suportada como associação descritiva, mas não como relação causal; H2 é rejeitada. Os resultados convergem com a tese de referência (o *flypaper* aparece com mais força onde a autonomia tributária é baixa, como em Teresina), mas indicam que, em capitais de grande porte e em um período de forte expansão das transferências federais, o efeito estimado é sensível ao controle de choques comuns. Essa sensibilidade dialoga com Becker (1996) e Helm e Stuhler (2024).

## 4.5 Ucrânia: descentralização e guerra

Segundo o FMI, a participação do governo local na receita do governo geral ucraniano passou de 15,6% em 2014 para 19,0% em 2017 e 2019, após a reforma de 2015. A razão entre transferências líquidas e receita própria local caiu de 143,9% em 2015 para 48,6% em 2020, e o desequilíbrio vertical caiu de 56,9% para 33,7% (Figura 8). A queda da participação local na despesa em 2020 (de 33,7% para 24,4%) coincide com a centralização do financiamento da saúde: a participação local na despesa com saúde passou de 69,5% para 28,9%. Ou seja, parte da redução da dependência decorre da transferência de responsabilidades de volta ao centro, e não apenas de maior arrecadação local.

\begin{figure}[H]\centering
\caption*{Figura 8 – Ucrânia: descentralização fiscal e dependência de transferências do governo local, 2011–2020}
\includegraphics[width=0.95\linewidth]{../figuras/fig6_ucrania_descentralizacao.png}
\caption*{\footnotesize Fonte: elaboração própria com dados do FMI (Fiscal Decentralization).}
\end{figure}
Durante a guerra, o governo central passou a gastar 57,9% do PIB em 2022 e 65,6% em 2023, com doações externas respondendo por 40,7% a 47,8% de sua receita e despesa militar entre 25,6% e 39,6% do PIB. Os orçamentos locais seguiram trajetória distinta (Figura 9). A receita própria do fundo geral caiu cerca de 10% em termos reais entre 2021 e 2025 e se estabilizou a partir de 2024. As transferências do Estado caíram mais, e a razão transferências/receita própria passou de 57,6% em 2021 para 38,0% em 2025. O imposto de renda partilhado responde por 57% a 68% da receita própria local. A exclusão do imposto de renda dos militares a partir de 2024 é uma quebra de série que reduz a receita própria comparável. Há, portanto, um limite à autonomia baseada em tributo partilhado: quando o centro precisa de receita, redefine a partilha.

\begin{figure}[H]\centering
\caption*{Figura 9 – Ucrânia: receita própria e transferências dos orçamentos locais, 2021–2025}
\includegraphics[width=0.95\linewidth]{../figuras/fig8_ucrania_orcamentos_locais_2021_2025.png}
\caption*{\footnotesize Fonte: elaboração própria com dados do Ministério das Finanças da Ucrânia e do Banco Mundial.}
\end{figure}
A comparação com as capitais brasileiras é ilustrativa, não de magnitude. Em 2025, as transferências equivaliam a 180% da receita tributária própria em Natal e a 323% em Teresina, contra 38% nos orçamentos locais ucranianos. A diferença decorre em boa medida da classificação: na Ucrânia, a parcela do imposto de renda é tratada como receita própria; no Brasil, as cotas de ICMS e o FPM são transferências. Esse ponto conecta-se diretamente à ilusão fiscal. Uma receita partilhada e visível ao contribuinte local (Turnbull, 1998; Grossman, 1990) tende a gerar maior responsabilização do que uma transferência "invisível" (Bracco et al., 2015). Por outro lado, Wright e Slukhai (2021) e Wright, Slukhai e Yakymchuk (2022) mostram que essa partilha não bastou para dar sustentabilidade às comunidades menores. E a centralização da saúde em 2020 e da arrecadação dos militares em 2024 mostra a fragilidade de uma autonomia que depende de decisões do centro, risco já apontado por Rodden (2002) e Bahl e Bird (2008).

## 4.6 O que mudou em relação ao trabalho anterior

O trabalho anterior trazia apenas planilhas de receita de Teresina (2016–2026), extraídas do portal municipal. Não havia dados de Natal, de despesas, de transferências desagregadas, de população, de PIB ou da Ucrânia. Os valores nominais de Teresina conferem com o Siconfi em todos os anos, com exceção de uma diferença de 0,23% nos impostos de 2021. A coluna deflacionada, porém, continha cinco células com fator incorreto (por exemplo, transferências correntes de 2021 multiplicadas por 0,12 em vez de 1,24) e incluía 2026, ano incompleto. Nesta versão, a base foi reconstruída a partir de fontes oficiais com coleta por API, deflator documentado (IPCA médio, base 2025), população compatibilizada com o Censo de 2022, sete capitais adicionais, despesas por natureza e função, indicadores da Ucrânia e rotinas reprodutíveis. As novas análises — painel, testes de hipótese, robustez e bibliometria — não existiam no trabalho anterior. O registro detalhado está em `documentacao/registro_alteracoes.md`.

## 4.7 Sensibilidade e limitações dos resultados

Os resultados descritivos são robustos à série de população (oficial ou compatibilizada) e à exclusão dos valores atípicos. As conclusões econométricas são sensíveis à inclusão de efeitos fixos de ano. Como se discutiu, essa sensibilidade é o próprio resultado substantivo, e não um defeito a ser escondido. A reclassificação do SUS em Natal afeta a composição das transferências, mas não o total das transferências correntes usado nos modelos. Para a Ucrânia, as séries do FMI (governo local, 2011–2020) e do Ministério das Finanças (fundo geral, 2021–2025) não são emendadas porque medem conceitos diferentes.

# 5 CONCLUSÃO

Este artigo perguntou se as transferências intergovernamentais se associam a um aumento de despesa superior ao da renda local e a uma redução do esforço de arrecadação em Natal e Teresina, e o que a descentralização ucraniana ensina sobre esse dilema. Há três respostas principais. Primeiro, as duas capitais exibem, nas comparações de cada município consigo mesmo, o padrão típico do efeito *flypaper*: cada real de transferência acompanha mais de um real de despesa, enquanto o PIB per capita não tem efeito. Essa associação, porém, não sobrevive ao controle dos choques comuns de ano e, portanto, não pode ser interpretada como efeito causal. Segundo, não houve substituição do esforço fiscal: a arrecadação própria cresceu mais rápido do que as transferências, sobretudo em Natal, e Teresina — a capital menos autônoma do Nordeste — melhorou sua autonomia de 16,3% para 20,0% da receita corrente. Terceiro, a Ucrânia mostra que a redução da dependência pode vir da atribuição de receitas partilhadas aos governos locais, mas também que essa autonomia é revogável pelo centro em momentos de crise.

As contribuições são uma base reprodutível e corrigida para as capitais nordestinas, uma leitura cautelosa das estimativas de *flypaper* à luz da literatura recente sobre efeitos fixos bidirecionais e uma ponte comparativa com a Ucrânia. As implicações para as finanças públicas são: (i) políticas de fortalecimento da arrecadação própria (cadastros imobiliários, ISS) têm espaço mesmo em capitais muito dependentes; (ii) a crescente participação do FPM na receita de Teresina recomenda vigilância sobre o crescimento das despesas obrigatórias, em especial de pessoal, que avançou mais do que a despesa total enquanto o investimento encolhia; e (iii) a classificação e a visibilidade das receitas — transferência ou tributo partilhado — importam para a responsabilização fiscal.

As limitações incluem o painel curto, o número reduzido de unidades, a defasagem do PIB municipal, as inconsistências declaratórias e a descontinuidade das estatísticas ucranianas. Pesquisas futuras podem explorar as descontinuidades populacionais do FPM em amostras amplas de municípios, estimadores robustos à heterogeneidade temporal (Callaway; Sant'Anna, 2021; Sun; Abraham, 2021) para choques como a desoneração do ICMS de 2022 e, para a Ucrânia, a formação escalonada das *hromadas* com dados municipais desagregados.

# REFERÊNCIAS

\setlength{\parindent}{0pt}\setlength{\parskip}{12pt}\singlespacing\raggedright

ACOSTA, P. The "flypaper effect" in presence of spatial interdependence: Evidence from Argentinean municipalities. **Annals of Regional Science**, v. 44, n. 3, p. 453-466, 2010. DOI: 10.1007/s00168-008-0277-0.

ALLERS, M. A.; VERMEULEN, W. Capitalization of equalizing grants and the flypaper effect. **Regional Science and Urban Economics**, v. 58, p. 115-129, 2016. DOI: 10.1016/j.regsciurbeco.2016.03.005.

ALVES, P. J. H. F.; ARAUJO, J. M. The effects of intergovernmental transfers on the local fiscal incentives of Brazilian municipalities. **Journal of Government and Economics**, v. 13, art. 100104, 2024. DOI: 10.1016/j.jge.2024.100104.

AMUSA, H.; MABUNDA, R.; MABUGU, R. Fiscal illusion at the local sphere: An empirical test of the flypaper effect using South African municipal data. **South African Journal of Economics**, v. 76, n. 3, p. 443-465, 2008. DOI: 10.1111/j.1813-6982.2008.00205.x.

ARAGON, F. M. Local spending, transfers, and costly tax collection. **National Tax Journal**, v. 66, n. 2, p. 343-369, 2013. DOI: 10.17310/ntj.2013.2.03.

ARAUJO, J. M.; SIQUEIRA, R. B. Demanda por gastos públicos locais: Evidências dos efeitos de ilusão fiscal no Brasil. **Estudos Economicos**, v. 46, n. 1, p. 189-219, 2016. DOI: 10.1590/0101-416146116jar.

ARIA, M.; CUCCURULLO, C. bibliometrix: an R-tool for comprehensive science mapping analysis. **Journal of Informetrics**, v. 11, n. 4, p. 959-975, 2017. (Software utilizado; não computado entre as referências substantivas.)

ARZAGHI, M.; HENDERSON, J. V. Why countries are fiscally decentralizing. **Journal of Public Economics**, v. 89, n. 7, p. 1157-1189, 2005. DOI: 10.1016/j.jpubeco.2003.10.009.

BAE, S.-S.; FEIOCK, R. C. The flypaper effect revisited: Intergovernmental grants and local governance. **International Journal of Public Administration**, v. 27, n. 8-9, p. 577-596, 2004. DOI: 10.1081/PAD-120030256.

BAEKGAARD, M.; KJAERGAARD, M. Intergovernmental Grants and Public Expenditures: Evidence from a Survey Experiment. **Local Government Studies**, v. 42, n. 2, p. 189-207, 2016. DOI: 10.1080/03003930.2015.1110521.

BAHL, R.; BIRD, R. Subnational taxes in developing countries: The way forward. **Public Budgeting and Finance**, v. 28, n. 4, p. 1-25, 2008. DOI: 10.1111/j.1540-5850.2008.00914.x.

BAKER, A. C.; LARCKER, D. F.; WANG, C. C. Y. How much should we trust staggered difference-in-differences estimates? **Journal of Financial Economics**, v. 144, n. 2, p. 370-395, 2022. DOI: 10.1016/j.jfineco.2022.01.004.

BASKARAN, T. Intergovernmental transfers, local fiscal policy, and the flypaper effect: Evidence from a German state. **FinanzArchiv**, v. 72, n. 1, p. 1-40, 2016. DOI: 10.1628/001522116X14462054864882.

BECKER, E. The illusion of fiscal illusion: Unsticking the flypaper effect. **Public Choice**, v. 86, n. 1-2, p. 85-102, 1996. DOI: 10.1007/BF00114876.

BERNARDELLI, L. V. et al. Intergovernmental transfers and fiscal performance: evidence from Brazil. **Local Government Studies**, 2026. DOI: 10.1080/03003930.2026.2655683.

BRACCO, E. et al. Intergovernmental grants as signals and the alignment effect: Theory and evidence. **Journal of Public Economics**, v. 123, p. 78-91, 2015. DOI: 10.1016/j.jpubeco.2014.11.007.

BRADFORD, D. F.; OATES, W. E. The analysis of revenue sharing in a new approach to collective fiscal decisions. **The Quarterly Journal of Economics**, v. 85, n. 3, p. 416-439, 1971. DOI: 10.2307/1885931.

BRASIL. Secretaria do Tesouro Nacional. **Siconfi – Declaração de Contas Anuais (DCA), Anexos I-C, I-D e I-E**, 2014–2025. Disponível em: https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca. Acesso em: 22 out. 2026.

BROLLO, F. et al. The political resource curse. **American Economic Review**, v. 103, n. 5, p. 1759-1796, 2013. DOI: 10.1257/aer.103.5.1759.

BROLLO, F.; NANNICINI, T. Tying your enemy's hands in close races: The politics of federal transfers in Brazil. **American Political Science Review**, v. 106, n. 4, p. 742-761, 2012. DOI: 10.1017/S0003055412000433.

CALDEIRA, T. C. M.; EHRL, P.; MOREIRA, T. B. S. Fiscal decentralization and tax collection: evidence from the rural property tax in Brazil. **European Journal of Political Economy**, v. 78, art. 102396, 2023. DOI: 10.1016/j.ejpoleco.2023.102396.

CALLAWAY, B.; SANT'ANNA, P. H. C. Difference-in-differences with multiple time periods. **Journal of Econometrics**, v. 225, n. 2, p. 200-230, 2021. DOI: 10.1016/j.jeconom.2020.12.001.

CÁRDENAS, O. J.; SHARMA, A. Mexican Municipalities and the Flypaper Effect. **Public Budgeting and Finance**, v. 31, n. 3, p. 73-93, 2011. DOI: 10.1111/j.1540-5850.2011.00990.x.

CARDOSO, R. L. et al. Lessons from Brazil's unsuccessful fiscal decentralization policy to fight COVID-19. **Public Administration and Development**, v. 43, n. 2, p. 106-119, 2023. DOI: 10.1002/pad.1990.

CARROLL, D. A. Diversifying municipal government revenue structures: Fiscal illusion or instability?. **Public Budgeting and Finance**, v. 29, n. 1, p. 27-48, 2009. DOI: 10.1111/j.1540-5850.2009.00922.x.

CASTRO, M.; MATTOS, E. Measuring Fiscal Spillovers in Brazilian Municipalities. **Public Finance Review**, v. 49, n. 2, p. 221-261, 2021. DOI: 10.1177/1091142121993522.

COSTA, C. S. **P1 – Finanças do Setor Público**: Ucrânia, Natal/RN e Teresina/PI. Brasília: UnB, 2026. Disponível em: https://github.com/snakecs/Prova-Finan-as-setor-p-blico. Acesso em: 22 out. 2026.

CRUZ, T.; SILVA, T. Minimum Spending in Education and the Flypaper Effect. **Economics of Education Review**, v. 77, art. 102012, 2020. DOI: 10.1016/j.econedurev.2020.102012.

DAHLBERG, M. et al. Using a discontinuous grant rule to identify the effect of grants on local taxes and spending. **Journal of Public Economics**, v. 92, n. 12, p. 2320-2335, 2008. DOI: 10.1016/j.jpubeco.2007.05.004.

DAHLBY, B. The marginal cost of public funds and the flypaper effect. **International Tax and Public Finance**, v. 18, n. 3, p. 304-321, 2011. DOI: 10.1007/s10797-010-9160-x.

DAHLBY, B.; FEREDE, E. The stimulative effects of intergovernmental grants and the marginal cost of public funds. **International Tax and Public Finance**, v. 23, n. 1, p. 114-139, 2016. DOI: 10.1007/s10797-015-9352-5.

DE CARVALHO FILHO, I.; LITSCHIG, S. Long-run impacts of intergovernmental transfers. **Journal of Human Resources**, v. 57, n. 3, p. 1-56, 2020. DOI: 10.3368/jhr.57.3.0917-9064R2.

DE CHAISEMARTIN, C.; D'HAULTFŒUILLE, X. Two-way fixed effects estimators with heterogeneous treatment effects. **American Economic Review**, v. 110, n. 9, p. 2964-2996, 2020. DOI: 10.1257/aer.20181169.

DE MELLO JR, L. R. Public finance, government spending and economic growth: The case of local governments in Brazil. **Applied Economics**, v. 34, n. 15, p. 1871-1883, 2002. DOI: 10.1080/00036840210128726.

DELLER, S. C.; MAHER, C. S. A model of asymmetries in the flypaper effect. **Publius: The Journal of Federalism**, v. 36, n. 2, p. 213-229, 2006. DOI: 10.1093/publius/pjj005.

DOLLERY, B.; WORTHINGTON, A. Fiscal illusion at the local level: An empirical test using Australian municipal data. **Economic Record**, v. 75, n. 1, p. 37-48, 1999. DOI: 10.1111/j.1475-4932.1999.tb02432.x.

DOS SANTOS, J. M. A. et al. Fiscal decentralization: the effect of transfers on public works in Brazil. **Empirical Economics**, v. 69, n. 4, p. 1699-1723, 2025. DOI: 10.1007/s00181-025-02805-1.

DOUGAN, W. R.; KENYON, D. A. Pressure groups and public expenditures: the flypaper effect reconsidered. **Economic Inquiry**, v. 26, n. 1, p. 159-170, 1988. DOI: 10.1111/j.1465-7295.1988.tb01676.x.

DRISCOLL, J. C.; KRAAY, A. C. Consistent covariance matrix estimation with spatially dependent panel data. **Review of Economics and Statistics**, v. 80, n. 4, p. 549-560, 1998. DOI: 10.1162/003465398557825.

FERREIRA, J. L. D.; ALVES, A. F.; CALDEIRA, E. Grants for Whom and Why? The Politics of Allocation of Transfers in Brazil. **Developing Economies**, v. 59, n. 1, p. 39-63, 2021. DOI: 10.1111/deve.12265.

FERREIRA, L. O. G. **Constitutional tax transfers in Brazilian municipalities**: the fiscal illusion and the flypaper effect. 2021. Tese (Doutorado em Ciências Contábeis) – Universidade de Brasília, Brasília, 2021.

FERREIRA, L. O. G.; SERRANO, A. L. M.; REVELLI, F. Effects of federal constitutional grants in Brazilian municipalities. **Review of Urban and Regional Development Studies**, v. 31, n. 3, p. 203-233, 2019. DOI: 10.1111/rurd.12103.

GENNARI, E.; MESSINA, G. How sticky are local expenditures in Italy? Assessing the relevance of the flypaper effect through municipal data. **International Tax and Public Finance**, v. 21, n. 2, p. 324-344, 2014. DOI: 10.1007/s10797-013-9269-9.

GOODMAN-BACON, A. Difference-in-differences with variation in treatment timing. **Journal of Econometrics**, v. 225, n. 2, p. 254-277, 2021. DOI: 10.1016/j.jeconom.2021.03.014.

GORDON, N. Do federal grants boost school spending? Evidence from Title I. **Journal of Public Economics**, v. 88, n. 9-10, p. 1771-1792, 2004. DOI: 10.1016/j.jpubeco.2003.09.002.

GROSSMAN, P. J. The impact of federal and state grants on local government spending: A test of the fiscal illusion hypothesis. **Public Finance Review**, v. 18, n. 3, p. 313-327, 1990. DOI: 10.1177/109114219001800304.

GUEDES, K. P.; GASPARINI, C. E. Descentralização fiscal e tamanho do governo no Brasil. **Economia Aplicada**, v. 11, n. 2, p. 303-323, 2007. DOI: 10.1590/S1413-80502007000200007.

HAMILTON, B. W. The flypaper effect and other anomalies. **Journal of Public Economics**, v. 22, n. 3, p. 347-361, 1983. DOI: 10.1016/0047-2727(83)90040-3.

HAMILTON, J. H. The flypaper effect and the deadweight loss from taxation. **Journal of Urban Economics**, v. 19, n. 2, p. 148-155, 1986. DOI: 10.1016/0094-1190(86)90036-7.

HELM, I.; STUHLER, J. The Dynamic Response of Municipal Budgets to Revenue Shocks. **American Economic Journal: Applied Economics**, v. 16, n. 4, p. 484-527, 2024. DOI: 10.1257/app.20220718.

HENDRICK, R. Revenue diversification: Fiscal illusion or flexible financial management. **Public Budgeting and Finance**, v. 22, n. 4, p. 52-72, 2002. DOI: 10.1111/1540-5850.00089.

HEYNDELS, B. Asymmetries in the flypaper effect: Empirical evidence for the Flemish municipalities. **Applied Economics**, v. 33, n. 10, p. 1329-1334, 2001. DOI: 10.1080/00036840010004536.

HEYNDELS, B.; SMOLDERS, C. Fiscal illusion at the local level: Empirical evidence for the Flemish municipalities. **Public Choice**, v. 80, n. 3-4, p. 325-338, 1994. DOI: 10.1007/BF01053224.

HINES, J. R.; THALER, R. H. Anomalies: the flypaper effect. **Journal of Economic Perspectives**, v. 9, n. 4, p. 217-226, 1995. DOI: 10.1257/jep.9.4.217.

IBGE. **Sistema IBGE de Recuperação Automática (SIDRA)**: tabelas 202, 1737, 4709, 5938 e 6579. Disponível em: https://sidra.ibge.gov.br. Acesso em: 22 out. 2026.

INMAN, R. P. Transfers and bailouts: Institutions for enforcing local fiscal discipline. **Constitutional Political Economy**, v. 12, n. 2, p. 141-160, 2001. DOI: 10.1023/A:1016602220782.

INTERNATIONAL MONETARY FUND. **Fiscal Decentralization (FD) dataset**. Disponível em: https://data.imf.org/en/datasets/IMF.STA:FD. Acesso em: 22 out. 2026.

JIN, H.; QIAN, Y.; WEINGAST, B. R. Regional decentralization and fiscal incentives: Federalism, Chinese style. **Journal of Public Economics**, v. 89, n. 9-10, p. 1719-1742, 2005. DOI: 10.1016/j.jpubeco.2004.11.008.

KAKAMU, K.; YUNOUE, H.; KURAMOTO, T. Spatial patterns of flypaper effects for local expenditure by policy objective in Japan: A Bayesian approach. **Economic Modelling**, v. 37, p. 500-506, 2014. DOI: 10.1016/j.econmod.2013.11.028.

KARABIN, T. et al. Local Government Transfer into the Process of Ukraine's European Integration: Achievements of Communities and Losses of the Executive Branch of Power. **Lex Localis**, v. 19, n. 3, p. 781-803, 2021. DOI: 10.4335/19.3.781-803(2021).

KJAERGAARD, M. The Flypaper Effect: Do Political Institutions Affect Danish Local Governments’ Response to Intergovernmental Grants?. **Local Government Studies**, v. 41, n. 4, p. 534-552, 2015. DOI: 10.1080/03003930.2014.968708.

KNIGHT, B. Endogenous federal grants and crowd-out of state government spending: theory and evidence from the federal highway aid program. **American Economic Review**, v. 92, n. 1, p. 71-92, 2002. DOI: 10.1257/000282802760015612.

KRAINYK, O.; FEDORCHAK, O. Financing the development of territorial communities in conditions of decentralization. **Financial and Credit Activity: Problems of Theory and Practice**, v. 2, n. 43, p. 118-125, 2022. DOI: 10.55643/fcaptp.2.43.2022.3558.

LEVAGGI, R.; ZANOLA, R. Flypaper effect and sluggishness: Evidence from regional health expenditure in Italy. **International Tax and Public Finance**, v. 10, n. 5, p. 535-547, 2003. DOI: 10.1023/A:1026118222901.

LITSCHIG, S.; MORRISON, K. M. The impact of intergovernmental transfers on education outcomes and poverty reduction. **American Economic Journal: Applied Economics**, v. 5, n. 4, p. 206-240, 2013. DOI: 10.1257/app.5.4.206.

LUNDQVIST, H. Granting public or private consumption? Effects of grants on local public spending and income taxes. **International Tax and Public Finance**, v. 22, n. 1, p. 41-72, 2015. DOI: 10.1007/s10797-013-9279-7.

MARTINEZ-VAZQUEZ, J.; LAGO-PEÑAS, S.; SACCHI, A. The impact of fiscal decentralization: a survey. **Journal of Economic Surveys**, v. 31, n. 4, p. 1095-1129, 2017. DOI: 10.1111/joes.12182.

MASIERO, G.; SANTAROSSA, M. Earthquakes, grants, and public expenditure: How municipalities respond to natural disasters. **Journal of Regional Science**, v. 60, n. 3, p. 481-516, 2020. DOI: 10.1111/jors.12462.

MATTOS, E.; POLITI, R.; YAMAGUCHI, A. Grants and dispersion of local education spending in Brazil. **Regional Studies**, v. 52, n. 2, p. 239-249, 2018. DOI: 10.1080/00343404.2017.1287891.

MATTOS, E.; ROCHA, F.; ARVATE, P. Flypaper effect revisited: Evidence for tax collection efficiency in Brazilian municipalities. **Estudos Economicos**, v. 41, n. 2, p. 239-267, 2011. DOI: 10.1590/S0101-41612011000200002.

MAZUR, H. et al. Fiscal Decentralization and Local Tax Policy: An Empirical Analysis of Community Self-Sufficiency in Ukraine. **Journal of Applied Economic Sciences**, v. 21, n. 2, p. 529-544, 2026. DOI: 10.57017/jaes.v21.2(92).08.

MEHIRIZ, K.; MARCEAU, R. The Flypaper and Asymmetric Effects of Intergovernmental Grants to Quebec Municipalities. **Public Budgeting and Finance**, v. 34, n. 1, p. 85-102, 2014. DOI: 10.1111/pbaf.12026.

MITIAS, P. M.; TURNBULL, G. K. Grant illusion, tax illusion, and local government spending. **Public Finance Review**, v. 29, n. 5, p. 347-368, 2001. DOI: 10.1177/109114210102900501.

OATES, W. E. An essay on fiscal federalism. **Journal of Economic Literature**, v. 37, n. 3, p. 1120-1149, 1999. DOI: 10.1257/jel.37.3.1120.

OATES, W. E. Toward a second-generation theory of fiscal federalism. **International Tax and Public Finance**, v. 12, n. 4, p. 349-373, 2005. DOI: 10.1007/s10797-005-1619-9.

PANAO, R. A. L. Beyond Flypaper: Unconditional Transfers and Local Revenue Generation in the Philippines, 1992–2016. **International Journal of Public Administration**, v. 44, n. 15, p. 1341-1354, 2021. DOI: 10.1080/01900692.2020.1759628.

QIAN, Y.; ROLAND, G. Federalism and the Soft Budget Constraint. **American Economic Review**, v. 88, n. 5, p. 1143-1162, 1998.

RIOS, V.; HORTAS-RICO, M.; PASCUAL, P. What shapes the flypaper effect? The role of the political environment in the budget process. **Local Government Studies**, v. 48, n. 5, p. 793-820, 2022. DOI: 10.1080/03003930.2020.1866555.

RODDEN, J. The dilemma of fiscal federalism: Grants and fiscal performance around the world. **American Journal of Political Science**, v. 46, n. 3, p. 670-687, 2002. DOI: 10.2307/3088407.

RODRÍGUEZ-POSE, A.; EZCURRA, R. Does decentralization matter for regional disparities? A cross-country analysis. **Journal of Economic Geography**, v. 10, n. 5, p. 619-644, 2010. DOI: 10.1093/jeg/lbp049.

ROSS, J. M.; MUGHAN, S. The Effect of Fiscal Illusion on Public Sector Financial Management: Evidence from Local Government Property Assessment. **Public Finance Review**, v. 46, n. 4, p. 635-664, 2018. DOI: 10.1177/1091142116676360.

SAENS, R.; COX, P.; VILLALOBOS, C. Fiscal capacity and the flypaper effect. **Public Choice**, 2026. DOI: 10.1007/s11127-026-01438-x.

SOBEL, R. S.; CROWLEY, G. R. Do intergovernmental grants create ratchets in state and local taxes?. **Public Choice**, v. 158, n. 1-2, p. 167-187, 2014. DOI: 10.1007/s11127-012-9957-5.

SOLÉ-OLLÉ, A.; SORRIBAS-NAVARRO, P. The effects of partisan alignment on the allocation of intergovernmental transfers. Differences-in-differences estimates for Spain. **Journal of Public Economics**, v. 92, n. 12, p. 2302-2319, 2008. DOI: 10.1016/j.jpubeco.2007.06.014.

STRUMPF, K. S. A predictive index for the flypaper effect. **Journal of Public Economics**, v. 69, n. 3, p. 389-412, 1998. DOI: 10.1016/S0047-2727(98)00008-5.

SUN, L.; ABRAHAM, S. Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. **Journal of Econometrics**, v. 225, n. 2, p. 175-199, 2021. DOI: 10.1016/j.jeconom.2020.09.006.

TOLKMITT, V.; VOLOKHOVA, I.; IGNATENKO, R. Financial decentralization in Ukraine in the context of European trends. **Financial and Credit Activity: Problems of Theory and Practice**, v. 4, n. 45, p. 36-47, 2022. DOI: 10.55643/fcaptp.4.45.2022.3839.

TURNBULL, G. K. Fiscal illusion, uncertainty, and the flypaper effect. **Journal of Public Economics**, v. 48, n. 2, p. 207-223, 1992. DOI: 10.1016/0047-2727(92)90027-D.

TURNBULL, G. K. The Overspending and Flypaper Effects of Fiscal Illusion: Theory and Empirical Evidence. **Journal of Urban Economics**, v. 44, n. 1, p. 1-26, 1998. DOI: 10.1006/juec.1997.2056.

UCRÂNIA. Ministério das Finanças. **Довідка щодо виконання доходів загального фонду місцевих бюджетів** (2022 e 2023) e comunicados sobre a execução dos orçamentos locais (2024 e 2025). Disponível em: https://mof.gov.ua. Acesso em: 22 out. 2026. (Lista completa de documentos em `documentacao/fontes_utilizadas_241003384.docx`.)

VYSOCHYNA, A. et al. Impact of Municipal Financial Resilience on Sustainable Economic Development: Case of Ukraine. **Review of Economics and Finance**, v. 20, p. 662-668, 2022. DOI: 10.55365/1923.X2022.20.77.

WEINGAST, B. R. Second generation fiscal federalism: The implications of fiscal incentives. **Journal of Urban Economics**, v. 65, n. 3, p. 279-293, 2009. DOI: 10.1016/j.jue.2008.12.005.

WORLD BANK. **World Development Indicators**: Ukraine. Disponível em: https://databank.worldbank.org/source/world-development-indicators. Acesso em: 22 out. 2026.

WORTHINGTON, A. C.; DOLLERY, B. E. Fiscal illusion and the Australian local government grants process: How sticky is the flypaper effect?. **Public Choice**, v. 99, n. 1-2, p. 1-13, 1999. DOI: 10.1023/a:1018329802757.

WRIGHT, G.; SLUKHAI, S. Decentralization policy in Ukraine: How voluntary amalgamation, inter-municipal cooperation and fiscal incentives impacted the local government system. **NISPAcee Journal of Public Administration and Policy**, v. 14, n. 1, p. 311-343, 2021. DOI: 10.2478/nispa-2021-0012.

WRIGHT, G.; SLUKHAI, S.; YAKYMCHUK, B. Amalgamation and Local Finance: A Case Study of Ukraine. **Central European Public Administration Review**, v. 20, n. 2, p. 147-168, 2022. DOI: 10.17573/cepar.2022.2.07.

WYCKOFF, P. G. A bureaucratic theory of flypaper effects. **Journal of Urban Economics**, v. 23, n. 1, p. 115-129, 1988. DOI: 10.1016/0094-1190(88)90009-5.

WYCKOFF, P. G. The elusive flypaper effect. **Journal of Urban Economics**, v. 30, n. 3, p. 310-328, 1991. DOI: 10.1016/0094-1190(91)90052-9.

YU, Y.; WANG, J.; TIAN, X. Identifying the Flypaper Effect in the Presence of Spatial Dependence: Evidence from Education in China's Counties. **Growth and Change**, v. 47, n. 1, p. 93-110, 2016. DOI: 10.1111/grow.12113.

YÜKSEL, C. The Flypaper Effect: “Reality” or “Myth”? Evidence from Turkey. **Sosyoekonomi**, v. 29, n. 49, p. 483-500, 2021. DOI: 10.17233/sosyoekonomi.2021.03.24.

ZADOROZHNA, O.; BADUNENKO, O. Local power, global scores: Effects of decentralization reform on Ukraine’s school graduate outcomes. **Economic Modelling**, v. 163, art. 107728, 2026. DOI: 10.1016/j.econmod.2026.107728.

ZHANG, T.; ZOU, H.-F. Fiscal decentralization, public spending, and economic growth in China. **Journal of Public Economics**, v. 67, n. 2, p. 221-240, 1998. DOI: 10.1016/S0047-2727(97)00057-1.
