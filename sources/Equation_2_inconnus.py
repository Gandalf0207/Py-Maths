### DÉBUT DE L'EXO ÉQUATION à 2 INCONNUES ###

## Importation des Librairies : 

# Module de création du Fichier Tex et convertion en pdf et autre
from pylatex import *
from pylatex.utils import *

#Modules de calcul...
import math
import random





def write(doc,i):
    # on génère les valeurs aléatoirement pour avoir de nouveau exercices !
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
    nb11= random.randint(1,50)

    # valeurs légèrement différentes pour le niveau 3 pour éviter de trop gros nombres
    nb1_nv3 = random.randint(1,10)
    nb2_nv3 = random.randint(1,10)
    nb3_nv3 = random.randint(1,10)
    nb4_nv3 = random.randint(1,10)
    nb5_nv3 = random.randint(1,10)
    nb6_nv3 = random.randint(1,10)
    nb7_nv3 = random.randint(1,10)
    nb8_nv3 = random.randint(1,10)
    nb9_nv3 = random.randint(1,10)
    nb10_nv3 = random.randint(1,10)

# on définit la taille de l'écriture pour le document
    doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
    doc.append(pylatex.Command('selectfont'))
    
    with doc.create(Section(f" Exo Équation à 2 inconnues n°{i+1}", numbering = False)):
            # pour chauque niveau on crée un environement avec la librairie amsmaths (latex) : begin{align*} et end{align*}
            # \\Leftrightarrow permet de mettre les doubles flêches
            # \\times pour les signes de multiplication
            # pour aligner tout les element entre eux (signes égales) et au pour les séparer on utilise '&' de la lib amsmath 
            # pour résoudre chaque équation on développe chaque étape dans la partie correction
            # on utilise le module 'cases' de latex pour générer le symbol d'acollade au débus pour la mise en page
        
            # l'element NoEscape permet d'écrire du code brute directement en dans le ficheir latex créé
        doc.append(NoEscape("\\ \\text{Pour chaque système d'équation ci-dessous; calculez la valeur (arrondie si nécéssaire) de $x$ et $y$}\\\\ " % ()))
        doc.append(NoEscape("\\\\"))

# Niveau 1 exo
        doc.append("Niveau 1 :")
        doc.append(NoEscape("\\begin{align*}"))
        doc.append(NoEscape("\\begin{cases}"))
        doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (nb1, nb2, nb5)))
        doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (nb3, nb4, nb6)))
        doc.append(NoEscape("\\end{cases}"))
        doc.append(NoEscape("\\\\"))
        doc.append(NoEscape("\\end{align*}"))


# Niveau 2 exo
        doc.append("Niveau 2 :")

        doc.append(NoEscape("\\begin{align*}"))
        doc.append(NoEscape("\\begin{cases}"))
        doc.append(NoEscape("\\  \\frac{%s}{%s}x + %sy &= %sy - %s \\\\" % (nb1, nb2, nb3, nb4, nb5)))
        doc.append(NoEscape("\\  %sx + %sy &= %sy + \\frac{%s}{%s} \\\\" % (nb6,nb7 ,nb8,nb9,nb10 )))
        doc.append(NoEscape("\\end{cases}"))
        doc.append(NoEscape("\\\\"))
        doc.append(NoEscape("\\end{align*}"))

# Niveau 3 exo
        doc.append("Niveau 3 :")

        doc.append(NoEscape("\\begin{align*}"))
        doc.append(NoEscape("\\begin{cases}"))
        doc.append(NoEscape("\\  %s(%sy + %sx) &= %s \\\\" % (nb1_nv3, nb2_nv3,nb3_nv3, nb4_nv3)))
        doc.append(NoEscape("\\  %sx + %sy &= %s(%sy + %s) \\\\" % (nb5_nv3,nb6_nv3, nb7_nv3, nb8_nv3, nb9_nv3)))
        doc.append(NoEscape("\\end{cases}"))
        doc.append(NoEscape("\\\\"))
        doc.append(NoEscape("\\end{align*}"))


# On ajoute une page entre la correction et les exercices
    doc.append(NewPage())

    with doc.create(Section(f"Correction Exo n°{i+1}", numbering = False)):
# Niveau 1 correction
        doc.append("Niveau 1 :")
