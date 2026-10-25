"""Monta o artigo final a partir de artigo_241003384.md (formatação ABNT).

- Insere as referências dos artigos (referencias.csv) e junta-as aos documentos oficiais
  em uma lista única, em ordem alfabética (NBR 6023).
- Figuras: título "Figura N – ..." acima e "Fonte: ..." abaixo (NBR 14724/IBGE).
- "Fonte:"/"Nota:" de tabelas e figuras em fonte menor, sem recuo.
Gera artigo_final.md (para o PDF, via LaTeX) e artigo_final_docx.md (para o Word).
"""
import re
import unicodedata
import pandas as pd

R = pd.read_csv('trabalho/referencias.csv')
fix = {'AARVATE, P.': 'ARVATE, P.',
 'PRESSURE GROUPS AND PUBLIC EXPENDITURES: THE FLYPAPER EFFECT RECONSIDERED': 'Pressure groups and public expenditures: the flypaper effect reconsidered',
 'EFFECTS OF FEDERAL CONSTITUTIONAL GRANTS IN BRAZILIAN MUNICIPALITIES': 'Effects of federal constitutional grants in Brazilian municipalities',
 'FINANCING THE DEVELOPMENT OF TERRITORIAL COMMUNITIES IN CONDITIONS OF DECENTRALIZATION': 'Financing the development of territorial communities in conditions of decentralization',
 'FINANCIAL DECENTRALIZATION IN UKRAINE IN THE CONTEXT OF EUROPEAN TRENDS': 'Financial decentralization in Ukraine in the context of European trends',
 'Long-run Impacts of Intergovernmental Transfers×': 'Long-run impacts of intergovernmental transfers'}
artigos = []
for s in R.abnt:
    for a, b in fix.items():
        s = s.replace(a, b)
    artigos.append(s.replace('..', '.').replace(';.', '.'))

src = open('artigo_241003384.md').read()
corpo, refs = src.split('# REFERÊNCIAS', 1)
docs_txt = refs.split('## Documentos oficiais, bases de dados e trabalhos de referência', 1)[1]
docs = [p.strip() for p in docs_txt.strip().split('\n\n') if p.strip()]


def chave(s):
    s = s.replace('*', '').upper()
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^A-Z0-9 ,.;]', '', s)


todas = sorted(artigos + docs, key=chave)

FIG = re.compile(r'^!\[(Figura \d+ – .*?)\]\((.*?)\)\{width=(\d+)%\}\s*$', re.M)


def partes(leg):
    titulo, _, fonte = leg.partition(' Fonte: ')
    nota = ''
    if ' Nota: ' in titulo:
        titulo, _, nota = titulo.partition(' Nota: ')
        nota = 'Nota: ' + nota
    return titulo.rstrip('.'), nota, ('Fonte: ' + fonte) if fonte else ''


def md2tex(s):
    return re.sub(r'\*(.+?)\*', r'\\textit{\1}', s)


def fig_tex(m):
    titulo, nota, fonte = partes(m.group(1))
    abaixo = ' '.join(x for x in (fonte, nota) if x)
    w = int(m.group(3)) / 100
    return ('\\begin{figure}[H]\\centering\n'
            f'\\caption*{{{md2tex(titulo)}}}\n'
            f'\\includegraphics[width={w:.2f}\\linewidth]{{{m.group(2)}}}\n'
            f'\\caption*{{\\footnotesize {md2tex(abaixo)}}}\n'
            '\\end{figure}')


def fig_docx(m):
    titulo, nota, fonte = partes(m.group(1))
    abaixo = ' '.join(x for x in (fonte, nota) if x)
    return f'{titulo}\n\n![]({m.group(2)}){{width={m.group(3)}%}}\n\n{abaixo}'


FONTE = re.compile(r'^(Fonte: .*)$', re.M)
pdf = FIG.sub(fig_tex, corpo)
pdf = FONTE.sub(lambda m: '\\noindent\\footnotesize ' + m.group(1) + '\\normalsize', pdf)
open('artigo_final.md', 'w').write(
    pdf + '# REFERÊNCIAS\n\n\\setlength{\\parindent}{0pt}\\setlength{\\parskip}{12pt}\\singlespacing\\raggedright\n\n'
    + '\n\n'.join(todas) + '\n')
docx = FIG.sub(fig_docx, corpo)
open('artigo_final_docx.md', 'w').write(docx + '# REFERÊNCIAS\n\n' + '\n\n'.join(todas) + '\n')
print(len(artigos), 'artigos +', len(docs), 'documentos =', len(todas), 'referências em lista única')
