### FIN DE L'EXO ÉQUATION DU PRÉMIER DEGRÉ ###

# Importation des librairies 

# Module de création du Fichier Tex et convertion en pdf et autre
from settings import *

from Eqt1degFolder.Eqt1degNv1 import Eqt1degNv1
from Eqt1degFolder.Eqt1degNv2 import Eqt1degNv2

class Eqt1deg(object):
    def __init__(self, doc, nb1, nb2, nb3, nb4, nb5, nb6, i, choixNiveau) -> None:

        self.doc = doc

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



    def Gestion(self):
        if self.choixNiveau == 1:
            Eqt1degNv1(self.doc, self.nb1, self.nb2, self.nb3, self.nb4, self.i).Setup()

        elif self.choixNiveau == 2:
            Eqt1degNv2(self.doc, self.nb1, self.nb2, self.nb3, self.nb4,self.nb5, self.nb6, self.i).Setup()