# on redonne l'exercices
    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\begin{cases}"))
    doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (nb1, nb2, nb5)))
    doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (nb3, nb4, nb6)))
    doc.append(NoEscape("\\end{cases}"))
    doc.append(NoEscape("\\\\"))
    doc.append(NoEscape("\\end{align*}"))

#puis on développe chaque étape avec un commentaire de ce que l'on fait
    doc.append(NoEscape("\\ \\text{L'équation ligne 2 permet d'écrire :}\\\\" % ()))


    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\  \\Leftrightarrow %sx + %sy - %sy &= %s - %sy \\\\" % (nb3,nb4,nb4,nb6,nb4)))

    doc.append(NoEscape("\\  \\Leftrightarrow %sx &= -%sy + %s\\\\" % (nb3, nb4,nb6)))

    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{-%sy + %s}{%s}\\\\" % (nb3,nb3,nb4,nb6,nb3)))
    doc.append(NoEscape("\\end{align*}"))
    
    doc.append(NoEscape("\\\\"))


    doc.append(NoEscape("\\ \\text{On remplace x par $\\frac{-%sy + %s}{%s}$ dans l'équation 1}\\\\" % (nb4,nb6,nb3)))



    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\ \\Leftrightarrow  %s \\times \\frac{-%sy + %s}{%s} + %sy &= %s\\\\" % (nb1,nb4,nb6,nb3,nb2,nb5)))

    doc.append(NoEscape("\\ \\Leftrightarrow  %s \\times \\frac{-%sy}{%s} + %s \\times \\frac{%s}{%s} + %sy &= %s\\\\" % (nb1,nb4,nb3,nb1,nb6, nb3,nb2,nb5)))

    new_y_1_nv1 = round((nb1*((-nb4)/nb3) + nb2),2)
    new_nb_1_nv1 = round((nb1*(nb6 / nb3)),2)
    doc.append(NoEscape("\\ \\Leftrightarrow  %sy + %s &= %s\\\\" % (new_y_1_nv1, new_nb_1_nv1,nb5)))

    doc.append(NoEscape("\\ \\Leftrightarrow  %sy + %s - %s &= %s - %s\\\\" % (new_y_1_nv1, new_nb_1_nv1,new_nb_1_nv1,nb5,new_nb_1_nv1)))

    new_nb_2_nb1 = round(nb5 - new_nb_1_nv1,2)
    doc.append(NoEscape("\\ \\Leftrightarrow  %sy  &= %s\\\\" % (new_y_1_nv1, new_nb_2_nb1)))

    doc.append(NoEscape("\\ \\Leftrightarrow  \\frac{%sy}{%s}  &= \\frac{%s}{%s}\\\\" % (new_y_1_nv1,new_y_1_nv1, new_nb_2_nb1,new_y_1_nv1)))

    result_y_nv1 = round((new_nb_2_nb1 / new_y_1_nv1),2)
    doc.append(NoEscape("\\ \\Leftrightarrow  y  &\\approx %s\\\\" % (result_y_nv1)))
    doc.append(NoEscape("\\end{align*}"))



    doc.append(NoEscape("\\ \\text{En remplaçant y par la valeur obtenue dans l'équation 1 :}\\\\" % ()))



    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\ \\Leftrightarrow  %sx + %s \\times %s &= %s \\\\" % (nb1,nb2,result_y_nv1,nb5)))

    nb = round((result_y_nv1*nb2),2)
    doc.append(NoEscape("\\ \\Leftrightarrow  %sx + %s -%s &= %s - %s \\\\" % (nb1,nb,nb,nb5, nb)))

    new_nb_3_nv1 = round(nb5 - nb,2)
    doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= %s \\\\" % (nb1, new_nb_3_nv1)))

    doc.append(NoEscape("\\ \\Leftrightarrow  \\frac{%sx}{%s} &= \\frac{%s}{%s}\\\\" % (nb1, nb1,new_nb_3_nv1,nb1)))

    approche = round((new_nb_3_nv1/nb1),2)
    doc.append(NoEscape("\\ \\Leftrightarrow  x &\\approx %s \\\\" % (approche)))
    doc.append(NoEscape("\\end{align*}"))







    doc.append(NoEscape("\\\\"))
    doc.append(NewPage())





