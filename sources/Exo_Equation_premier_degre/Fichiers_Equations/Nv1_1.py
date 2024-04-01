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

        # Fonction de pgcd pour pouvoir simplifier la fraction au maximum
        pgcd_frac1 = pgcd(nb1,nb2)
        nb1 = nb1//pgcd_frac1
        nb2 = nb2//pgcd_frac1

        pgcd_frac2 = pgcd(nb4,nb5)
        nb4 = nb4//pgcd_frac2
        nb5 = nb5//pgcd_frac2

        # Les fractions sont simplifiées si c'est possible
        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s - %s &= \\frac{%s}{%s} -%sx - %s\\\\" % (nb1,nb2,nb3,nb3,nb4,nb5,nb6,nb3)))
        
        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %sx &= \\frac{%s}{%s} -%sx + %sx - %s\\\\" % (nb1,nb2,nb6,nb4,nb5,nb6,nb6,nb3)))

        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %sx &= \\frac{%s}{%s} - %s\\\\" % (nb1,nb2,nb6,nb4,nb5,nb3)))

        #On met tout les valeurs sur le même dénominateurs pour pouvoir les additionner
        nb6 = nb2*nb6
        nb3 = nb5*nb3
        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + \\frac{%s}{%s}x &= \\frac{%s}{%s} - \\frac{%s}{%s}\\\\" % (nb1,nb2,nb6,nb2,nb4,nb5,nb3,nb5)))

        #On simplifie en additionnant les fraction entre elles
        nbx = nb1 + nb6
        nb = nb4 - nb3
        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x &= \\frac{%s}{%s} \\\\" % (nbx,nb2,nb,nb5)))

        #On multiplie par l'inverse de la fraction de x pour obtenir la valeur pour x
        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x \\times \\frac{%s}{%s} &= \\frac{%s}{%s} \\times \\frac{%s}{%s} \\\\" % (nbx,nb2,nb2,nbx,nb,nb5,nb2,nbx)))

        #On calcule cette multiplication de fraction

        #calcul resultat fraction
        nb_num = nb*nb2
        nb_den = nb5*nbx

        #calcul du pgcd si c'est possible d'arrondir
        pgcd_frac_result = pgcd(nb_num,nb_den)
        nb_num = nb_num//pgcd_frac_result
        nb_den = nb_den//pgcd_frac_result
        doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s}{%s}  \\\\" % (nb_num,nb_den)))


    else :
        if (nb1==nb2) and (nb4==nb5):

            #Ils sont pareils donc on affiche 1 (frac1&2)
            doc.append(NoEscape("\\  \\Leftrightarrow x +%s - %s +%sx &= %s -%sx +%sx - %s \\\\" % (nb3,nb3,nb6,nb_value,nb6,nb6,nb3)))

            #On developpe
            doc.append(NoEscape("\\  \\Leftrightarrow x + %sx &= %s -%s \\\\" % (nb6,nb_value,nb3)))

            #On developpe
            nbx = nb_value + nb6
            nb = nb_value - nb3
            doc.append(NoEscape("\\  \\Leftrightarrow %sx &= -%s \\\\" % (nbx,nb)))

            #On divise par x pour obtenir la valeur de x
            doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{%s}{%s} \\\\" % (nbx,nbx,nb,nbx)))

            #On simplifie et on calcule le pgcd si il est nécésaire
            pgcd_frac1 = pgcd(nb,nbx)
            nb = nb//pgcd_frac1
            nbx = nbx//pgcd_frac1
            doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s}{%s} \\\\" % (nb,nbx)))


        elif (nb1==nb2):
            #Ils sont pareils donc on affiche 1 (frac1&2)
            doc.append(NoEscape("\\  \\Leftrightarrow x +%s - %s &= \\frac{%s}{%s} -%sx - %s \\\\" % (nb3,nb3,nb4,nb5,nb6,nb3)))

            #on calcule le pgcd pour simplifier la fraction
            
            pgcd_frac2 = pgcd(nb4,nb5)
            nb4 = nb4//pgcd_frac2
            nb5 = nb5//pgcd_frac2
            # on déplace les éléments que chaque coté
            doc.append(NoEscape("\\  \\Leftrightarrow x +%sx &= \\frac{%s}{%s} -%sx +%sx - %s \\\\" % (nb6,nb4,nb5,nb6,nb6,nb3)))

            # on passe les elements sur fraction du coté ou cela est nécéssaire et on simplifie les x
            nb3 = nb3*nb5
            nbx = nb6 + nb_value

            doc.append(NoEscape("\\  \\Leftrightarrow %sx &= \\frac{%s}{%s} - \\frac{%s}{%s} \\\\" % (nbx,nb4,nb5,nb3,nb5)))

            #on passe tout sur la meme fraction à droite 
            nb = nb4 - nb3
            doc.append(NoEscape("\\  \\Leftrightarrow %sx &= \\frac{%s}{%s}  \\\\" % (nbx,nb,nb5)))


            doc.append(NoEscape("\\end{align*}"))

        else:

            doc.append(NoEscape("\\ \\text{L'équation à résoudre est : } " % ()))

            doc.append(NoEscape("\\begin{align*}"))
            doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s &= \\frac{%s}{%s} - %sx \\\\" % (nb1,nb2,nb3,nb4,nb5,nb6)))
            doc.append(NoEscape("\\end{align*}"))

            # Etape 1 : 
            doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 1} : Simplions les fractions. Pour cela, multiplions chaque terme de l'équation par le dénominateur commun qui est %s }" % (nb2)))
            
            doc.append(NoEscape("\\begin{align*}"))
            doc.append(NoEscape("\\  \\Leftrightarrow %s \\cdot \\frac{%s}{%s}x + %s \\cdot %s &= %s \\cdot %s - %s \\cdot %sx \\\\" % (nb2,nb1,nb2,nb2,nb3,nb2,nb_value,nb2,nb6)))
            nb = nb2*nb3
            nbx = nb2 * nb6
            doc.append(NoEscape("\\  \\Leftrightarrow %sx + %s &= %s - %sx \\\\" % (nb1,nb,nb2,nbx)))
            doc.append(NoEscape("\\end{align*}"))

            








        