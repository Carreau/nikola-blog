s =  \
"""- **Active mechanics in living oocytes reveal molecular-scale force kinetics** – Biophysical Journal – 2016 – Ahmed, Wylie; Fodor, Etienne; Almonacid, Maria; Bussonnier, Matthias; Verlhac, Marie-Helene; Gov, Nir; Visco, Paolo; van Wijland, Frederic; Betz, Timo;
- **Nonequilibrium dissipation in living oocytes** – EPL (Europhysics Letters) – 2016 – Fodor, Étienne; Ahmed, Wylie W; Almonacid, Maria; Bussonnier, Matthias; Gov, Nir S; Verlhac, M-H; Betz, Timo; Visco, Paolo; van Wijland, Frédéric;
- **Cell-sized liposome doublets reveal active tension build-up driven by acto-myosin dynamics** – Soft Matter – 2016 – Caorsi, V; Lemière, J; Campillo, C; Bussonnier, M; Manzi, J; Betz, T; Plastino, J; Carvalho, K; Sykes, C;
- **Jupyter Notebooks—a publishing format for reproducible computational workflows** – Positioning and Power in Academic Publishing: Players, Agents and Agendas – 2016 – Kluyver, Thomas; Ragan-Kelley, Benjamin; Pérez, Fernando; Granger, Brian; Bussonnier, Matthias; Frederic, Jonathan; Kelley, Kyle; Hamrick, Jessica; Grout, Jason; Corlay, Sylvain;
- **Quantification of collagen contraction in three-dimensional cell culture** – Methods in cell biology – 2015 – Kopanska, Katarzyna S; Bussonnier, Matthias; Geraldo, Sara; Simon, Anthony; Vignjevic, Danijela; Betz, Timo;
- **Active diffusion positions the nucleus in mouse oocytes** – Nature cell biology – 2015 – Almonacid, Maria; Ahmed, Wylie W; Bussonnier, Matthias; Mailly, Philippe; Betz, Timo; Voituriez, Raphaël; Gov, Nir S; Verlhac, Marie-Hélène;
- **Active mechanics reveal molecular-scale force kinetics in living oocytes** – arXiv preprint arXiv:1510.08299 – 2015 – Ahmed, Wylie W; Fodor, Etienne; Almonacid, Maria; Bussonnier, Matthias; Verlhac, Marie-Helene; Gov, Nir S; Visco, Paolo; van Wijland, Frederic; Betz, Timo;
- **Mechanical detection of a long-range actin network emanating from a biomimetic cortex** – Biophysical journal – 2014 – Bussonnier, Matthias; Carvalho, Kevin; Lemière, Joël; Joanny, Jean-François; Sykes, Cécile; Betz, Timo;
- **Actin gel mechanics** – University Paris VII archives – 2014 – Bussonnier, Matthias;
- **The Jupyter/IPython architecture: a unified view of computational research, from interactive exploration to communication and publication.** – AGU – 2014 – Ragan-Kelley, M.; Perez, F.; Granger, B.; Kluyver, T.; Ivanov, P.; Frederic, J.; Bussonnier, M.;
- **Nuclear positioning powered by F-actin flows in oocytes** – MOLECULAR BIOLOGY OF THE CELL – 2013 – Almonacid, M; Bussonnier, M; Betz, T; Luksza, M; Queguiner, I; Voituriez, R; Gov, N; Verlhac, MH;
- **IPython: components for interactive and parallel computing across disciplines. (Invited)** – AGU – 2013 – Perez, F.; Bussonnier, M.; Frederic, J. D.; Froehle, B. M.; Granger, B. E.; Ivanov, P.; Kluyver, T.; Patterson, E.; Ragan-Kelley, B.; Sailer, Z.;
- **IPython: components for interactive and parallel computing across disciplines** – AGU – 2013 – Perez, F.; Bussonnier, M.; Frederic, J. D.; Froehle, B. M.; Granger, B. E.; Ivanov, P.; Kluyver, T.; Patterson, E.; Ragan-Kelley, B.; Sailer, Z.;
"""



publis = s.splitlines()


def cvify(publis):
    for i,p in reversed(list(enumerate(reversed(publis), start=1))):
        items = p.split(' – ')
        items = [it.replace('#', '\\#') for it in items if '](' not in it] # filter links
        items[0] = items[0].strip('- *')
        items.insert(0, '[%s]'%i )
        while len(items) < 6:
            items.append('')
        print('\\cventry{'+'}{'.join(items)+'}')

