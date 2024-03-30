from pylatex import *
from pylatex.utils import * 

import random

def pgcd(a,b):
    # pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b
    while b != 0:
        a,b=b,a%b
    return a


nb1 = random.randint(1,10)
nb2 = random.randint(1,10)

# Créez un document
doc = Document()

doc.packages.append(NoEscape("\\usepackage{amsmath}"))


doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
doc.append(pylatex.Command('selectfont'))

with doc.create(Section("Section de test", numbering = False)):
    doc.append("Niveau 1 :")

#tu ecris entre ces deux éléments

    doc.append(NoEscape("\\begin{align*}"))

    nb_value = 1
    nb1 = random.randint(1,10)
    nb2 = random.randint(1,10)
    nb3 = random.randint(1,10)
    nb4 = random.randint(1,10)
    nb5 = random.randint(1,10)
    nb6 = random.randint(1,10)
        

        
    ### LIGNE DE L'EXO ###

    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s &= \\frac{%s}{%s} - %sx \\\\" % (nb1,nb2,nb3,nb4,nb5,nb6)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    ### LIGNE 1 ###

    #On regarde s'ils sont différents pour savoir si on doit simplifier directement la fraction ou non 
    if (nb2 != nb1) and (nb4!=nb5):

        # Fonction de pgcd pour pouvoir simplifier la fraction au maximum
        pgcd_frac1 = pgcd(nb1,nb2)
        nb1 = nb1//pgcd_frac1
        nb2 = nb2//pgcd_frac1

        pgcd_frac2 = pgcd(nb4,nb5)
        nb4 = nb4//pgcd_frac2
        nb5 = nb5//pgcd_frac2

        # Les fractions sont simplifiées si c'est possible
        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s - %s &= \\frac{%s}{%s} -%sx - %s\\\\" % (nb1,nb2,nb3,nb3,nb4,nb5,nb6,nb3)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

    else :
        if (nb1==nb2):

            #Ils sont pareils donc on affiche 1 (frac1)
            doc.append(NoEscape("\\  \\Leftrightarrow x +%s - %s &= \\frac{%s}{%s} -%sx - %s \\\\" % (nb3,nb3,nb4,nb5,nb6,nb3)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())
        else:
            #Ils sont pareils donc on affiche 1 (frac2)
            doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s - %s &= %s -%sx - %s\\\\" % (nb1,nb2,nb3,nb3,nb_value,nb6,nb3)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())


    ### LIGNE 2 ###


        doc.append(NoEscape("\\\\"))
        doc.append(NoEscape("\\\\"))






    doc.append(NoEscape("\\  \\Leftrightarrow  &= \\\\" % ()))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    doc.append(NoEscape("\\  \\Leftrightarrow  &= \\\\" % ()))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    doc.append(NoEscape("\\ \\Leftrightarrow   &= \\\\" % ()))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())




    doc.append(NoEscape("\\end{align*}"))


# Générez le fichier PDF
doc.generate_pdf(clean_tex=False, compiler='pdflatex')