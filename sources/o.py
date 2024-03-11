from pylatex import *
from pylatex.utils import * 

# Créez un document
doc = Document()

doc.packages.append(NoEscape("\\usepackage{amsmath}"))


doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
doc.append(pylatex.Command('selectfont'))

with doc.create(Section("Section de test", numbering = False)):
    doc.append("Niveau 1 :")

#tu ecris entre ces deux éléments

    doc.append(NoEscape(r"\left\{"))
    doc.append(NoEscape(r"\begin{aligned}"))
    doc.append(NoEscape(r"2x + 3y - z &= 1 \\"))
    doc.append(NoEscape(r"x - y + z &= 0"))
    doc.append(NoEscape(r"\end{aligned}"))
    doc.append(NoEscape(r"\right."))

    # doc.append(NoEscape("\\  \\Leftrightarrow  &= \\\\" % ()))
    # doc.append(Command('vspace', '5mm'))
    # doc.append(NewLine())

    # doc.append(NoEscape("\\  \\Leftrightarrow  &= \\\\" % ()))
    # doc.append(Command('vspace', '5mm'))
    # doc.append(NewLine())

    # doc.append(NoEscape("\\ \\Leftrightarrow   &= \\\\" % ()))
    # doc.append(Command('vspace', '5mm'))
    # doc.append(NewLine())




### pour les accolades


#\documentclass{article}
# \usepackage{amsmath}

# \begin{document}

# \begin{align*}
# \begin{cases}
#       1 & \text{si la banque $i$ émet des ABs au temps $t$}\\
#       2 & \text{si la banque $i$ émet des CBs au temps $t$}\\
#       0 & \text{sinon}
# \end{cases}
# \vspace{5mm}%
# \\
# \begin{cases}
#       1 & \text{si la banque $i$ émet des ABs au temps $t$}\\
#       2 & \text{si la banque $i$ émet des CBs au temps $t$}\\
#       0 & \text{sinon}
# \end{cases} 
# \end{align*}
# \\
# \begin{align*}
# \begin{cases}
#       1 & \text{if bank $i$ issues AyjhtyjytjhtyjtyjtyjtyjtyjBs at time $t$}\\
#       2 & \text{if bank $i$ issues CBs at time $t$}\\
#       0 & \text{otherwise}
# \end{cases}
# \vspace{5mm}%
# \\
# \begin{cases}
#       1 & \text{if bank $i$ issues AtyjtyjtyjtjtjytjuBs at time $t$}\\
#       2 & \text{if bank $i$ issues CBs at time $t$}\\
#       0 & \text{otherwise}
# \end{cases} 
# \end{align*}


# \end{document}



    


# Générez le fichier PDF
doc.generate_pdf(clean_tex=False, compiler='pdflatex')