with open('pages/me.md')as f:
    data = f.read()
    lines = data.splitlines()

    talk_lines = []
    to_push = []
    push = False
    for l in lines:
        if l.startswith('### Talks'):
            to_push = talk_lines
            continue
        elif l.startswith('#'):
            to_push = []
        to_push.append(l)

    tt = '\n'.join([l for l in talk_lines if l])

talks = tt

"""- **Ending Py2/Py3 compatibility in a user friendly manner** – PyCon – 2017 – M. Bussonnier, M. Pacer, T. Kluyver – [slides](https://carreau.github.io/pycon2017/) – [video](https://www.youtube.com/watch?v=2DkfPzWWC2Q)
- **Documentation and Continuous Integration in Python with Sphinx and Travis CI** – The Hacker Within, Berkeley – 2017 – Nelle Varoquaux, Chris Holdgraf, Matthias Bussonnier
- **Continuous integration, Documentation and Travis CI** – Docathon Conference, Berkeley – 2017 – Matthias Bussonnier - [slides](https://speakerdeck.com/carreau/continuous-integration-documentation-and-travis-ci)
- **Git and GitHub** – The Hacker Within, Berkeley – 2017 – Ciera Martinez and Matthias Bussonnier
- **Keynote: Jupyter : an insider story** – JupyterDay Boston , Invited Keynote, about the history of Jupyter and the challenges of managing a growing open source project
- **Project Jupyter Overview** – PyBay – 2016 – By Jamie Whitacre, and Matthias Bussonnier
- **Xonsh :Put some Python in your shell** PyBay – 2016 – Matthias Bussonnier and the Xonsh Core team – [video](https://www.youtube.com/watch?v=lopI4HkA9rE) [slides](https://speakerdeck.com/carreau/xonsh-pybay-2016)
- **Python Metaprogramming and Conversion to Python 3** – 2016 – The hacker Within, Berkeley – Ryan Pavlovsky wand Matthias Bussonnier
- **Jupyter, from data gathering to publications** – PLoS: Lunch and Learn, talks and Posdcast – 2016 – Matthias Bussonnier
- **Talks Python to me : Episode #44: Project Jupyter and IPython** – Podcast – 2016 - Min RK, Michael Kennedy, Matthias Bussonnier
- **Jupyter: A tool for Open Science** – UC Merced – 2016 – Invited presentation for the UC Merced Applied Math Department
- **Jupyter, State of Real–Time collaboration** – SciPy – 2015– Matthias Bussonnier and Kester Tong - [video](https://www.youtube.com/watch?v=DyGoHAP8B_s)
- **Jupyter: A tool for datascience at scale** – LBL Labtech – 2015 – Presentation about the current and future state of Jupyter at the Lawrence Berkeley National Laboratory LabTech conference.
- **IPython: protocol, kernels and new features** – EuroSciPy – 2014 – By Thomas Kluyver and Matthias Bussonnier
- **Jupyter/IPython notebook, a tool for data science** – NSLS–II workshop at Brookhaven National Lab. – 2013 – Matthias Bussonnier"""

assert tt == talks


conf = """- **Jupyter Tutorial** – PyCon – 2017 – Michael Bright, Matthias Bussonnier
- **Docathon** – Berkeley – 2017 – [website](https://docathon.github.io/docathon/)
- **The Hacker Within** – Berkeley – once a week during academic semester – 2015-2017
- **Python Bootcamp Fall 2016** – Berkeley – 2016
- **Jupyter Advanced Topics Tutorial** – SciPy – 2015 – Matthias Bussonnier, Jonathan Frederic and Thomas Kluyver – [video](https://www.youtube.com/watch?v=38R7jiCspkw)
- **Software Carpentry Worksops** – Multiple Location –  2014-2017
- **IPython Advanced tutorial** – EuroSciPy – 2013 – Min Ragan-Kelley, Matthias Bussonnier
"""


print()
print('\\section{Publications and Proceedings}')
print()

cvify(publis)

print()
print('\\section{Talks}')
print()

cvify(talks.splitlines())


print()
print('\\section{Workshop conference: organizer / lecturer / instructor / helper}')
print()

cvify(conf.splitlines())