# de meme pour la correction du niveau 2
    doc.append("Niveau 2 :")

    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\begin{cases}"))
    doc.append(NoEscape("\\  \\frac{%s}{%s}x + %sy &= %sy - %s \\\\" % (nb1, nb2, nb3, nb4, nb5)))
    doc.append(NoEscape("\\  %sx + %sy &= %sy + \\frac{%s}{%s} \\\\" % (nb6,nb7 ,nb8,nb9,nb10 )))
    doc.append(NoEscape("\\end{cases}"))
    doc.append(NoEscape("\\\\"))
    doc.append(NoEscape("\\end{align*}"))


    doc.append(NoEscape("\\ \\text{L'équation ligne 1 permet d'écrire :}\\\\" % ()))


    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\  \\Leftrightarrow  \\frac{%s}{%s}x + %sy - %sy &= %sy - %s - %sy \\\\" % (nb1, nb2, nb3,nb3, nb4, nb5,nb3)))

    new_y_1_nv2 = nb4-nb3
    doc.append(NoEscape("\\  \\Leftrightarrow  \\frac{%s}{%s}x &= %sy - %s \\\\" % (nb1, nb2, new_y_1_nv2, nb5)))

    doc.append(NoEscape("\\  \\Leftrightarrow  \\frac{%s}{%s}x \\times \\frac{%s}{%s} &= (%sy - %s) \\times \\frac{%s}{%s} \\\\" % (nb1, nb2,nb2,nb1, new_y_1_nv2, nb5,nb2,nb1)))    

    new_y_2_nv2 = round(new_y_1_nv2/(nb1/nb2),2)
    new_nb_1_nv2 = round(nb5/(nb1/nb2),2)
    doc.append(NoEscape("\\  \\Leftrightarrow  x &= %sy - %s\\\\" % (new_y_2_nv2,new_nb_1_nv2)))    
    doc.append(NoEscape("\\end{align*}"))
    


    doc.append(NoEscape("\\\\"))


    doc.append(NoEscape("\\ \\text{On remplace x par $%sy - %s$ dans l'équation 2}\\\\" % (new_y_2_nv2,new_nb_1_nv2)))



    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\ \\Leftrightarrow  %s(%sy - %s) + %sy &= %sy + \\frac{%s}{%s} \\\\" % (nb6,new_y_2_nv2,new_nb_1_nv2,nb7,nb8,nb9,nb10)))

    new_y_3_nv2 = round((nb6*new_y_2_nv2),3)
    new_nb_2_nv2 = round((nb6*new_nb_1_nv2),3)
    doc.append(NoEscape("\\ \\Leftrightarrow  %sy - %s + %sy &= %sy + \\frac{%s}{%s} \\\\" % (new_y_3_nv2,new_nb_2_nv2,nb7,nb8,nb9,nb10)))

    doc.append(NoEscape("\\ \\Leftrightarrow  %sy - %s +%s + %sy &= %sy + \\frac{%s}{%s} +%s \\\\" % (new_y_3_nv2,new_nb_2_nv2,new_nb_2_nv2,nb7,nb8,nb9,nb10,new_nb_2_nv2)))

    new_nb_4_nv2 = round(((nb9 / nb10) + new_nb_2_nv2),2)
    doc.append(NoEscape("\\ \\Leftrightarrow  %sy +%sy - %sy &= %sy -%sy + %s \\\\" % (new_y_3_nv2,nb7,nb8,nb8,nb8,new_nb_4_nv2)))

    new_y_4_nv2 = round(new_y_3_nv2 +nb7 - nb8,2)
    doc.append(NoEscape("\\ \\Leftrightarrow  %sy &= %s \\\\" % (new_y_4_nv2, new_nb_4_nv2)))

    doc.append(NoEscape("\\ \\Leftrightarrow  \\frac{%sy}{%s} &= \\frac{%s}{%s} \\\\" % (new_y_4_nv2,new_y_4_nv2, new_nb_4_nv2,new_y_4_nv2)))

    result_y_nv2 = round((new_nb_4_nv2/ new_y_4_nv2),2)
    doc.append(NoEscape("\\ \\Leftrightarrow y &\\approx %s \\\\" % (result_y_nv2)))
    doc.append(NoEscape("\\end{align*}"))


    doc.append(NoEscape("\\ \\text{En remplaçant y par la valeur obtenue dans l'équation 2 :}\\\\" % ()))


    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\  %sx + %s \\times %s &= %s \\times %s + \\frac{%s}{%s} \\\\" % (nb6,nb7, result_y_nv2 ,nb8,result_y_nv2,nb9,nb10 )))

    new_nb_5_nv2 = round((nb7*result_y_nv2),2)
    new_nb_6_nv2 = round((nb8 * result_y_nv2),2)
    doc.append(NoEscape("\\ \\Leftrightarrow %sx + %s - %s &= %s +\\frac{%s}{%s} -%s \\\\" % (nb6, new_nb_5_nv2, new_nb_5_nv2, new_nb_6_nv2,nb9,nb10, new_nb_5_nv2 )))

    new_nb_7_nv2 = round((new_nb_6_nv2 + (nb9/nb10)-new_nb_5_nv2),2)
    doc.append(NoEscape("\\ \\Leftrightarrow %sx &= %s \\\\" % (nb6, new_nb_7_nv2)))

    doc.append(NoEscape("\\ \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{%s}{%s} \\\\" % (nb6,nb6 ,new_nb_7_nv2,nb6)))

    result_x_nv_2 = round((new_nb_7_nv2/nb6),2)
    doc.append(NoEscape("\\ \\Leftrightarrow x &\\approx %s \\\\" % (result_x_nv_2)))
    doc.append(NoEscape("\\end{align*}"))



    doc.append(NoEscape("\\\\"))
    doc.append(NewPage())



