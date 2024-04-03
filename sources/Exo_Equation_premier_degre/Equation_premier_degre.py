### FIN DE L'EXO ÉQUATION DU PRÉMIER DEGRÉ ###

# Importation des librairies 

# Module de création du Fichier Tex et convertion en pdf et autre
from pylatex import *
from pylatex.utils import *

#Modules de calcul...
import math
import random

#Importation de toutes les equations (dans des fichiers différents pour une gestion plus simple)
from Exo_Equation_premier_degre.Fichiers_Equations import Nv1_1
from Exo_Equation_premier_degre.Fichiers_Equations import Nv1_2
from Exo_Equation_premier_degre.Fichiers_Equations import Nv1_3

def write(doc, num_exo):
   
    nb_value = 1
    nb1 = 15 #random.randint(2,20)
    nb2 = 14 #random.randint(2,20)
    nb3 = 5 #random.randint(2,20)
    nb4 =  18 #random.randint(2,20)
    nb5 = 8 #random.randint(2,20)
    nb6 = 12 #random.randint(2,20)

   # Définitions de la taille de police d'écriture
    doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
    doc.append(pylatex.Command('selectfont'))

    #Numéro de l'exos
    with doc.create(Section(f'Exo Equation du premier degré n°{num_exo + 1}', numbering = False)):
        doc.append("Pour chaque équation du premier degré suivante : Trouver la valeur de x ")
       
        # niveau 1
        with doc.create(Subsection("Equation niveau 1 : ", numbering = False)):
            Nv1_1.ligne_exo(doc,nb1,nb2,nb3,nb4,nb5,nb6,nb_value)
        # niveau 2
        with doc.create(Subsection("Equation niveau 2 : ", numbering = False)):
            Nv1_1.ligne_exo(doc,nb1,nb2,nb3,nb4,nb5,nb6,nb_value)       
        #niveau 3
        with doc.create(Subsection("Equation niveau 3 : ", numbering = False)):
            Nv1_1.ligne_exo(doc,nb1,nb2,nb3,nb4,nb5,nb6,nb_value)



    # On ajoute une page entre les consignes et la correction
    doc.append(NewPage())




    #correction des équations
    with doc.create(Section(f'Correction Exo Equation du premier degré n°{num_exo + 1}', numbering = False)):

        with doc.create(Subsection("Equations niveau 1", numbering = False)):

            # correction niveau 1
            Nv1_1.correction_exo(doc,nb1,nb2,nb3,nb4,nb5,nb6,nb_value)
            doc.append(NoEscape("\\\\"))            
            Nv1_1.correction_exo(doc,nb1,nb2,nb3,nb4,nb5,nb6,nb_value)





