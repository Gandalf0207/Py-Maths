from settings import *

from Poly2defFolder.Poly2degNv import ConsignesPoly2degNv, CorrectionsPoly2degNv

class Poly2deg(object):

    def __init__(self, doc, i, a, b, c) -> None:
        
        self.doc = doc
        self.i = i
        self.a = a
        self.b = b
        self.c = c

        # on définit la taille de l'écriture pour le document
        self.doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
        self.doc.append(pylatex.Command('selectfont'))

        self.consigne = ConsignesPoly2degNv(self.doc, self.i, self.a, self.b, self.c)
        self.correction = CorrectionsPoly2degNv(self.doc, self.i, self.a, self.b, self.c)

    def GestionAllExoPoly2deg(self):
        self.consigne.Poly2DegTitreConsigne()
        self.consigne.ConsigneAlpha(1)
        self.consigne.ConsigneBeta(2)
        self.consigne.ConsigneDelta(3)
        self.consigne.ConsigneSolutionsDelta(4)
        self.consigne.ConsigneFormeCanonique(5)
        self.consigne.ConsigneSommetS(6)
        self.consigne.ConsignePointA(7)
        self.consigne.ConsigneAllureCourbe(8)
        self.consigne.ConsigneTableauSignes(9)
        self.consigne.ConsigneTableauVariations(10)

        self.doc.append(NewPage())

        self.correction.Poly2DegTitreCorrection()
        self.correction.CorrectionAlpha(1)
        self.correction.CorrectionBeta(2)
        self.correction.CorrectionDelta(3)
        self.correction.CorrectionSolutionsDelta(4)
        self.correction.CorrectionFormeCanonique(5)
        self.correction.CorrectionSommetS(6)
        self.correction.CorrectionPointA(7)
        self.correction.CorrectionAllureCourbe(8)
        self.correction.CorrectionTableauSignes(9)
        self.correction.CorrectionTableauVariations(10)

        self.doc.append(NewPage())

# exo personnalisé
    def AddPoly2DegTitreConsigne(self):
        self.consigne.Poly2DegTitreConsigne()

    def AddConsigneAlpha(self, numEtape):
        self.consigne.ConsigneAlpha(numEtape) 

    def AddConsigneBeta(self, numEtape):
        self.consigne.ConsigneBeta(numEtape) 

    def AddConsigneDelta(self, numEtape):
        self.consigne.ConsigneDelta(numEtape)

    def AddConsigneSolutionsDelta(self, numEtape):
        self.consigne.ConsigneSolutionsDelta(numEtape)

    def AddConsigneFormeCanonique(self, numEtape):
        self.consigne.ConsigneFormeCanonique(numEtape)

    def AddConsigneSommetS(self, numEtape):
        self.consigne.ConsigneSommetS(numEtape)

    def AddConsignePointA(self, numEtape):
        self.consigne.ConsignePointA(numEtape)

    def AddConsigneAllureCourbe(self, numEtape):
        self.consigne.ConsigneAllureCourbe(numEtape)

    def AddConsigneTableauSignes(self, numEtape):
        self.consigne.ConsigneTableauSignes(numEtape)

    def AddConsigneTableauVariations(self, numEtape):
        self.consigne.ConsigneTableauVariations(numEtape)


# correction personnalisé
    def AddPoly2DegTitreCorrection(self):
        self.correction.Poly2DegTitreCorrection()

    def AddCorrectionAlpha(self, numEtape):
        self.correction.CorrectionAlpha(numEtape)

    def AddCorrectionBeta(self, numEtape):
        self.correction.CorrectionBeta(numEtape)

    def AddCorrectionDelta(self, numEtape):
        self.correction.CorrectionDelta(numEtape)

    def AddCorrectionSolutionsDelta(self, numEtape):
        self.correction.CorrectionSolutionsDelta(numEtape)

    def AddCorrectionFormeCanonique(self, numEtape):
        self.correction.CorrectionFormeCanonique(numEtape)

    def AddCorrectionSommetS(self, numEtape):
        self.correction.CorrectionSommetS(numEtape)

    def AddCorrectionPointA(self, numEtape):
        self.correction.CorrectionPointA(numEtape)

    def AddCorrectionAllureCourbe(self, numEtape):
        self.correction.CorrectionAllureCourbe(numEtape)

    def AddCorrectionTableauSignes(self, numEtape):
        self.correction.CorrectionTableauSignes(numEtape)

    def AddCorrectionTableauVariations(self, numEtape):
        self.correction.CorrectionTableauVariations(numEtape)
