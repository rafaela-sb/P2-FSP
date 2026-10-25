"""Gera a lista de referências (ABNT) a partir dos registros do Scopus + referências verificadas no Crossref."""
import pandas as pd, re, json, unicodedata
d = pd.read_csv('/root/p2/artigo/trabalho/refs_scopus_selecionadas.csv')

def fmt_autor(a):
    a = a.strip()
    m = re.match(r"^(.*?)\s+((?:[A-Z][a-z]?\.-?\s?)+)$", a)
    if m:
        sob, ini = m.group(1), m.group(2)
        ini = re.sub(r"\.(?=[A-Z])", ". ", ini).strip()
        return f"{sob.upper()}, {ini}"
    return a.upper()

def cit_nome(a):
    a = a.strip(); m = re.match(r"^(.*?)\s+((?:[A-Z][a-z]?\.-?\s?)+)$", a)
    return (m.group(1) if m else a)

refs = []
for _, r in d.iterrows():
    aus = [x for x in str(r.authors).split(';') if x.strip()]
    if len(aus) > 3:
        au = fmt_autor(aus[0]) + ' et al.'
    else:
        au = '; '.join(fmt_autor(x) for x in aus)
    tit = str(r.title).split(' [')[0].split('; [')[0]
    s = f"{au} {tit}. **{r.source}**"
    if pd.notna(r.vol): s += f", v. {int(r.vol) if str(r.vol).replace('.0','').isdigit() else r.vol}"
    if pd.notna(r.issue): s += f", n. {str(r.issue).replace('.0','')}"
    if pd.notna(r.ps) and pd.notna(r.pe): s += f", p. {str(r.ps).replace('.0','')}-{str(r.pe).replace('.0','')}"
    elif pd.notna(r.art): s += f", art. {r.art}"
    s += f", {int(r.year)}."
    if pd.notna(r.doi): s += f" DOI: {r.doi}."
    n1 = cit_nome(aus[0])
    if len(aus) == 1: c = n1
    elif len(aus) == 2: c = f"{n1}; {cit_nome(aus[1])}"
    else: c = f"{n1} et al."
    refs.append(dict(fonte='scopus', ordem=unicodedata.normalize('NFKD', au).encode('ascii','ignore').decode().upper(), abnt=s, cit=c, ano=int(r.year), primeiro=n1))

manuais = [
 ("BAKER, A. C.; LARCKER, D. F.; WANG, C. C. Y. How much should we trust staggered difference-in-differences estimates? **Journal of Financial Economics**, v. 144, n. 2, p. 370-395, 2022. DOI: 10.1016/j.jfineco.2022.01.004.", "Baker et al.", 2022),
 ("BRADFORD, D. F.; OATES, W. E. The analysis of revenue sharing in a new approach to collective fiscal decisions. **The Quarterly Journal of Economics**, v. 85, n. 3, p. 416-439, 1971. DOI: 10.2307/1885931.", "Bradford; Oates", 1971),
 ("BROLLO, F. et al. The political resource curse. **American Economic Review**, v. 103, n. 5, p. 1759-1796, 2013. DOI: 10.1257/aer.103.5.1759.", "Brollo et al.", 2013),
 ("CALLAWAY, B.; SANT'ANNA, P. H. C. Difference-in-differences with multiple time periods. **Journal of Econometrics**, v. 225, n. 2, p. 200-230, 2021. DOI: 10.1016/j.jeconom.2020.12.001.", "Callaway; Sant'Anna", 2021),
 ("DAHLBY, B.; FEREDE, E. The stimulative effects of intergovernmental grants and the marginal cost of public funds. **International Tax and Public Finance**, v. 23, n. 1, p. 114-139, 2016. DOI: 10.1007/s10797-015-9352-5.", "Dahlby; Ferede", 2016),
 ("DE CHAISEMARTIN, C.; D'HAULTFŒUILLE, X. Two-way fixed effects estimators with heterogeneous treatment effects. **American Economic Review**, v. 110, n. 9, p. 2964-2996, 2020. DOI: 10.1257/aer.20181169.", "De Chaisemartin; D'Haultfœuille", 2020),
 ("DRISCOLL, J. C.; KRAAY, A. C. Consistent covariance matrix estimation with spatially dependent panel data. **Review of Economics and Statistics**, v. 80, n. 4, p. 549-560, 1998. DOI: 10.1162/003465398557825.", "Driscoll; Kraay", 1998),
 ("GOODMAN-BACON, A. Difference-in-differences with variation in treatment timing. **Journal of Econometrics**, v. 225, n. 2, p. 254-277, 2021. DOI: 10.1016/j.jeconom.2021.03.014.", "Goodman-Bacon", 2021),
 ("HINES, J. R.; THALER, R. H. Anomalies: the flypaper effect. **Journal of Economic Perspectives**, v. 9, n. 4, p. 217-226, 1995. DOI: 10.1257/jep.9.4.217.", "Hines; Thaler", 1995),
 ("KNIGHT, B. Endogenous federal grants and crowd-out of state government spending: theory and evidence from the federal highway aid program. **American Economic Review**, v. 92, n. 1, p. 71-92, 2002. DOI: 10.1257/000282802760015612.", "Knight", 2002),
 ("MARTINEZ-VAZQUEZ, J.; LAGO-PEÑAS, S.; SACCHI, A. The impact of fiscal decentralization: a survey. **Journal of Economic Surveys**, v. 31, n. 4, p. 1095-1129, 2017. DOI: 10.1111/joes.12182.", "Martinez-Vazquez et al.", 2017),
 ("OATES, W. E. An essay on fiscal federalism. **Journal of Economic Literature**, v. 37, n. 3, p. 1120-1149, 1999. DOI: 10.1257/jel.37.3.1120.", "Oates", 1999),
 ("OATES, W. E. Toward a second-generation theory of fiscal federalism. **International Tax and Public Finance**, v. 12, n. 4, p. 349-373, 2005. DOI: 10.1007/s10797-005-1619-9.", "Oates", 2005),
 ("SUN, L.; ABRAHAM, S. Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. **Journal of Econometrics**, v. 225, n. 2, p. 175-199, 2021. DOI: 10.1016/j.jeconom.2020.09.006.", "Sun; Abraham", 2021),
]
for s, c, a in manuais:
    refs.append(dict(fonte='crossref', ordem=unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode().upper(), abnt=s, cit=c, ano=a, primeiro=c.split(';')[0].split(' et al')[0]))
R = pd.DataFrame(refs).sort_values(['ordem', 'ano'])
R.to_csv('/root/p2/artigo/trabalho/referencias.csv', index=False)
print(len(R))
for _, r in R.iterrows(): print(f"{r.cit} ({r.ano})")
