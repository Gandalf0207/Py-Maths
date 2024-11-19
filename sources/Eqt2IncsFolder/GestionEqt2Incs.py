### DÉBUT DE L'EXO ÉQUATION à 2 INCONNUES ###

## Importation des Librairies : 

from settings import *
from Eqt2IncsFolder.Eqt2IncsNv1 import Eqt2IncsNv1

class Eqt2Incs(object):
    def __init__(self, doc, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9, nb10, nb11, nb12, i, choixNiveau) -> None:
        
        self.doc = doc

        # on définit la taille de l'écriture pour le document
        self.doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
        self.doc.append(pylatex.Command('selectfont'))

        self.choixNiveau = choixNiveau
        self.i = i

        self.nb1 = nb1  
        self.nb2 = nb2  
        self.nb3 = nb3  
        self.nb4 = nb4  
        self.nb5 = nb5  
        self.nb6 = nb6  
        self.nb7 = nb7
        self.nb8 = nb8
        self.nb9 = nb9
        self.nb10 = nb10
        self.nb11 = nb11
        self.nb12 = nb12
        
    def Gestion(self):
        if self.choixNiveau == 1:
            Eqt2IncsNv1(self.doc, self.nb1, self.nb2, self.nb3, self.nb4, self.nb5, self.nb6, self.i).Setup()


        elif self.choixNiveau == 2:
            self.CreateExoNv2()
            # On ajoute une page entre la correction et les exercices
            self.doc.append(NewPage())
            # correction
            self.CreateCorrectionNv2()


    def CreateExoNv2(self):
        pass

    def CreateCorrectionNv2(self):
        pass 

### Partis triviales sur les simplifications car jamais simplifiables, repasser plus tard


