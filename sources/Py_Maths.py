from Exo_Equation_deux_inconnues import Equation_2_inconnues

# Importation des scripts de mise en age et de gestions autre
from Module_Gestion import Hearder_Footer
from Module_Gestion import Contenue_Page_1

from settings import *


# Paramettres généraux de l'interface graphique
fenetre = Tk()
fenetre.title("Py-Maths : Générateur d'exercices")
fenetre.geometry("800x500")
bg = '#B3D1F0'
text = '#111645'
fenetre.config(bg = bg)


def activation():

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



        type_exo = 'Equation à 2 inconnus'
        
        # On recupère le nombre d'exos souhaités
        nb_exo = CheckVar2.get()
            
        # On fait appel au scripts qui permettent la mise en page
        appel1 = Hearder_Footer.generate_header(doc, type_exo)
        appel2 = Contenue_Page_1.generate_contenue_p1(doc)
        doc.append(NewPage())
        
        # On fait tourner la boucle pour générer le nombre d'exercices demandés en appelant à chaque fois le bon script
        for i in range(nb_exo):
                appel = Equation_2_inconnues.write(doc,i)
                doc.append(NewPage())
                        

        # création du fichier en .tex puis sans conversion en .pdf en spécifiant le compilateur, ici : pdf LaTaTex
        doc.generate_pdf(f"Py-Maths_{type_exo}" , clean_tex=False, compiler="pdfLaTex")



# Titre de l'interfae graphique avec son sous-titre
Label_TitrePage = Label(fenetre, text="Py-Maths", bg = bg, font=("Times New Roman", 20, "bold"), fg=text)
Label_textpage = Label(fenetre, text="Générateur d'exercices de mathématiques avec leurs corrections !", bg = bg, font=("Times New Roman", 15), fg='black')
Label_TitrePage.pack()
Label_textpage.pack()

# Création des elements du GUI
Label_infos_nb = Label(fenetre, text="Équation à deux inconnues, choisissez le nombre d'exo :", borderwidth=0, bg = bg)
Label_infos_nb.pack(padx=5, pady=5)
CheckVar2 = IntVar()
CheckVar2.set(1)


Label_nb = Entry(fenetre, textvariable=CheckVar2, width=5)
Label_nb.pack(pady=  5, padx =5)


Label_btn_exo_Thalès = Button(fenetre, relief=GROOVE, text='Générer', command=activation)
Label_btn_exo_Thalès.pack(pady=  5, padx =5)
textInfo = """
Py-Maths est un projet étudiant développé par deux élèves de Terminale NSI au lycée cette année.
Suite à la demande de Monsieur Escoute, nous avons repris au plus vite (délais de 12h) notre projet réalisé l'an passé.
(nommé au trophées NSI) pour que vous puissiez en profiter lors de ces vacances, et vous entraîner sur les systèmes 
d'équations à deux inconnus. Cette version est donc une version réduite et conçue expressément pour vous.
Pour plus de renseignements, n'hésitez pas à contacter M.Escoute. En vous souhaitant bon travail et bon courage ! "

Nous vous prions de bien vouloir excuser l'affichage donc rudimentaire dû au court délai...

Lien GitHub du projet : https://github.com/Gandalf0207/Py-Maths
"""
boxTexteInfo = Frame(fenetre, bg = None)
boxTexteInfo.pack(padx=0, pady=20)
titreTextInfo = Label(boxTexteInfo, text="Informations : ", anchor=NE, fg="red", font=("", 11, "bold"))
titreTextInfo.pack()
textInfoTempo = Label(boxTexteInfo,text= textInfo, width = 400, anchor=CENTER)
textInfoTempo.pack()

textCredits = """
by Théo LUBAN & Quentin PLADEAU
Py-Maths © Tous droits réservés
"""
Label_Credits = Label(fenetre, text=textCredits, bg = bg, borderwidth=0, font=("Times New Roman", 9,'italic'))
Label_Credits.pack(pady=  5, padx =5)


fenetre.mainloop()

