# import settings

from settings import *

class VolumesNv1(object):
    """Class parent de l'exercice de calcul de volume. Contient des méthodes utilisés globalement.
    Permet de gérer plus facilement des apples et la création des exercices.
    
        Input : 
            doc -> pdf latex
            a -> int, valeur 5,25 
            b -> int, valeur 25,50 
            r -> int, valeur 4, 12 
            d -> int, valeur 6, 32
            L -> int, valeur 8, 34
            l -> int, valeur 7, 23 
            h -> int, valrur 3, 45

        Output : / """

    def __init__(self, doc, a, b, r, d, L, l, h) -> None:
        """Initialisation des attribbuts de la class parent de l'exercie Volumes"""

        self.doc = doc # pdf latex
        self.a = a # coef nb
        self.b = b # coef nb
        self.r = r # coef nb
        self.d = d # coef nb
        self.L = L # coef nb
        self.l = l # coef nb
        self.h = h # coef nb

    def __pgcd__(self, a, b) -> int:
        """ Méthode pgcd, permet de calculer le plus grand diviseur comment entre deux nombres. Utiliser pour créer des fractions iréductibles.
            Input : 
                a -> nombre entier 
                b -> nombre entier
            Output : a -> nombre entier """

        while b != 0:
            a,b=b,a%b
        return a # retour du pgcd


class ConsignesVolumesNv1(VolumesNv1):
    """Class enfant contenant toutes la méthode pour pouvoir écrire les consignes
    
        Input : 
            doc -> pdf latex
            i -> int numéro de l'exercice
            a -> int, valeur 5,25 
            b -> int, valeur 25,50 
            r -> int, valeur 4, 12 
            L -> int, valeur 8, 34
            l -> int, valeur 7, 23 
            h -> int, valrur 3, 45

        Output : / """
    

    def __init__(self, i, doc, a, b, r, d, L, l, h) -> None:
        """Initialisation des attributs de la class enfant consignes, de l'exerccie volumes."""

        super().__init__(doc, a, b, r, d, L, l, h)
        self.i = i # nunméro de l'exercice

    def VolumesNv1Consignes(self) -> None:
        """Méthode d'écriture du titre des consignes
        Input  : /    
        Output : /"""

        with self.doc.create(Section(f"Exo Volumes n°{self.i+1}", numbering=False)): #titre de l'exo
            self.doc.append(NoEscape("\\ \\text{A l'aide des valeurs données, veuillez calculer l'aire ou le volume demandé. Une valeur exacte et arrondie au dixième vous est demandée.} \\\\")) # consigne générale
            self.doc.append(NoEscape("\\\\"))

    def ConsigneVCube(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer le volume d'un cube.
        Input : numéro de l'étape
        Output : /"""

        self.doc.append(NoEscape("\\ %s. Calculer le volume d'un cube de côté : c = %sm" % (numEtape, self.a)))
        self.doc.append(NoEscape("\\\\"))

    def ConsigneVSphere(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer le volume d'une sphère.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer le volume d'une sphère de rayon : r = %sm" % (numEtape, self.r)))
        self.doc.append(NoEscape("\\\\"))

    def ConsigneVCone(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer le volume d'un cône.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer le volume d'un cône de hauteur et de diametre de base: h = %sm ; d = %sm" % (numEtape, self.h, self.d)))
        self.doc.append(NoEscape("\\\\"))

    def ConsigneVCylindre(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer le volume d'un cylindre.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer le volume d'un cylindre de hauteur et de rayon de base: h = %sm ; r = %sm" % (numEtape, self.h, self.r)))
        self.doc.append(NoEscape("\\\\"))   

    def ConsigneVPaveDroit(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer le volume d'un pavé droit.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer le volume d'un pavé droit de Longueur et de largeur: L = %sm ; l = %sm" % (numEtape, self.L, self.l)))
        self.doc.append(NoEscape("\\\\"))   

    def ConsigneVPyramideBaseCarre(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer le volume d'une pyramide à base carré.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer le volume d'une pyramide à base carré de côté de base et hauter: c = %sm ; h = %sm" % (numEtape, self.b, self.h)))
        self.doc.append(NoEscape("\\\\"))  

    def ConsigneADisque(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer l'aire d'un disque.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer l'aire d'un disque de diametre:  d = %sm" % (numEtape, self.d)))
        self.doc.append(NoEscape("\\\\"))

    def ConsigneATriangleRectangle(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer l'aire triangle rectangle.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer l'aire d'un triangle rectangle (ABC) en A de côté : AB = %sm; AC = %sm" % (numEtape, self.a, self.b)))
        self.doc.append(NoEscape("\\\\"))   

    def ConsigneARectangle(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer l'aire d'un rectangle.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer l'aire d'un rectangle : L = %sm; l = %sm" % (numEtape, self.L, self.l)))
        self.doc.append(NoEscape("\\\\"))


class CorrectionVolumesNv1(VolumesNv1):
    """Class enfant contentant toutes les méthodes pour pouvoir écrire les corrections et calculer les valeurs
    
      Input : 
        doc -> pdf latex
        i -> int numéro de l'exercice
        a -> int, valeur 5,25 
        b -> int, valeur 25,50 
        r -> int, valeur 4, 12 
        L -> int, valeur 8, 34
        l -> int, valeur 7, 23 
        h -> int, valrur 3, 45

    Output : / """
    

    def __init__(self, doc, i, a, b, r, d, L, l, h) -> None:
        """Initialisation des attributs de la class enfant correction, de l'exercice volumes"""
        
        super().__init__(doc, a, b, r, d, L, l, h)
        self.i = i # numéro exo

        self.VCube = None
        self.VSphere = None
        self.VCone = None
        self.VCylindre = None
        self.VPaveDroit = None
        self.VPyramideBaseCarre = None
        self.ADisque = None
        self.ATriangleRectangle = None
        self.ARectangle = None

        self.__AllCalculs__()

    def __AllCalculs__(self) -> None:
        """Méthode de calcculs afin de pouvoirs écrire toutes les corrections.
        Input : /
        Output : / """

        
        self.VCube = self.a**3
        self.VSphere = 4/3*pi*self.r**3
        self.VCone = 1/3 * self.h * pi* (self.d/2)**2
        self.VCylindre = pi * self.h*self.r**2
        self.VPaveDroit = self.L * self.L * self.h
        self.VPyramideBaseCarre =  (self.b**2 * self.h )/ 3
        self.ADisque = pi * (self.d / 2)**2
        self.ATriangleRectangle = (self.a * self.b) / 2
        self.ARectangle = self.L * self.L


    def VolumesTitreCorrection(self) -> None:
        """Méthode d'écriture du titre des corrections
        Input : / 
        Output : / """

        with self.doc.create(Section(f"Correction Exo Volumes n°{self.i + 1}", numbering=False)) # titre exp correction
            self.doc.append(NoEscape("\\\\"))

    def CorrectionVCube(self, numEtape) -> None:
        """Méthode d'écriture de la correction pour : """

        pass