# de meme pour la correction du niveau 3
    doc.append("Niveau 3 :")

    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\begin{cases}"))
    doc.append(NoEscape("\\  %s(%sy + %sx) &= %s \\\\" % (nb1_nv3, nb2_nv3,nb3_nv3, nb4_nv3)))
    doc.append(NoEscape("\\  %sx + %sy &= %s(%sy + %s) \\\\" % (nb5_nv3,nb6_nv3, nb7_nv3, nb8_nv3, nb9_nv3)))
    doc.append(NoEscape("\\end{cases}"))
    doc.append(NoEscape("\\\\"))
    doc.append(NoEscape("\\end{align*}"))


    doc.append(NoEscape("\\ \\text{L'équation ligne 1 permet d'écrire :}\\\\" % ()))


    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\  \\Leftrightarrow %s \\times %sy + %s \\times %sx &= %s \\\\" % (nb1_nv3, nb2_nv3,nb1_nv3,nb3_nv3, nb4_nv3)))

    new_y_1_nv1 = (nb1_nv3*nb2_nv3)
    new_x_1_nv3 = (nb1_nv3*nb3_nv3)
    doc.append(NoEscape("\\  \\Leftrightarrow %sy + %sx &= %s \\\\" % (new_y_1_nv1, new_x_1_nv3, nb4_nv3)))

    doc.append(NoEscape("\\  \\Leftrightarrow %sy - %sy + %sx &= %s - %sy \\\\" % (new_y_1_nv1, new_y_1_nv1, new_x_1_nv3, nb4_nv3, new_y_1_nv1)))

    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{%s - %sy}{%s} \\\\" % (new_x_1_nv3,new_x_1_nv3, nb4_nv3, new_y_1_nv1,new_x_1_nv3)))

    doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s - %sy}{%s} \\\\" % (nb4_nv3, new_y_1_nv1,new_x_1_nv3)))
    doc.append(NoEscape("\\end{align*}"))

    
    doc.append(NoEscape("\\\\"))


    doc.append(NoEscape("\\ \\text{On remplace x par $\\frac{%s - %sy}{%s}$ dans l'équation 2}\\\\" % (nb4_nv3, new_y_1_nv1,new_x_1_nv3)))

    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\ \\Leftrightarrow %s \\times \\frac{%s - %sy}{%s} + %sy &= %s \\times %sy + %s \\times %s \\\\" % (nb5_nv3,nb4_nv3, new_y_1_nv1,new_x_1_nv3,nb6_nv3, nb7_nv3,nb8_nv3 ,nb7_nv3, nb9_nv3)))
    
    new_y_2_nv3 = (nb7_nv3*nb8_nv3)
    new_nb_2_nv3 = (nb7_nv3*nb9_nv3)
    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s \\times (%s - %sy)}{%s} + %sy - %sy &= %sy - %sy + %s \\\\" % (nb5_nv3,nb4_nv3, new_y_1_nv1,new_x_1_nv3,nb6_nv3,new_y_2_nv3,new_y_2_nv3,new_y_2_nv3,new_nb_2_nv3)))

    new_nb_3_nv3 = (nb5_nv3*nb4_nv3)
    new_y_3_nv3 = (nb5_nv3*new_y_1_nv1)
    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s - %sy}{%s} + %sy - %sy &= %s \\\\" % (new_nb_3_nv3,new_y_3_nv3,new_x_1_nv3,nb6_nv3,new_y_2_nv3,new_nb_2_nv3)))

    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s} - \\frac{%sy}{%s} + %sy -%sy &= %s \\\\" % (new_nb_3_nv3,new_x_1_nv3,new_y_3_nv3,new_x_1_nv3,nb6_nv3,new_y_2_nv3,new_nb_2_nv3)))

    new_y_4_nv3 = round(((- new_y_3_nv3 / new_x_1_nv3) + nb6_nv3 - new_y_2_nv3),2)
    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s} - \\frac{%s}{%s} + %sy &= %s - \\frac{%s}{%s} \\\\" % (new_nb_3_nv3,new_x_1_nv3,new_nb_3_nv3,new_x_1_nv3,new_y_4_nv3, new_nb_2_nv3,new_nb_3_nv3,new_x_1_nv3)))

    new_nb_5_nv3 = round((new_nb_2_nv3 +(- new_nb_3_nv3 / new_x_1_nv3)),2)
    doc.append(NoEscape("\\  \\Leftrightarrow %sy &= %s \\\\" % (new_y_4_nv3, new_nb_5_nv3)))

    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%sy}{%s} &= \\frac{%s}{%s} \\\\" % (new_y_4_nv3,new_y_4_nv3,new_nb_5_nv3,new_y_4_nv3)))

    result_y_nv3 = round((new_nb_5_nv3 / new_y_4_nv3),2)
    doc.append(NoEscape("\\  \\Leftrightarrow y &\\approx %s \\\\" % (result_y_nv3)))
    doc.append(NoEscape("\\end{align*}"))


    doc.append(NoEscape("\\ \\text{En remplaçant y par la valeur obtenue dans l'équation 2 :}\\\\" % ()))


    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\  %s(%s \\times %s + %sx) &= %s \\\\" % (nb1_nv3, nb2_nv3,result_y_nv3 ,nb3_nv3, nb4_nv3)))

    new_nb_6_nv3 = round((nb2_nv3 * result_y_nv3),2)
    doc.append(NoEscape("\\  %s \\times %s + %s \\times %sx &= %s \\\\" % (nb1_nv3, new_nb_6_nv3,nb1_nv3 ,nb3_nv3, nb4_nv3)))

    new_nb_7_nv7 = round((nb1_nv3 * new_nb_6_nv3),2)
    new_x_2_nv3 = round((nb1_nv3*nb3_nv3),2)
    doc.append(NoEscape("\\  %s - (%s) +  %sx &= %s -(%s)\\\\" % (new_nb_7_nv7,new_nb_7_nv7,new_x_2_nv3, nb4_nv3,new_nb_7_nv7)))

    new_nb_8_nv3 = round((nb4_nv3 - new_nb_7_nv7),2)
    doc.append(NoEscape("\\  %sx &= %s\\\\" % (new_x_2_nv3,new_nb_8_nv3)))

    doc.append(NoEscape("\\  \\frac{%sx}{%s} &= \\frac{%s}{%s}\\\\" % (new_x_2_nv3,new_x_2_nv3,new_nb_8_nv3,new_x_2_nv3)))

    result_x_nv3 = round((new_nb_8_nv3 / new_x_2_nv3),2)
    doc.append(NoEscape("\\  x &\\approx %s\\\\" % (result_x_nv3)))
    doc.append(NoEscape("\\end{align*}"))


### FIN DE L'EXO ÉQUATION à 2 INCONNUES ###