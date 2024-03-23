# Module de création du Fichier Tex et convertion en pdf et autre
from pylatex import *
from pylatex.utils import *

# Module de GUI de python
from tkinter import *

#Modules de création, graphes, courbes.....
# backend_pdf est importé directement car il peut causer des problème de création des graphes sur une version pdf depuis un executable (.exe)
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

# Importation des scripts pour les exercices
import Equation_premier_degre
import Polynome_second_degre
import Equation_2_inconnus

# Importation des scripts de mise en age et de gestions autre
import Hearder_Footer
import Contenue_Page_1


# Paramettres généraux de l'interface graphique
fenetre = Tk()
fenetre.title("Py-Maths : Générateur d'exercices")
fenetre.geometry("800x400")
bg = '#B3D1F0'
text = '#111645'
fenetre.config(bg = bg)


# Titre de l'interfae graphique avec son sous-titre
Label_TitrePage = Label(fenetre, text="Py-Maths", bg = bg, font=("Times New Roman", 20, "bold"), fg=text)
Label_textpage = Label(fenetre, text="Générateur d'exercices de mathématiques avec leurs corrections !", bg = bg, font=("Times New Roman", 15), fg='black')


def activation():

        # Gestion et suppression des fichiers .pdf pour un nettoyage complet
        fichier = glob.glob('./*.pdf')
        for supprimer in fichier:
                os.remove(supprimer)


        #Paramettres du pdf 
        geometry_options = {"head": "40pt",
                            "margin":"5mm",
                            "bottom": "0.6cm",
                            "includeheadfoot": True}
        doc = Document(geometry_options=geometry_options)

        # Spécification des librairie latex et caractère qui seront utilisés sous différents formes 
        doc.preamble.append(pylatex.Command('usepackage', 'newunicodechar'))
        doc.packages.append(NoEscape("\\usepackage{tkz-tab}"))
        doc.packages.append(NoEscape("\\usepackage{amsmath}"))
        doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{∞}{\ensuremath{\infty}}'))
        doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{Δ}{\ensuremath{\Delta}}'))
        doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{α}{\ensuremath{\alpha}}'))
        doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{β}{\ensuremath{\beta}}'))



        value_type_exo = CheckVar1.get()
        type_exo = ''
        if value_type_exo =='1':
                type_exo = 'Polynôme du second degre'
        if value_type_exo =="2":
                type_exo = 'Equation premier degre'
        if value_type_exo =='3':
                type_exo = 'Equation à 2 inconnus'
        
        nb_exo = CheckVar2.get()
            

        appel1 = Hearder_Footer.generate_header(doc, type_exo)
        appel2 = Contenue_Page_1.generate_contenue_p1(doc)
        doc.append(NewPage())
        
        for i in range(nb_exo):
                if value_type_exo =='1':
                        appel = Polynome_second_degre.write(doc, i)
                        doc.append(NewPage())

                elif value_type_exo =="2":
                        appel = Equation_premier_degre.write(doc, i)
                        doc.append(NewPage())

                elif value_type_exo=='3':
                        appel = Equation_2_inconnus.write(doc,i)
                        doc.append(NewPage())
                        



        doc.generate_pdf(f"Py-Maths_{type_exo}" , clean_tex=False, compiler="pdfLaTex")


        fichier = glob.glob('./*.tex')
        for supprimer in fichier:
            os.remove(supprimer)






Label_infos_nb = Label(fenetre, text="Choisissez le nombre d'exos que vous souhaitez :", borderwidth=0, bg = bg)
CheckVar2 = IntVar()
Label_nb = Entry(fenetre, textvariable=CheckVar2, width=5)


Label_infos_exos = Label(fenetre, text="Choisissez votre type d'exos :", borderwidth=0, bg = bg)
CheckVar1 = StringVar()
Label_box_exo = Label(fenetre, relief=GROOVE, borderwidth=0, bg = bg)

Label_btn_exo_poly2degre = Radiobutton(Label_box_exo, relief=GROOVE, text='Polynôme du second degré',variable=CheckVar1, value="1", borderwidth=0)
Label_btn_exo_Equation_Inéquation_premier_degre= Radiobutton(Label_box_exo, relief=GROOVE, text='Équation premier degre',variable=CheckVar1, value="2", borderwidth=0)
Label_btn_exo_Thalès = Radiobutton(Label_box_exo, relief=GROOVE, text='Équation à deux inconnues',variable=CheckVar1, value="3", borderwidth=0)


Label_btn_valider = Button(fenetre, text='Générer',borderwidth=1, command=activation)

Label_Credits = Label(fenetre, text="by Théo LUBAN & Quentin PLADEAU", bg = bg, borderwidth=0, font=("Times New Roman", 9,'italic'))



fenetre.columnconfigure(0, weight=1)
fenetre.columnconfigure(3, weight=1)

Label_TitrePage.grid(column= 1,row=0,columnspan=2, pady=5)
Label_textpage.grid(column= 1,row=1, columnspan=2, pady=5 )

Label_infos_nb.grid(column=1,row=2, sticky='NE', padx=5, pady=15)
Label_nb.grid(column=2,row=2,sticky='NW', pady=15)


Label_infos_exos.grid(column=1,row=3, sticky='NE' ,padx=5, pady=15)

Label_box_exo.grid(column=2, row=3 , sticky='NW', pady=15)
Label_btn_exo_poly2degre.grid(pady=2, sticky='W')
Label_btn_exo_Equation_Inéquation_premier_degre.grid(pady=2, sticky='W')
Label_btn_exo_Thalès.grid(pady=2, sticky='W')



Label_btn_valider.grid(column=1, columnspan=2 ,pady=25)
Label_Credits.grid( column=2, sticky='S', pady=15)

fenetre.mainloop()




### INFOS GÉNÉRALES

# Un fichier "Main.py" qui centralise toutes les actions
# Un fichier "nomexo.py" par exercice qui permet de générer de A à Z l'exercice
# Un fichier de page d'acceuil
# Un fichier d'entête et pied de page

# Nettoyage des fichiers généré : .tex et .pdf pour éviter les problème de place dans le lieu de création des fichiers
