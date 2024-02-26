# Module de création du Fichier Tex et convertion en pdf et autre
from pylatex import *
from pylatex.utils import *

from tkinter import *

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

# importation du script pour les polynome du second degré
import Polynome_second_degre
import Hearder_Footer
import Contenue_Page_1
# import Hearder_Footer

fichier = glob.glob('./*.pdf')
for supprimer in fichier:
    os.remove(supprimer)


fenetre = Tk()
fenetre.title("Py-Maths : Générateur d'exercices")
fenetre.geometry("800x400")
bg = '#B3D1F0'
text = '#111645'
fenetre.config(bg = bg)



Label_TitrePage = Label(fenetre, text="Py-Maths", bg = bg, font=("Times New Roman", 20, "bold"), fg=text)
Label_textpage = Label(fenetre, text="Générateur d'exercices de mathématiques avec leurs correction !", bg = bg, font=("Times New Roman", 15), fg='black')


def activation():

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



        value_type_exo = CheckVar1.get()
        type_exo = ''
        if value_type_exo =='1':
                type_exo = 'Polynôme du second degré'
        
        nb_exo = CheckVar2.get()
            

        appel1 = Hearder_Footer.generate_header(doc, type_exo)
        appel2 = Contenue_Page_1.generate_contenue_p1(doc)
        doc.append(NewPage())
        
        for i in range(nb_exo):
            appel = Polynome_second_degre.write(doc, i)
            doc.append(NewPage())



        doc.generate_pdf(f"Py-Maths_{type_exo}" , clean_tex=False, compiler="pdfLaTex")


        fichier = glob.glob('./*.tex')
        for supprimer in fichier:
            os.remove(supprimer)






Label_infos_nb = Label(fenetre, text="Choisissez le nombre d'exos que vous souhaitez :", borderwidth=0, bg = bg)
CheckVar2 = IntVar()
Label_nb = Entry(fenetre, textvariable=CheckVar2, width=5)


Label_infos_exos = Label(fenetre, text="Choisissez votre type d'exercices :", borderwidth=0, bg = bg)
CheckVar1 = StringVar()
Label_box_exo = Label(fenetre, relief=GROOVE, borderwidth=0, bg = bg)

Label_btn_exo_poly2degre = Radiobutton(Label_box_exo, relief=GROOVE, text='Polynôme du second degré',variable=CheckVar1, value="1", borderwidth=0)
Label_btn_exo_Pythagore= Radiobutton(Label_box_exo, relief=GROOVE, text='Pythagore',variable=CheckVar1, value="Pythagore", borderwidth=0)
Label_btn_exo_Thalès = Radiobutton(Label_box_exo, relief=GROOVE, text='Thalès',variable=CheckVar1, value="Thalès", borderwidth=0)


Label_btn_valider = Button(fenetre, text='Générer',borderwidth=1, command=activation)




fenetre.columnconfigure(0, weight=1)
fenetre.columnconfigure(3, weight=1)

Label_TitrePage.grid(column= 1,row=0,columnspan=2, pady=5)
Label_textpage.grid(column= 1,row=1, columnspan=2, pady=5 )

Label_infos_nb.grid(column=1,row=2, sticky='NE', padx=5, pady=15)
Label_nb.grid(column=2,row=2,sticky='NW', pady=15)


Label_infos_exos.grid(column=1,row=3, sticky='NE' ,padx=5, pady=15)

Label_box_exo.grid(column=2, row=3 , sticky='NW', pady=15)
Label_btn_exo_poly2degre.grid(pady=2, sticky='W')
Label_btn_exo_Pythagore.grid(pady=2, sticky='W')
Label_btn_exo_Thalès.grid(pady=2, sticky='W')



Label_btn_valider.grid(column=1, columnspan=2 ,pady=25)

fenetre.mainloop()






    
# un fichier pasr type d'exos qui gère l'exo
# un ficheir main 
# un fichier latex .py qui gère tout le back
# un fichier qui gere tout le front

# crédits Mattis
# https://stackoverflow.com/questions/48898660/mathematics-in-latex-using-python

# import fonction d'un autre fichier
# print(main.testfunction())
