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
    #on cré de nouvelle valeurs aléatoire
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
    doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
    doc.append(pylatex.Command('selectfont'))

    #Numéro de l'exos
    with doc.create(Section(f'Exo Equation du premier degré n°{num_exo + 1}', numbering = False)):
        doc.append("Pour chaque équation du premier degré suivante : Trouver la valeur de x ")


        #Pour chaque niveau, on écrit directement du code Latex brute qui sera inséré dans le document latex

        # les elements ne sont pas dans un environement dcp on met le '$' au début et fin
# niveau 1
        with doc.create(Subsection("Equation niveau 1 : ", numbering = False)):
            doc.append(NoEscape("\\ $%s - %sx = %s + %s $" % (nb1, nb2, nb3, nb4)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())
            doc.append(NoEscape("\\ $%s + %sx  = %s + %s$" % (nb5, nb6, nb7, nb8)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())
            doc.append(NoEscape("\\ $%s + %s = %sx - %s$" % (nb9, nb10, nb11, nb12)))
# niveau 2
        with doc.create(Subsection("Equation niveau 2 : ", numbering = False)):
            doc.append(NoEscape("$\\frac{%s}{%s}x + %s = \\frac{%s}{%s} - %sx$" % (nb1, nb2, nb3, nb4, nb5, nb6)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())
            doc.append(NoEscape("$\\ %s + \\frac{%s}{%s}x = \\frac{%s}{%s}$" % (nb7, nb8, nb9, nb10, nb11)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())
            doc.append(NoEscape("$\\frac{%s}{%s}x - %s = \\frac{%s}{%s} - %sx$" % (nb1, nb3, nb5, nb7, nb9, nb12)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())
#niveau 3
        with doc.create(Subsection("Equation niveau 3 : ", numbering = False)):
            doc.append(NoEscape("$\\ %s(%sx + %s) + %sx = %s(%sx - %s)$" % (nb1, nb2, nb3, nb4, nb5, nb6, nb7)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())
            doc.append(NoEscape("$\\ \\frac{-%s}{%sx + %s} = \\frac{%s}{%s}$" % (nb8, nb9, nb10, nb11, nb12)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())



# On ajoute une page entre les consignes et la correction
    doc.append(NewPage())

#correction des équations
    with doc.create(Section(f'Correction Exo Equation du premier degré n°{num_exo + 1}', numbering = False)):

        with doc.create(Subsection("Equations niveau 1", numbering = False)):
            # pour chauqeu niveau on crée un environement avec la librairie amsmaths (latex)
            # on ne met donc plus les '$'
            # \\Leftrightarrow permet de mettre les doubles flêches
            # \\times pour les signes de multiplication
            # pour aligner tout les element entre eux (signes égales) et au pour les séparer on utilise '&' de la lib amsmath 
            # pour résoudre chaque équation on développe chaque étape
            # sur une meme ligne on retrouve 3 ligne d'équation : à chaque fois celle de chaque équation... 

# correction niveau 1
            doc.append(NoEscape("\\begin{align*}"))
            doc.append(NoEscape("\\  \\Leftrightarrow %s - %sx &= %s + %s     & \\Leftrightarrow %s + %sx  &= %s + %s       & \\Leftrightarrow %s + %s &= %sx - %s\\\\" % (nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9, nb10, nb11, nb12)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            doc.append(NoEscape("\\  \\Leftrightarrow %s - %s - %sx &= %s + %s -%s      & \\Leftrightarrow %s - %s + %sx  &= %s + %s + %s        & \\Leftrightarrow %s + %s + %s &= %sx - %s +%s\\\\" % (nb1, nb1, nb2, nb3, nb4, nb1, nb5, nb5, nb6, nb7, nb8, nb5, nb9, nb10,nb12, nb11, nb12, nb12 )))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            newnb_1 = nb3 + nb4 - nb1
            newnb_2 = nb5 + nb7 + nb8
            newnb_3 = nb9 + nb10 + nb12
            doc.append(NoEscape("\\  \\Leftrightarrow \\frac{-%sx}{-%s} &= \\frac{%s}{-%s}      & \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{%s}{%s}      & \\Leftrightarrow \\frac{%s}{%s} &= \\frac{%sx}{%s}\\\\" % (nb2, nb2, newnb_1, nb2, nb6,nb6, newnb_2, nb6, newnb_3, nb11, nb11, nb11)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            result_1 = round((newnb_1 / (- nb2)),1)
            result_2 = round((newnb_2 / nb6),1)
            result_3 = round((newnb_3 / nb11),1)
            doc.append(NoEscape("\\  \\Leftrightarrow  x &= %s      & \\Leftrightarrow  x &= %s      & \\Leftrightarrow  x &= %s\\\\" % (result_1, result_2, result_3)))

            doc.append(NoEscape("\\end{align*}"))
        
# correction niveau 2
        with doc.create(Subsection("Equations niveau 2", numbering = False)):

            doc.append(NoEscape("\\begin{align*}"))

            doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s &= \\frac{%s}{%s} - %sx       &     \\Leftrightarrow %s + \\frac{%s}{%s}x &= \\frac{%s}{%s}     &     \\Leftrightarrow  \\frac{%s}{%s}x - %s &= \\frac{%s}{%s} - %sx\\\\" % (nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9, nb10, nb11, nb1, nb3, nb5, nb7, nb9, nb12)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s + %sx  &= \\frac{%s}{%s} - %sx +%sx    &    \\Leftrightarrow %s - %s + \\frac{%s}{%s}x &= \\frac{%s}{%s} + %s      &     \\Leftrightarrow  \\frac{%s}{%s}x +%sx - %s &= \\frac{%s}{%s} - %sx  + %sx\\\\" % (nb1, nb2, nb3, nb6, nb4, nb5, nb6, nb6, nb7,nb7, nb8, nb9, nb10, nb11, nb7,nb1, nb3,nb12, nb5, nb7, nb9, nb12, nb12)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            newnbx_1 = round(((nb1 / nb2) + nb6),1)
            newnb_5 = round(((nb10/nb11)+ nb7),1)
            newnbx_2 = round(((nb1/nb2)+nb12),1)
            doc.append(NoEscape("\\  \\Leftrightarrow %sx + %s - %s &= \\frac{%s}{%s}	- %s       &      \\Leftrightarrow \\frac{%s}{%s}x &= %s     &   \\Leftrightarrow  %sx - %s +%s &= \\frac{%s}{%s} + %s\\\\" % (newnbx_1, nb3, nb3, nb4, nb5, nb3, nb8, nb9, newnb_5,newnbx_2, nb5,nb5, nb7, nb9 ,nb5)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            newnb_4 = round(((nb4/nb5)-nb3),1)
            newnb_6 = round(((nb7/nb9)+nb5),1)
            doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{%s}{%s}     &      \\Leftrightarrow \\frac{%s}{%s}x \\times \\frac{%s}{%s} &= %s x \\times \\frac{%s}{%s}      &      \\Leftrightarrow  \\frac{%sx}{%s} &= \\frac{%s}{%s}\\\\" % (newnbx_1, newnbx_1, newnb_4, newnbx_1, nb8, nb9,nb9, nb8, newnb_5, nb9, nb8, newnbx_2,newnbx_2, newnb_6, newnbx_2)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            result_4 = round((newnb_4/newnbx_1),1)
            result_5 = round((newnb_5 * (nb9/nb8)),1)
            result_6 = round((newnb_6/newnbx_2),1)
            doc.append(NoEscape("\\  \\Leftrightarrow x &= %s    &     \\Leftrightarrow x &= %s     &     \\Leftrightarrow  x &= %s\\\\" % (result_4, result_5, result_6)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            doc.append(NoEscape("\\end{align*}"))

# correction niveau 3
        with doc.create(Subsection("Equations niveau 3", numbering = False)):

            doc.append(NoEscape("\\begin{align*}"))

            doc.append(NoEscape("\\ \\Leftrightarrow %s(%sx + %s) + %sx &= %s(%sx - %s)\\\\" % (nb1, nb2, nb3, nb4, nb5, nb6, nb7)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            doc.append(NoEscape("\\ \\Leftrightarrow %s \\times %sx + %s \\times %s + %sx     &=      %s \\times %sx - %s \\times %s\\\\" % (nb1, nb2, nb1, nb3, nb4, nb5, nb6, nb5, nb7)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            nv3_newnb_1 = (nb1 * nb2) + nb4
            nv3_newnb_2 = nb1 * nb3
            nv3_newnb_3 = nb5 * nb6
            nv3_newnb_4 = nb5 * nb7
            doc.append(NoEscape("\\ \\Leftrightarrow %sx + %s   &= %sx - %s\\\\" % (nv3_newnb_1, nv3_newnb_2, nv3_newnb_3, nv3_newnb_4)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            doc.append(NoEscape("\\ \\Leftrightarrow %sx -%sx + %s - %s   &=  %sx - %sx + %s - %s\\\\" % (nv3_newnb_1, nv3_newnb_3, nv3_newnb_2, nv3_newnb_2, nv3_newnb_3, nv3_newnb_3, nv3_newnb_4, nv3_newnb_2)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            nv3_new2nb_1 = nv3_newnb_1 - nv3_newnb_3
            nv3_new2nb_2 = nv3_newnb_4 - nv3_newnb_2
            doc.append(NoEscape("\\ \\Leftrightarrow \\frac{%sx}{%s}   &= \\frac{%s}{%s}\\\\" % (nv3_new2nb_1, nv3_new2nb_1, nv3_new2nb_2, nv3_new2nb_1)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            result_nv3 = round((nv3_new2nb_2/nv3_new2nb_1),1)
            doc.append(NoEscape("\\ \\Leftrightarrow x  &= %s\\\\" % (result_nv3)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            doc.append(NoEscape("\\end{align*}"))


            doc.append(NewLine())




            doc.append(NoEscape("\\begin{align*}"))

            doc.append(NoEscape("\\  \\Leftrightarrow \\frac{-%s}{%sx + %s} &= \\frac{%s}{%s}\\\\" % (nb8, nb9, nb10, nb11, nb12)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            doc.append(NoEscape("\\   \\Leftrightarrow \\frac{-%s}{%sx + %s} \\times( %sx + %s) \\times %s &= \\frac{%s}{%s} \\times %s \\times (%sx + %s)\\\\" % (nb8, nb9, nb10,nb9, nb10,nb12, nb11, nb12, nb12, nb9, nb10)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            nv3_newnb_3 = nb5*nb6
            nv3_newnb_4 = nb5*nb7
            doc.append(NoEscape("\\  \\Leftrightarrow -%s \\times %s &= %s \\times (%sx + %s)\\\\" % (nb8, nb12, nb11, nb9, nb10)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())


            nv3_newnb_5 = ((-nb8)*nb12)
            nv3_newnb_6 = (nb11*nb9)
            nv3_newnb_7 = (nb11*nb10)
            doc.append(NoEscape("\\   \\Leftrightarrow \\ %s - %s &= %sx + %s - %s\\\\" % (nv3_newnb_5,nv3_newnb_7, nv3_newnb_6, nv3_newnb_7, nv3_newnb_7)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            nv3_new2nb_3 = nv3_newnb_5 - nv3_newnb_7
            doc.append(NoEscape("\\   \\Leftrightarrow \\frac{%s}{%s} &= \\frac{%sx}{%s}\\\\" % (nv3_new2nb_3,nv3_newnb_6,  nv3_newnb_6, nv3_newnb_6)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())

            result_nv3_2 = round((nv3_new2nb_3/nv3_newnb_6),1)
            doc.append(NoEscape("\\   \\Leftrightarrow x &= %s\\\\" % (result_nv3_2)))
            doc.append(Command('vspace', '3mm'))
            doc.append(NewLine())


            doc.append(NoEscape("\\end{align*}"))
