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
    doc.append(pylatex.Command('fontsize', arguments = ['15', '12']))
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
            doc.append(NoEscape("$\\frac{%s}{%s}x + %s = \\frac{%s}{%s} - %sx$" % (nb1, nb2, nb3, nb4, nb5, nb6)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())
            doc.append(NoEscape("$\\ %s + \\frac{%s}{%s}x = \\frac{%s}{%s}$" % (nb7, nb8, nb9, nb10, nb11)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())
            doc.append(NoEscape("$\\frac{%s}{%s}x - %s = \\frac{%s}{%s} - %sx$" % (nb1, nb3, nb5, nb7, nb9, nb12)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())


# On ajoute une page entre les consignes et la correction
    doc.append(NewPage())

#correction des équations
    with doc.create(Section(f'Correction Equation du premier degré n°{num_exo + 1}', numbering = False)):
        doc.append("Niveau 1 :")


#### fonctionne pas 
### regarde lib latex : amsmat
# visualisation convaincante sur overleaf
        with doc.create(Subsection("Niveau 1 :")):

            with doc.create(Center()):
                # with doc.create(MiniPage()):
                doc.append("Equations n°1")
                doc.append(Command('vspace', '10mm'))
                # doc.append(LineBreak())
                doc.append(NewLine())

                doc.append(NoEscape("\\ $ \\Leftrightarrow %s - %sx = %s + %s $" % (nb1, nb2, nb3, nb4)))
                doc.append(Command('vspace', '5mm'))
                # doc.append(LineBreak())
                doc.append(NewLine())

                doc.append(NoEscape("\\ $ \\Leftrightarrow %s - %s - %sx = %s + %s -%s $" % (nb1, nb1, nb2, nb3, nb4, nb1 )))
                doc.append(Command('vspace', '5mm'))
                # doc.append(LineBreak())
                doc.append(NewLine())

                newnb_1 = nb3 + nb4 - nb1
                doc.append(NoEscape("\\ $ \\Leftrightarrow \\frac{-%sx}{-%s} = \\frac{%s}{-%s} $" % (nb2, nb2, newnb_1, nb2)))
                doc.append(Command('vspace', '5mm'))
                # doc.append(LineBreak())
                doc.append(NewLine())

                result_1 = round((newnb_1 / (- nb2)),1)
                doc.append(NoEscape("\\ $ \\Leftrightarrow  x = %s $" % (result_1)))


            # doc.append(Command('hspace', '2cm'))   
            # doc.append(NewLine())
            
                
            with doc.create(Center()):
                doc.append("Equations n°2")
                doc.append(Command('vspace', '10mm'))
                doc.append(LineBreak())

                doc.append(NoEscape("\\ $ \\Leftrightarrow %s + %sx  = %s + %s$" % (nb5, nb6, nb7, nb8)))
                doc.append(Command('vspace', '5mm'))
                doc.append(LineBreak())

                doc.append(NoEscape("\\ $ \\Leftrightarrow %s - %s + %sx  = %s + %s + %s$" % (nb5, nb5, nb6, nb7, nb8, nb5)))
                doc.append(Command('vspace', '5mm'))
                doc.append(LineBreak())

                newnb_2 = nb5 + nb7 + nb8
                doc.append(NoEscape("\\ $ \\Leftrightarrow %sx  = %s $" % (nb6, newnb_2)))
                doc.append(Command('vspace', '5mm'))
                doc.append(LineBreak())

                doc.append(NoEscape("\\ $ \\Leftrightarrow \\frac{%sx}{%s} = \\frac{%s}{%s} $" % (nb6,nb6, newnb_2, nb6)))
                doc.append(Command('vspace', '5mm'))
                doc.append(LineBreak())

                result_2 = round((newnb_2 / nb6),1)
                doc.append(NoEscape("\\ $ \\Leftrightarrow  x = %s $" % (result_2)))

###EXEMPLE : 

    # nomP = 15
    # var = 12
    # aab = 5

    # #On donne l'équation du premier degré à résoudre 
    # with doc.create(Section("Hello")):
    #     doc.append(NoEscape("\\ $%s(%s + 5x)=%s$" % (nomP, var, aab)))
