from pylatex import *
from pylatex.utils import * 

import random


def pgcd(a,b):
    # pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b
    while b != 0:
        a,b=b,a%b
    return a

### LIGNE DE L'EXO ###
def ligne_exo(doc,nb1,nb2,nb3,nb4,nb5,nb6,nb_value):

    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s &= \\frac{%s}{%s} - %sx \\\\" % (nb1,nb2,nb3,nb4,nb5,nb6)))
    doc.append(NoEscape("\\end{align*}"))

### CORRECTION DE L'EXO ###
# Toutes les simplification sont faites si possible en fonction (simplification de fraction...)
def correction_exo(doc,nb1,nb2,nb3,nb4,nb5,nb6,nb_value):

    doc.append(NoEscape("\\begin{align*}"))

    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s &= \\frac{%s}{%s} - %sx \\\\" % (nb1,nb2,nb3,nb4,nb5,nb6)))

    doc.append(NoEscape("\\end{align*}"))

    #On regarde s'ils sont différents pour savoir si on doit simplifier directement la fraction ou non 
    if (nb2 != nb1) and (nb4!=nb5):

        doc.append(NoEscape("\\ \\text{L'équation à résoudre est : } " % ()))

        doc.append(NoEscape("\\begin{align*}"))
        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s &= \\frac{%s}{%s} - %sx \\\\" % (nb1,nb2,nb3,nb4,nb5,nb6)))
        doc.append(NoEscape("\\end{align*}"))


        # Etape 1
        deno_com = nb2*nb5
        doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 1} : Simplifions les fractions. Pour simplifier, multiplions chaque terme de l’équation par le dénominateur commun, qui est (%s) (le produit de (%s) et (%s)) : }" % (deno_com,nb2,nb5)))
        
        doc.append(NoEscape("\\begin{align*}"))
        doc.append(NoEscape("\\  \\Leftrightarrow %s \\cdot \\left(\\frac{%s}{%s}x + %s\\right) &= %s \\cdot \\left(\\frac{%s}{%s} - %sx\\right) \\\\" % (deno_com,nb1,nb2,nb3, deno_com,nb4,nb5,nb6)))
        nbx =((nb1 * deno_com)//nb2)
        nb = nb3 * deno_com
        nb_2 = ((deno_com *nb4)//nb5)
        nbx_2 = (deno_com *nb6)
        doc.append(NoEscape("\\  \\Leftrightarrow %sx + %s &= %s - %sx \\\\" % (nbx,nb,nb_2,nbx_2)))
        doc.append(NoEscape("\\end{align*}"))

        # Etape 2
        doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 2} : Regroupons les termes contenant la variable x d’un côté de l’équation et les termes constants de l’autre côté.}" % ()))

        doc.append(NoEscape("\\begin{align*}"))
        doc.append(NoEscape("\\  \\Leftrightarrow %sx + %s - %s + %sx &= %s - %sx + %sx - %s \\\\" % (nbx,nb,nb,nbx_2,nb_2,nbx_2,nbx_2,nb)))
        nb = nb_2 - nb
        nbx = nbx + nbx_2
        doc.append(NoEscape("\\  \\Leftrightarrow %sx &= %s \\\\" % (nbx,nb)))
        doc.append(NoEscape("\\end{align*}"))

        # Etape 3
        doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 3} : Divisons les deux côtés de l’équation par %s pour isoler x et simplifions: }" % (nbx)))

        doc.append(NoEscape("\\begin{align*}"))
        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{%s}{%s} \\\\" % (nbx,nbx,nb,nbx)))
        pgcd_frac3 = pgcd(nb,nbx)
        nb = nb//pgcd_frac3
        nbx = nbx//pgcd_frac3
        doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s}{%s} \\\\" % (nb,nbx)))
        doc.append(NoEscape("\\end{align*}"))


    else :
        if (nb1==nb2) and (nb4==nb5):

            # doc.append(NoEscape("\\ \\text{L'équation à résoudre est : } " % ()))

            # doc.append(NoEscape("\\begin{align*}"))
            # doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s &= \\frac{%s}{%s} - %sx \\\\" % (nb1,nb2,nb3,nb4,nb5,nb6)))
            # doc.append(NoEscape("\\end{align*}"))


        elif (nb1==nb2):

            # doc.append(NoEscape("\\ \\text{L'équation à résoudre est : } " % ()))

            # doc.append(NoEscape("\\begin{align*}"))
            # doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s &= \\frac{%s}{%s} - %sx \\\\" % (nb1,nb2,nb3,nb4,nb5,nb6)))
            # doc.append(NoEscape("\\end{align*}"))


        else:

            doc.append(NoEscape("\\ \\text{L'équation à résoudre est : } " % ()))

            doc.append(NoEscape("\\begin{align*}"))
            doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s &= \\frac{%s}{%s} - %sx \\\\" % (nb1,nb2,nb3,nb4,nb5,nb6)))
            doc.append(NoEscape("\\end{align*}"))

            # Etape 1
            doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 1} : Simplions les fractions. Pour cela, multiplions chaque terme de l'équation par le dénominateur commun qui est %s : }" % (nb2)))
            
            doc.append(NoEscape("\\begin{align*}"))
            doc.append(NoEscape("\\  \\Leftrightarrow %s \\cdot \\frac{%s}{%s}x + %s \\cdot %s &= %s \\cdot %s - %s \\cdot %sx \\\\" % (nb2,nb1,nb2,nb2,nb3,nb2,nb_value,nb2,nb6)))
            nb = nb2*nb3
            nbx = nb2 * nb6
            doc.append(NoEscape("\\  \\Leftrightarrow %sx + %s &= %s - %sx \\\\" % (nb1,nb,nb2,nbx)))
            doc.append(NoEscape("\\end{align*}"))

            # Etape 2
            doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 2} : Regroupons les termes contenant la variable x d’un côté de l’équation et les termes constants de l’autre côté. Ajoutons %sx des deux côtés et retirons %s des deux côtés également : }" % (nbx,nb)))

            doc.append(NoEscape("\\begin{align*}"))
            doc.append(NoEscape("\\  \\Leftrightarrow %sx + %s -%s + %sx &= %s - %sx + %sx -%s \\\\" % (nb1,nb,nb,nbx,nb2,nbx,nbx,nb)))
            nb = nb2 - nb
            nbx = nb1 + nbx
            doc.append(NoEscape("\\  \\Leftrightarrow %sx &= %s \\\\" % (nbx,nb)))
            doc.append(NoEscape("\\end{align*}"))

            # Etape 3
            doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 3} : Divisons les deux côtés de l’équation par %s pour isoler x et simplifions: }" % (nbx)))

            doc.append(NoEscape("\\begin{align*}"))
            doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{%s}{%s} \\\\" % (nbx,nbx,nb,nbx)))
            pgcd_frac3 = pgcd(nb,nbx)
            nb = nb//pgcd_frac3
            nbx = nbx//pgcd_frac3
            doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s}{%s} \\\\" % (nb,nbx)))
            doc.append(NoEscape("\\end{align*}"))







        