from Eqt2IncsFolder.GestionEqt2Incs import *
from Eqt1degFolder.GestionEqt1deg import *
from Poly2defFolder.GestionPoly2deg import *

# Importation des scripts de mise en age et de gestions autre
from basePDF import *
from Module_Gestion import Contenue_Page_1

from settings import *

class GUI(object):
    def __init__(self) -> None:
        self.fenetre = Tk()
        self.fenetre.title("Py-Maths : Générateur d'exercices")
        self.fenetre.geometry("800x500")
        self.bg = '#B3D1F0'
        self.text = '#111645'
        self.fenetre.config(bg=self.bg)

        self.CheckVar2 = IntVar()
        self.CheckVar2.set(1)

    def choixExo(self):
        # Titre de l'interface graphique avec son sous-titre
        Label_TitrePage = Label(self.fenetre, text="Py-Maths", bg=self.bg, font=("Times New Roman", 20, "bold"), fg=self.text)
        Label_textpage = Label(self.fenetre, text="Générateur d'exercices de mathématiques avec leurs corrections !", bg=self.bg, font=("Times New Roman", 15), fg='black')
        Label_TitrePage.pack()
        Label_textpage.pack()

        # Élément d'entrée utilisateur
        Label_infos_nb = Label(self.fenetre, text="Choisissez le nombre d'exo et type d'exo :", borderwidth=0, bg=self.bg)
        Label_infos_nb.pack(padx=5, pady=5)


        Label_nb = Entry(self.fenetre, textvariable=self.CheckVar2, width=5)
        Label_nb.pack(pady=5, padx=5)

        # Bouton pour générer l'exercice
        Label_btn_exo_Thalès = Button(self.fenetre, relief=GROOVE, text='Générer', command=self.generate_pdf)
        Label_btn_exo_Thalès.pack(pady=5, padx=5)

        # Crédit
        textCredits = """
        by Théo LUBAN & Quentin PLADEAU
        Py-Maths © Tous droits réservés
        """
        Label_Credits = Label(self.fenetre, text=textCredits, bg=self.bg, borderwidth=0, font=("Times New Roman", 9, 'italic'))
        Label_Credits.pack(pady=5, padx=5)


    def getValue(self):
        return self.CheckVar2.get()

    def generate_pdf(self):
        generation_instance = Generation()
        generation_instance.BuildPDF()

    def Build(self):
        self.choixExo()
        self.fenetre.mainloop()


class Generation(object):
    def __init__(self) -> None:
        # Initialisation des paramètres du PDF
        geometry_options = {"head": "40pt", "margin": "5mm", "bottom": "0.6cm", "includeheadfoot": True}
        self.doc = Document(geometry_options=geometry_options)

        # Ajout des paquets nécessaires
        self.doc.preamble.append(pylatex.Command('usepackage', 'newunicodechar'))
        self.doc.packages.append(NoEscape("\\usepackage{tkz-tab}"))
        self.doc.packages.append(NoEscape("\\usepackage{placeins}"))
        self.doc.packages.append(NoEscape("\\usepackage{amsmath}"))
        self.doc.packages.append(NoEscape("\\usepackage[utf8]{inputenc}"))
        self.doc.packages.append(NoEscape("\\usepackage{enumitem}"))

        self.doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{∞}{\ensuremath{\infty}}'))
        self.doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{Δ}{\ensuremath{\Delta}}'))
        self.doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{α}{\ensuremath{\alpha}}'))
        self.doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{β}{\ensuremath{\beta}}'))


    def BuildPDF(self):

        def checkUniqueValuesList(liste):
            return len(liste) == len(set(liste)) # check de si toutes les valeurs sont uniques
        

        typeExo = "tttt"

        # Récupération du nombre d'exercices à générer
        nb_exo = int(GUI().getValue())

        # Ajout de l'en-tête et du contenu de la première page
        hp = HeaderFooter(self.doc, typeExo)
        hp.HeaderFooterPage()

        Contenue_Page_1.generate_contenue_p1(self.doc)
        self.doc.append(NewPage())

        # Génération des exercices
        for i in range(200):
            liste = []
            a = random.randint(-25,25)
            b = random.randint(-25,25)
            c = random.randint(-25,25)
            nb1 = random.randint(2,50)
            nb2 = random.randint(2,50)
            nb3 = random.randint(2,50)
            nb4 = random.randint(2,50)
            nb5 = random.randint(2,50)
            nb6 = random.randint(2,50)
            nb7 = random.randint(2,50)
            nb8 = random.randint(2,50)
            nb9 = random.randint(2,50)
            nb12 = random.randint(2,50)
            nb10 = random.randint(2,50)
            nb11 = random.randint(2,50)
        
            liste = [nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9, nb10, nb11, nb12]
            # liste = [a,b,c]

            while not checkUniqueValuesList(liste) or a ==0 or b == 0 or c==0:
                liste= []

                a = random.randint(-25,25)
                b = random.randint(-25,25)
                c = random.randint(-25,25)

                # liste = [a,b,c]


                nb1 = random.randint(2,50)
                nb2 = random.randint(2,50)
                nb3 = random.randint(2,50)
                nb4 = random.randint(2,50)
                nb5 = random.randint(2,50)
                nb6 = random.randint(2,50)
                nb7 = random.randint(2,50)
                nb8 = random.randint(2,50)
                nb9 = random.randint(2,50)
                nb12 = random.randint(2,50)
                nb10 = random.randint(2,50)
                nb11 = random.randint(2,50)
                liste = [nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9, nb10, nb11, nb12]

            # Equations 2 inconnus

            a  = Eqt2Incs(self.doc, i, 1, nb1, nb2, nb3, nb4, nb5, nb6,)
            # a.GestionAllExoEqt2Incs()
            a.AddTitreConsigneNv1()
            a.AddTitreConsigneNv2()
            self.doc.append(NewPage())
            a.AddTitreCorrectionNv1()
            a.AddTitreCorrectionNv2()
            self.doc.append(NewPage())

            # b = Eqt2Incs(self.doc, i, 2, nb7, nb8, nb9, nb10, nb11, nb12)
            # b.GestionAllExoEqt2Incs()

###
            # Equation 1 degré

            # a = Eqt1deg(self.doc, i, 1, nb1, nb2, nb3, nb4, nb5, nb6)
            # a.GestionAllExoEqt1deg()

            # a.AddTitreConsigneNv1()
            # a.AddTitreConsigneNv2()
            # self.doc.append(NewPage())
            # a.AddTitreCorrectionNv1()
            # a.AddTitreCorrectionNv2()
            # self.doc.append(NewPage())

            # b = Eqt1deg(self.doc, i, 2 ,nb1, nb2, nb3, nb4, nb5, nb6)
            # b.GestionAllExoEqt1deg()

####
            # Poly 2 degré

            # c = Poly2deg(self.doc,i, a, b, c )
            # c.GestionAllExoPoly2deg()
            # c.AddPoly2DegTitreConsigne()
            # c.AddConsigneAlpha(1)
            # c.AddConsigneTableauSignes(2)

            # self.doc.append(NewPage())

            # c.AddPoly2DegTitreCorrection()
            # c.AddCorrectionAlpha(1)
            # c.AddCorrectionTableauSignes(2)
            
            # self.doc.append(NewPage())


        # Création du fichier PDF
        self.doc.generate_pdf(f"Py-Maths_{typeExo}", clean_tex=False, compiler="pdfLaTex")


if __name__ == "__main__":
    GUI().Build()
