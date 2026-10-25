# Estudo bibliométrico com o pacote bibliometrix (Aria & Cuccurullo, 2017) – P2 FSP, matrícula 241003384
# ----------------------------------------------------------------------------------------------------
# Base: Scopus, acessado pelo Portal de Periódicos da CAPES (acesso CAFe/UnB) em 22/10/2026.
# String de busca (Advanced search):
#   TITLE-ABS-KEY ( "flypaper effect" OR "fiscal illusion" OR "intergovernmental transfer*" OR
#   "intergovernmental grant*" OR "fiscal decentrali*" OR "fiscal equali*" ) AND
#   TITLE-ABS-KEY ( municipal* OR "local government*" OR subnational OR "local public financ*" )
#   AND DOCTYPE ( ar )
# Resultado: 1.444 artigos (1964–2026). Exportação: CSV, "todas as informações" (inclui referências).
# Arquivo: bibliometria/scopus.csv
#
# Uso: Rscript bibliometria/bibliometria.R   (diretório de trabalho = raiz do repositório)
# Alternativa interativa vista em aula: library(bibliometrix); biblioshiny()  -> importar scopus.csv
# ----------------------------------------------------------------------------------------------------
suppressMessages({
  library(bibliometrix)
  library(dplyr)
  library(ggplot2)
})
dir.create("bibliometria/figuras", showWarnings = FALSE, recursive = TRUE)
dir.create("bibliometria/resultados", showWarnings = FALSE, recursive = TRUE)

# scopus.csv vai compactado no repositório (limite de tamanho do GitHub pela web)
if (!file.exists("bibliometria/scopus.csv")) unzip("bibliometria/scopus.zip", exdir = "bibliometria")
M <- convert2df("bibliometria/scopus.csv", dbsource = "scopus", format = "csv")
cat("Documentos:", nrow(M), "\n")

# 1. Análise descritiva -------------------------------------------------------------------------------
res <- biblioAnalysis(M, sep = ";")
s <- summary(res, k = 20, pause = FALSE, verbose = FALSE)
capture.output(summary(res, k = 20, pause = FALSE), file = "bibliometria/resultados/resumo_bibliometrix.txt")
write.csv(s$MainInformationDF, "bibliometria/resultados/informacoes_principais.csv", row.names = FALSE)
write.csv(s$AnnualProduction, "bibliometria/resultados/producao_anual.csv", row.names = FALSE)
write.csv(s$MostRelSources, "bibliometria/resultados/periodicos_mais_relevantes.csv", row.names = FALSE)
write.csv(s$MostProdAuthors, "bibliometria/resultados/autores_mais_produtivos.csv", row.names = FALSE)
write.csv(s$MostProdCountries, "bibliometria/resultados/paises_mais_produtivos.csv", row.names = FALSE)
write.csv(s$MostCitedPapers, "bibliometria/resultados/artigos_mais_citados_global.csv", row.names = FALSE)
write.csv(s$MostRelKeywords, "bibliometria/resultados/palavras_chave_mais_frequentes.csv", row.names = FALSE)

# 2. Tabela no formato da Tabela 1 de Baker, Larcker e Wang (2022) -------------------------------------
# Baker et al. contam, por periódico, os artigos que usam DiD e os que usam DiD escalonado.
# Aqui: por periódico (10 com mais artigos, 2000–2025), (1) artigos sobre transferências/descentralização
# fiscal local; (2) desses, os que tratam explicitamente de efeito flypaper ou ilusão fiscal; (3) = (2)/(1).
txt <- toupper(paste(M$TI, M$AB, M$DE, M$ID))
M$FLY <- grepl("FLYPAPER|FISCAL ILLUSION", txt)
M$BRA <- grepl("BRAZIL", txt)
P <- M %>% filter(PY >= 2000, PY <= 2025)
top <- P %>% count(SO, sort = TRUE) %>% slice_head(n = 10) %>% pull(SO)
tab <- P %>% filter(SO %in% top) %>% group_by(Periodico = SO) %>%
  summarise(Transferencias_descentralizacao = n(), Flypaper_ilusao_fiscal = sum(FLY), .groups = "drop") %>%
  arrange(desc(Transferencias_descentralizacao))
