### DÉBUT DE L'EXO ÉQUATION à 2 INCONNUES ###

## Importation des Librairies : 

from settings import *

class Eqt2Incs(object):
    def __init__(self, doc, nb1, nb2, nb3, nb4, nb5, nb6, i, choixNiveau) -> None:
        
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

    def Gestion(self):
        if self.choixNiveau == 1:
            self.CreateExoNv1()
            # On ajoute une page entre la correction et les exercices
            self.doc.append(NewPage())
            # correction
            self.CreateCorrectionNv1()

        elif self.choixNiveau == 2:
            self.CreateExoNv2()
            # On ajoute une page entre la correction et les exercices
            self.doc.append(NewPage())
            # correction
            self.CreateCorrectionNv2()

    def pgcd(self, a, b):
        # pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b
        while b != 0:
            a,b=b,a%b
        return a

    def CreateExoNv1(self):

        with self.doc.create(Section(f" Exo Équation à 2 inconnues n°{self.i+1}", numbering = False)):
                # pour chauque niveau on crée un environement avec la librairie amsmaths (latex) : begin{align*} et end{align*}
                # \\Leftrightarrow permet de mettre les doubles flêches
                # \\times pour les signes de multiplication
                # pour aligner tout les element entre eux (signes égales) et au pour les séparer on utilise '&' de la lib amsmath 
                # pour résoudre chaque équation on développe chaque étape dans la partie correction
                # on utilise le module 'cases' de latex pour générer le symbol d'acollade au débus pour la mise en page
            
                # l'element NoEscape permet d'écrire du code brute directement en dans le ficheir latex créé
            self.doc.append(NoEscape("\\ \\text{Pour chaque système d'équation ci-dessous; calculez la valeur (arrondie si nécéssaire) de $x$ et $y$}\\\\ " % ()))
            self.doc.append(NoEscape("\\\\"))

    # Niveau 1 exo
            self.doc.append("Niveau 1 :")
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\begin{cases}"))
            self.doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (self.nb1, self.nb2, self.nb5)))
            self.doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (self.nb3, self.nb4, self.nb6)))
            self.doc.append(NoEscape("\\end{cases}"))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))

    def CreateCorrectionNv1(self):
        
        with self.doc.create(Section(f"Correction Exo n°{self.i+1}", numbering = False)):
    # Niveau 1 correction
            self.doc.append("Niveau 1 :")
    # on redonne l'exercices
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\begin{cases}"))
        self.doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (self.nb1, self.nb2, self.nb5)))
        self.doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (self.nb3, self.nb4, self.nb6)))
        self.doc.append(NoEscape("\\end{cases}"))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))

    #puis on développe chaque étape avec un commentaire de ce que l'on fait
        #Etape 1 
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 1} : Multiplier chaque équation pour aligner les coefficients d'une variable. Pour aligner les coefficients de x, nous pouvons multiplier les deux équations pour obtenir le même coefficient de x. Par exemple, nous pouvons multiplier l'équation 1 par %s et l'équation 2 par %s: }" % (self.nb3,self.nb1)))

        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  %s \\times (%sx + %sy) &= %s \\times %s \\\\" % (self.nb3, self.nb1, self.nb2, self.nb5, self.nb3)))
        self.doc.append(NoEscape("\\  %s \\times (%sx + %sy) &= %s \\times %s \\\\" % (self.nb1, self.nb3, self.nb4, self.nb6, self.nb1)))
        self.doc.append(NoEscape("\\end{align*}"))

        newNb1 = self.nb3*self.nb1
        newNb2 = self.nb3*self.nb2
        newNb5 = self.nb3*self.nb5
        newNb3 = self.nb1*self.nb3
        newNb4 = self.nb1*self.nb4
        newNb6 = self.nb1*self.nb6
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (newNb1, newNb2, newNb5)))
        self.doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (newNb3, newNb4, newNb6)))
        self.doc.append(NoEscape("\\end{align*}"))

        #Etape 2 
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 2} : Soustraire les équations. En soustrayant l'équation 1 de l'équation 2, nous éliminons la variable x:}"))

        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ \\Leftrightarrow  (%sx + %sy) - (%sx + %sy) &= %s - %s\\\\" % (newNb1, newNb2, newNb3, newNb4, newNb5, newNb6)))
        newY = newNb2 - newNb4
        newValue = newNb5 - newNb6
        self.doc.append(NoEscape("\\ \\Leftrightarrow  %sy &= %s\\\\" % (newY, newValue)))
        self.doc.append(NoEscape("\\end{align*}"))

        #Etape 3 
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 3} : Résoudre pour y}"))
        division = self.pgcd(newValue, newY)
        newValue = newValue// division
        newY = newY // division

        self.doc.append(NoEscape("\\begin{align*}"))
        if newY ==1:
            self.doc.append(NoEscape("\\ \\Leftrightarrow  y  &= %s\\\\" % (newValue)))
        else:
            self.doc.append(NoEscape("\\ \\Leftrightarrow  y  &= \\frac{%s}{%s} \\\\" % (newValue, newY)))
        self.doc.append(NoEscape("\\end{align*}"))
        
        
        #Etape 4
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 4} : Substituer y dans l'une des équations d'origine pour résoudre pour x}"))

        self.doc.append(NoEscape("\\begin{align*}"))
        if newY ==1 : 
            self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx + %s &= %s\\\\" % (self.nb1, self.nb2, self.nb5)))
            self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx &= %s - %s\\\\" % (self.nb1, self.nb5, self.nb2)))
            newValue2 = self.nb5 - self.nb2
            self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= %s \\\\" % (self.nb1, newValue2)))
            division = self.pgcd(self.nb1, newValue2)
            newX = self.nb1 // division
            newValue2 = newValue2 // division

            if newX ==1:
                self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= %s \\\\" % (newValue2)))
            else:
                self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\\\" % (newValue2, newX)))
        else:
            self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx + %s \\times \\frac{%s}{%s} &= %s\\\\" % (self.nb1, self.nb2, newValue, newY, self.nb5)))
            newValue_ = self.nb2*newValue
            division = self.pgcd(newValue_, newY)
            newValue_ = newValue_// division
            newY_ = newY // division
            if newY_ ==1:
                self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx + %s &= %s\\\\" % (self.nb1, newValue_, self.nb5)))
                self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx &= %s - %s\\\\" % (self.nb1, self.nb5, newValue_)))
                newValue2 = self.nb5 - newValue_
                self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= %s \\\\" % (self.nb1, newValue2)))
                division = pgcd(self.nb1, newValue2)
                newX = self.nb1 // division
                newValue2 = newValue2 // division

                if newX ==1:
                    self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= %s \\\\" % (newValue2)))
                else:
                    self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\\\" % (newValue2, newX)))
            else:
                self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx + \\frac{%s}{%s}  &= %s\\\\" % (self.nb1, newValue_, newY_, self.nb5)))
                self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= %s - \\frac{%s}{%s}\\\\" % (self.nb1, self.nb5, newValue_, newY_)))
                newValue2 = newValue_ - self.nb5*newY_  
                division = self.pgcd(newValue2, newY_)
                newValue2 = newValue2// division
                newY_ = newY_ // division

                if newY_ ==1:
                    self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= %s \\\\" % (self.nb1, newValue2)))
                    division = self.pgcd(self.nb1, newValue2)
                    newX = self.nb1 // division
                    newValue2 = newValue2 // division

                    if newX ==1:
                        self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= %s \\\\" % (newValue2)))
                    else:
                        self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\\\" % (newValue2, newX)))
                else:
                    self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= \\frac{%s}{%s} \\\\" % (self.nb1, newValue2, newY_)))
                    self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\times \\frac{1}{%s} \\\\" % (newValue2, newY_, self.nb1)))
                    newX = newY_*self.nb1
                    division = self.pgcd(newValue2, newX)
                    newValue2 = newValue2// division
                    newX = newX // division

                    if newX ==1:
                        self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= %s \\\\" % (newValue2)))
                    else:
                        self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\\\" % (newValue2, newX))) 
        
        self.doc.append(NoEscape("\\end{align*}"))          

    def CreateExoNv2(self):
        pass

    def CreateCorrectionNv2(self):
        pass 

### Partis triviales sur les simplifications car jamais simplifiables, repasser plus tard


