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
    nb1 = random.randint(2,20)
    nb2 = random.randint(2,20)
    nb3 = random.randint(2,20)
    nb4 = random.randint(2,20)
    nb5 = random.randint(2,20)
    nb6 = random.randint(2,20)
        


    ### LIGNE DE L'EXO ###

    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s &= \\frac{%s}{%s} - %sx \\\\" % (nb1,nb2,nb3,nb4,nb5,nb6)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())



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

        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %sx &= \\frac{%s}{%s} -%sx + %sx - %s\\\\" % (nb1,nb2,nb6,nb4,nb5,nb6,nb6,nb3)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %sx &= \\frac{%s}{%s} - %s\\\\" % (nb1,nb2,nb6,nb4,nb5,nb3)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        #On met tout les valeurs sur le même dénominateurs pour pouvoir les additionner
        nb6 = nb2*nb6
        nb3 = nb5*nb3

        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + \\frac{%s}{%s}x &= \\frac{%s}{%s} - \\frac{%s}{%s}\\\\" % (nb1,nb2,nb6,nb2,nb4,nb5,nb3,nb5)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        #On simplifie en additionnant les fraction entre elles
        nbx = nb1 + nb6
        nb = nb4 - nb3

        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x &= \\frac{%s}{%s} \\\\" % (nbx,nb2,nb,nb5)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        #On multiplie par l'inverse de la fraction de x pour obtenir la valeur pour x

        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x \\times \\frac{%s}{%s} &= \\frac{%s}{%s} \\times \\frac{%s}{%s} \\\\" % (nbx,nb2,nb2,nbx,nb,nb5,nb2,nbx)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        #On calcule cette multiplication de fraction

            #calcul resultat fraction
        nb_num = nb*nb2
        nb_den = nb5*nbx

            #calcul du pgcd si c'est possible d'arrondir
        pgcd_frac_result = pgcd(nb_num,nb_den)
        nb_num = nb_num//pgcd_frac_result
        nb_den = nb_den//pgcd_frac_result

        doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s}{%s}  \\\\" % (nb_num,nb_den)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

    else :
        if (nb1==nb2) and (nb4==nb5):

            #Ils sont pareils donc on affiche 1 (frac1&2)
            doc.append(NoEscape("\\  \\Leftrightarrow x +%s - %s +%sx &= %s -%sx +%sx - %s \\\\" % (nb3,nb3,nb6,nb_value,nb6,nb6,nb3)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())

            #On developpe
            doc.append(NoEscape("\\  \\Leftrightarrow x + %sx &= %s -%s \\\\" % (nb6,nb_value,nb3)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())

            #On developpe
            nbx = 1 + nb6
            nb = 1 - nb3

            doc.append(NoEscape("\\  \\Leftrightarrow %sx &= -%s \\\\" % (nbx,nb)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())

            #On divise par x pour obtenir la valeur de x

            doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{%s}{%s} \\\\" % (nbx,nbx,nb,nbx)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())

            #On simplifie et on calcule le pgcd si il est nécésaire

            pgcd_frac1 = pgcd(nb,nbx)
            nb = nb//pgcd_frac1
            nbx = nbx//pgcd_frac1

            doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s}{%s} \\\\" % (nb,nbx)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())



        elif (nb1==nb2):
            #Ils sont pareils donc on affiche 1 (frac1&2)
            doc.append(NoEscape("\\  \\Leftrightarrow x +%s - %s &= \\frac{%s}{%s} -%sx - %s \\\\" % (nb3,nb3,nb4,nb5,nb6,nb3)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())

        else:
            #Ils sont pareils donc on affiche 1 (frac2)
            doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s - %s &= %s -%sx - %s\\\\" % (nb1,nb2,nb3,nb3,nb_value,nb6,nb3)))
            doc.append(Command('vspace', '5mm'))
            doc.append(NewLine())




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