tot_top <- tibble(Periodico = "Subtotal (10 periódicos)",
                  Transferencias_descentralizacao = sum(tab$Transferencias_descentralizacao),
                  Flypaper_ilusao_fiscal = sum(tab$Flypaper_ilusao_fiscal))
tot_all <- tibble(Periodico = "Todos os periódicos (2000–2025)",
                  Transferencias_descentralizacao = nrow(P), Flypaper_ilusao_fiscal = sum(P$FLY))
tab <- bind_rows(tab, tot_top, tot_all) %>%
  mutate(Percentual = round(100 * Flypaper_ilusao_fiscal / Transferencias_descentralizacao, 1))
write.csv(tab, "bibliometria/resultados/tabela1_estilo_baker.csv", row.names = FALSE)
print(tab)

# Por década (complementa a Tabela 1, como o "394 dos 407 desde 2010" de Baker et al.)
dec <- M %>% mutate(Periodo = cut(PY, c(1960, 1999, 2009, 2019, 2026),
                                  labels = c("até 1999", "2000–2009", "2010–2019", "2020–2026"))) %>%
  group_by(Periodo) %>% summarise(Artigos = n(), Flypaper_ilusao = sum(FLY), Brasil = sum(BRA), .groups = "drop")
write.csv(dec, "bibliometria/resultados/artigos_por_periodo.csv", row.names = FALSE)
print(dec)

# 3. Figuras ------------------------------------------------------------------------------------------
ap <- M %>% count(PY) %>% filter(PY <= 2025)
g <- ggplot(ap, aes(PY, n)) + geom_col(fill = "#2a78d6", width = 0.8) +
  labs(x = "Ano", y = "Artigos") +
  theme_minimal(base_size = 11) + theme(panel.grid.minor = element_blank(), plot.title = element_text(size = 11))
ggsave("bibliometria/figuras/producao_anual.png", g, width = 8, height = 3.6, dpi = 200)

png("bibliometria/figuras/coocorrencia_palavras.png", width = 2000, height = 1600, res = 220)
NetMatrix <- biblioNetwork(M, analysis = "co-occurrences", network = "author_keywords", sep = ";")
net <- networkPlot(NetMatrix, normalize = "association", n = 40, type = "fruchterman",
                   Title = "Co-ocorrência de palavras-chave dos autores", labelsize = 0.7, size.cex = TRUE,
                   remove.multiple = FALSE, verbose = FALSE)
plot(net$graph); dev.off()

mapa <- thematicMap(M, field = "DE", n = 250, minfreq = 5, stemming = FALSE, size = 0.5, n.labels = 3, repel = TRUE)
ggsave("bibliometria/figuras/mapa_tematico.png", mapa$map, width = 8, height = 6.5, dpi = 200)
write.csv(mapa$clusters, "bibliometria/resultados/mapa_tematico_clusters.csv", row.names = FALSE)

# Lei de Bradford (zonas de periódicos) e de Lotka (produtividade de autores)
bd <- bradford(M)
write.csv(bd$table, "bibliometria/resultados/bradford.csv", row.names = FALSE)
lk <- lotka(res)
capture.output(lk, file = "bibliometria/resultados/lotka.txt")

# 4. Citações locais (dentro da base) e lista de documentos para seleção das referências ----------------
lc <- tryCatch(localCitations(M, sep = ";"), error = function(e) NULL)
if (!is.null(lc)) write.csv(lc$Papers, "bibliometria/resultados/citacoes_locais_artigos.csv", row.names = FALSE)
CR <- citations(M, field = "article", sep = ";")
write.csv(head(as.data.frame(CR$Cited), 100), "bibliometria/resultados/referencias_mais_citadas_na_base.csv", row.names = FALSE)
doc <- M[, intersect(c("AU", "TI", "SO", "PY", "VL", "IS", "BP", "EP", "DI", "TC", "DE"), names(M))]
doc$FLY <- M$FLY; doc$BRA <- M$BRA
write.csv(doc, "bibliometria/resultados/base_documentos.csv", row.names = FALSE)
cat("Concluído.\n")
