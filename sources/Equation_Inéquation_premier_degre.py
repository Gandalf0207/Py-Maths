# Module de création du Fichier Tex et convertion en pdf et autre
from pylatex import *
from pylatex.utils import *

#Modules de création, g raphe, courbe.....
import matplotlib.backends.backend_pdf
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Modules de calcul...
import math
import random

# Modle de convertion / création des formules / la forme
import latexify
from sympy import *

#Module de gestion fichier sur la machine
import os
import glob



def write(doc, num_exo):

    #Avec sympy, définition du symbole pour le polynôme 
    x = Symbol('x')


    nb1 = random.randint(1,50)
    nb2 = random.randint(1,50)
    nb3 = random.randint(1,50)
    nb4 = random.randint(1,50)
    nb5 = random.randint(1,50)
    nb6 = random.randint(1,50)
    nb7 = random.randint(1,50)
    nb8 = random.randint(1,50)
    nb9 = random.randint(1,50)
    nb10 = random.randint(1,50)
    nb11 = random.randint(1,50)
    nb12 = random.randint(1,50)



   # Définitions de la taille de police d'écriture
    doc.append(pylatex.Command('fontsize', arguments = ['20', '15']))
    doc.append(pylatex.Command('selectfont'))

    #Numéro de l'exos
    with doc.create(Section(f'Equation du premier degré n°{num_exo + 1}', numbering = False)):
        doc.append("Avec les équations du premier degré suivantes : ")

        with doc.create(Subsection("Equation niveau 1 : ", numbering = False)):
            doc.append(NoEscape("\\ $%s - %sx = %s + %s $" % (nb1, nb2, nb3, nb4)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())
            doc.append(NoEscape("\\ $%s + %sx  = %s + %s$" % (nb5, nb6, nb7, nb8)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())
            doc.append(NoEscape("\\ $%s + %s = %sx - %s$" % (nb9, nb10, nb11, nb12)))

        with doc.create(Subsection("Equation niveau 2 : ", numbering = False)):
            doc.append(NoEscape("$\\frac{%s}{%s} + %s = \\frac{%s}{%s} - %s$" % (nb1, nbx1, nbx1, nb2, nbx2, nb1)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())
            doc.append(NoEscape("$\\ %s + \\frac{%s}{%s} = \\frac{%s}{%s}$" % (nb3, nb4, nbx3, nb2, nbx4)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())
            doc.append(NoEscape("$\\frac{%s + %s}{%s + %s} = \\frac{%sx}{%s}$" % (nb5, nbx5, nbx6, nbx4, nb6, nb5)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())


#correction des équations
    with doc.create(Section(f'CorrectionEquation du premier degré n°{num_exo + 1}', numbering = False)):
        with doc.create(MiniPage(align='c')):

            doc.append(NoEscape("\\ $ \\Leftrightarrow %s - %sx = %s + %s $" % (nb1, nb2, nb3, nb4)))
            doc.append(Command('vspace', '5mm'))
            doc.append(LineBreak())
            doc.append(NoEscape("\\ $ \\Leftrightarrow %s - %s - %sx = %s + %s -%s $" % (nb1, nb1, nb2, nb3, nb4, nb1 )))
            doc.append(Command('vspace', '5mm'))
            doc.append(LineBreak())
            newnb_1 = nb3 + nb4 + nb1
            doc.append(NoEscape("\\ $ \\Leftrightarrow \\frac{%sx}{%s} = \\frac{%s}{%s} $" % (nb2, nb2, newnb_1, nb2)))
            doc.append(Command('vspace', '5mm'))
            doc.append(LineBreak())
            result_1 = round((newnb_1 / nb2),1)
            doc.append(NoEscape("\\ $ \\Leftrightarrow  x = %s $" % (result_1)))

###EXEMPLE : 

    # nomP = 15
    # var = 12
    # aab = 5

    # #On donne l'équation du premier degré à résoudre 
    # with doc.create(Section("Hello")):
    #     doc.append(NoEscape("\\ $%s(%s + 5x)=%s$" % (nomP, var, aab)))
