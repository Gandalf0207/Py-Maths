# Module de création du Fichier Tex et convertion en pdf et autre
from pylatex import *
from pylatex.utils import *

from tkinter import *
#Modules de création, graphe, courbe.....
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

# importation du script pour les polynome du second degré
import Polynome_second_degre
import Hearder_Footer
import Contenue_Page_1
# import Hearder_Footer

fenetre = Tk()

def activation():


    if __name__ == '__main__':

        geometry_options = {"head": "40pt",
                            "margin":"1cm",
                            "bottom": "0.6cm",
                            "includeheadfoot": True}
        doc = Document(geometry_options=geometry_options)

        doc.preamble.append(pylatex.Command('usepackage', 'newunicodechar'))
        doc.packages.append(NoEscape("\\usepackage{tkz-tab}"))
        doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{∞}{\ensuremath{\infty}}'))
        doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{Δ}{\ensuremath{\Delta}}'))
        doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{α}{\ensuremath{\alpha}}'))
        doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{β}{\ensuremath{\beta}}'))


        # a = int(input('exo poly = 1:'))
        # nb_exo = int(input("Le nombre d'exo voulu : "))
        # if a ==1:
        type_exo = 'Polynome du Second degré'
        nb_exo = 4
        
        appel1 = Hearder_Footer.generate_header(doc, type_exo)
        appel2 = Contenue_Page_1.generate_contenue_p1(doc)
        doc.append(NewPage())

        for i in range(nb_exo):
            # if a ==1:
            appel = Polynome_second_degre.write(doc, i)
            doc.append(NewPage())



        doc.generate_pdf(f"Python-Maths_{type_exo}" , clean_tex=False, compiler="pdfLaTex")


# fichier = glob.glob('./*.tex')
# for supprimer in fichier:
#     os.remove(supprimer)











laveb_bouton = Button(fenetre, text='generation1exo', command=activation) 
laveb_bouton.pack()

fenetre.mainloop()






    
# un fichier pasr type d'exos qui gère l'exo
# un ficheir main 
# un fichier latex .py qui gère tout le back
# un fichier qui gere tout le front

# crédits Mattis
# https://stackoverflow.com/questions/48898660/mathematics-in-latex-using-python

# import fonction d'un autre fichier
# print(main.testfunction())
