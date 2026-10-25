#!/bin/sh
# Gera o PDF e o DOCX do artigo (requer pandoc e xelatex). Executar dentro da pasta artigo/.
python3 trabalho/montar_artigo.py
pandoc artigo_final.md -o 241003384_artigo.pdf --pdf-engine=xelatex --resource-path=.:.. \
  -V geometry:"a4paper,top=3cm,left=3cm,bottom=2cm,right=2cm" -V fontsize=12pt -V mainfont="Liberation Serif" \
  -V lang=pt-BR -V colorlinks=true -V linkcolor=black -V urlcolor=blue -H trabalho/cabecalho.tex
pandoc artigo_final_docx.md -o 241003384_artigo.docx --resource-path=.:..
