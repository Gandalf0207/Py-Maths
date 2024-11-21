from settings import *

from Poly2defFolder.Poly2degNv import Poly2degNv

class Poly2deg(object):

    def __init__(self, doc, i, a, b, c) -> None:
        
        self.doc = doc

        self.a = a
        self.b = b
        self.c = c

        # on définit la taille de l'écriture pour le document
        self.doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
        self.doc.append(pylatex.Command('selectfont'))

        self.i = i


        
    def Gestion(self):
        Poly2degNv(self.doc,self.a, self.b, self.c, self.i).Setup()