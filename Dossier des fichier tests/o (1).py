from pylatex import *
from pylatex.utils import * 

a1 = 3
b1 = 2
c1 = 8
a2 = 2
b2 = -1
c2 = 4

# Créez un document
doc = Document()

doc.packages.append(NoEscape("\\usepackage{amsmath}"))


doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
doc.append(pylatex.Command('selectfont'))

with doc.create(Section("Section de test", numbering = False)):
    doc.append("Niveau 1 :")
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())


#tu ecris entre ces deux éléments
    doc.append("Étape 1 : Multiplier la deuxième équation par 2 pour obtenir un coefficient opposé de y :")

    doc.append(NoEscape("\\begin{align*}"))

    




    doc.append(NoEscape("\\end{align*}"))


# Générez le fichier PDF
doc.generate_pdf(clean_tex=False, compiler='pdflatex')