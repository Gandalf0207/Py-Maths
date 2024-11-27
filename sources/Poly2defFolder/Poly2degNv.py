### FICHIER EXO SECOND DEGRE ###

from settings import *

class Poly2degNv(object):
    def __init__(self, doc, a, b, c, i) -> None:
        
        self.doc = doc

        self.a = a
        self.b = b
        self.c = c

        self.i = i

    def pgcd(self, a, b):
        # pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b
        while b != 0:
            a,b=b,a%b
        return a

    def WritePoly(self, element = "x"):
        self.doc.append(NoEscape("\\begin{align*}"))
        if self.b < 0 or self.c < 0:
            if self.b < 0 and self.c < 0:
                self.doc.append(NoEscape("\\ f(%s) =  %s%s^2  %s%s  %s \\\\" % (element, self.a, element, self.b, element, self.c)))
            elif self.b < 0:
                self.doc.append(NoEscape("\\ f(%s) =  %s%s^2  %s%s + %s \\\\" % (element, self.a, element, self.b, element, self.c)))
            else:
                self.doc.append(NoEscape("\\ f(%s) =  %s%s^2 + %s%s  %s \\\\" % (element, self.a, element, self.b, element, self.c)))
        else:
            self.doc.append(NoEscape("\\ f(%s) =  %s%s^2 + %s%s + %s \\\\" % (element, self.a, element, self.b, element, self.c)))

        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))

    def SimplificationDeltaRacines(self, num, den):
        num = num
        den = den

        if isinstance(num, int) and isinstance(den, int):
            # Trouver le plus grand commun diviseur (PGCD)
            facteur_commun = gcd(int(num), den)
            num //= facteur_commun
            den //= facteur_commun
    
        # Retour sous forme de fraction lisible
        return num, den

    def CreateExoPoly2degNv(self):
        with self.doc.create(Section(f" Exo Polynôme du second degré n°{self.i+1}", numbering = False)):
                # pour chauque niveau on crée un environement avec la librairie amsmaths (latex) : begin{align*} et end{align*}
                # \\Leftrightarrow permet de mettre les doubles flêches
                # \\times pour les signes de multiplication
                # pour aligner tout les element entre eux (signes égales) et au pour les séparer on utilise '&' de la lib amsmath 
                # pour résoudre chaque équation on développe chaque étape dans la partie correction
                # on utilise le module 'cases' de latex pour générer le symbol d'acollade au débus pour la mise en page
            
                # l'element NoEscape permet d'écrire du code brute directement en dans le ficheir latex créé
            self.doc.append(NoEscape("\\ \\text{A l'aide de cette fonction polynôme du second degré, répondez aux questions suivantes :}\\\\ "))
            self.doc.append(NoEscape("\\\\"))

            self.WritePoly()

            self.doc.append(NoEscape("\\ 1. Donner la valeur de α \\\\"))            
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\ 2. Calculer la valeur de Δ \\\\"))            
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\ 3. Déduire la valeur de  β \\\\"))            
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\ 4. Trouver la/les solution(s) possible de Δ \\\\"))            
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\ 5. Déterminer la forme canonique \\\\"))            
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\ 6. Déterminer le Sommet S \\\\"))            
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\ 7. Déterminer le point A ayant pour abscisse 0 \\\\"))            
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\ 8. Représenter l'allure de la coube avec les deux points demandés \\\\"))            
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\ 9. Dresser le tableau de signes de f(x) \\\\"))            
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\ 10. Dresser le tableau de variations de f(x) \\\\"))            
            self.doc.append(NoEscape("\\\\"))


    def CreateCorrectionPolyNv(self):
        with self.doc.create(Section(f'Correction Exo Polynome du second degré n°{self.i + 1}', numbering = False)):
            self.doc.append(NoEscape("\\ \\text{Le polynome étudié} \\\\"))
            self.doc.append(NoEscape("\\\\"))

            self.WritePoly()

        # alpha value
            self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 1 : Donner la valeur de α } \\\\ La valeur de α est calculée avec cette formule :}"))
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\ α = - \\frac{ b }{ 2 \\cdot a } \\\\"))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))  

            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant : }}"))
            self.doc.append(NoEscape("\\begin{align*}"))  
            self.doc.append(NoEscape("\\ α &=  \\frac{- (%s)}{2 \\cdot (%s)} \\\\" % (self.b, self.a)))

            numAlpha = -self.b
            denAlpha = 2*self.a
            division = self.pgcd(numAlpha, denAlpha)
            numAlpha = numAlpha // division
            denAlpha = denAlpha // division

            if denAlpha == 1:
                self.doc.append(NoEscape("\\ α &= %s \\\\"%(numAlpha)))
            else:
                self.doc.append(NoEscape("\\ α &= \\frac{%s}{%s} \\\\" % (numAlpha, denAlpha)))

            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))  


        #calcul delta
            self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 2 : Valeur de Δ } \\\\ La formule du discriminant est :}"))
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\ Δ = b^2 - 4 \\cdot a \\cdot c \\\\"))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))

            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{Ici $a$ = %s, $b$ = %s, $c$ = %s. Calculons : }}" % (self.a, self.b, self.c)))
            self.doc.append(NoEscape("\\begin{align*}"))
            deltaValue = self.b**2 - 4*self.a*self.c
            self.doc.append(NoEscape("\\ Δ &= (%s)^2 - 4 \\cdot (%s) \\cdot (%s) \\\\" % (self.b, self.a, self.c)))
            self.doc.append(NoEscape("\\ Δ &= %s \\\\" % (deltaValue)))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))


        # # beta value
            self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 3 : Donner la valeur de β } \\\\ La valeur de β est calculée avec cette formule :}"))
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\ β = f(α)  \\\\"))
            self.doc.append(NoEscape("\\end{align*}"))
            self.WritePoly("α")


            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{Calculons : }}"))
            if denAlpha == 1:
                if self.b < 0 or self.c < 0:
                    if self.b < 0 and self.c < 0:
                        self.doc.append(NoEscape("\\begin{align*}"))
                        self.doc.append(NoEscape("\\ β =  %s \\cdot (%s)^2  %s \\cdot (%s)  %s \\\\" % (self.a, numAlpha, self.b, numAlpha, self.c)))
                        self.doc.append(NoEscape("\\\\"))
                        self.doc.append(NoEscape("\\end{align*}"))
                    elif self.b < 0:
                        self.doc.append(NoEscape("\\begin{align*}"))
                        self.doc.append(NoEscape("\\ β =  %s \\cdot (%s)^2  %s \\cdot (%s) + %s \\\\" % (self.a, numAlpha, self.b, numAlpha, self.c)))
                        self.doc.append(NoEscape("\\\\"))
                        self.doc.append(NoEscape("\\end{align*}"))
                    else:
                        self.doc.append(NoEscape("\\begin{align*}"))
                        self.doc.append(NoEscape("\\ β =  %s \\cdot (%s)^2 + %s \\cdot (%s)  %s \\\\" % (self.a, numAlpha, self.b, numAlpha, self.c)))
                        self.doc.append(NoEscape("\\\\"))
                        self.doc.append(NoEscape("\\end{align*}"))
                else:
                    self.doc.append(NoEscape("\\begin{align*}"))
                    self.doc.append(NoEscape("\\ β =  %s \\cdot (%s)^2 + %s \\cdot (%s) + %s \\\\" % (self.a, numAlpha, self.b, numAlpha, self.c)))
                    self.doc.append(NoEscape("\\\\"))
            else:
                if self.b < 0 or self.c < 0:
                    if self.b < 0 and self.c < 0:
                        self.doc.append(NoEscape("\\begin{align*}"))
                        self.doc.append(NoEscape("\\ β =  %s \\cdot (\\frac{%s}{%s})^2  %s \\cdot (\\frac{%s}{%s})  %s \\\\" % (self.a, numAlpha, denAlpha, self.b, numAlpha, denAlpha, self.c)))
                        self.doc.append(NoEscape("\\\\"))
                        self.doc.append(NoEscape("\\end{align*}"))
                    elif self.b < 0:
                        self.doc.append(NoEscape("\\begin{align*}"))
                        self.doc.append(NoEscape("\\ β =  %s \\cdot (\\frac{%s}{%s})^2  %s \\cdot (\\frac{%s}{%s}) + %s \\\\" % (self.a, numAlpha, denAlpha, self.b, numAlpha, denAlpha, self.c)))
                        self.doc.append(NoEscape("\\\\"))
                        self.doc.append(NoEscape("\\end{align*}"))
                    else:
                        self.doc.append(NoEscape("\\begin{align*}"))
                        self.doc.append(NoEscape("\\ β =  %s \\cdot (\\frac{%s}{%s})^2 + %s \\cdot (\\frac{%s}{%s})  %s \\\\" % (self.a, numAlpha, denAlpha, self.b, numAlpha, denAlpha, self.c)))
                        self.doc.append(NoEscape("\\\\"))
                        self.doc.append(NoEscape("\\end{align*}"))
                else:
                    self.doc.append(NoEscape("\\begin{align*}"))
                    self.doc.append(NoEscape("\\ β =  %s \\cdot (\\frac{%s}{%s})^2 + %s \\cdot (\\frac{%s}{%s}) + %s \\\\" % (self.a, numAlpha, denAlpha, self.b, numAlpha, denAlpha, self.c)))
                    self.doc.append(NoEscape("\\\\"))


            self.doc.append(NoEscape("\\begin{align*}"))
            # ne pas oublier de soustraire la fraction à la valeur de c
            numBeta = self.c * 4*self.a - self.b**2  
            denBeta = 4*self.a
            division = self.pgcd(numBeta, denBeta)
            numBeta = numBeta // division
            denBeta = denBeta // division

            if denBeta ==1 : 
                self.doc.append(NoEscape("\\ β = %s \\\\" % (self.c - denBeta)))
            else:
                self.doc.append(NoEscape("\\ β = \\frac{%s}{%s}\\\\" % (numBeta, denBeta)))

            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))       


        # solus delta
            self.doc.append(NoEscape("\\parbox{ 450pt }{\\textbf{Etape 4 : Trouver la/les solution(s) possible(s) de Δ} \\\\ Les solutions dépendent de la valeur de Δ :}"))
            self.doc.append(NoEscape("{\\renewcommand{\\labelitemi}{\\textbullet}"))
            self.doc.append(NoEscape("\\begin{itemize}"))
            self.doc.append(NoEscape("\\item $\\text{Si Δ > 0, il y a deux solutions réelles distinctes.}$"))
            self.doc.append(NoEscape("\\item $\\text{Si Δ = 0, il y a une solution réelle unique (racine double).}$"))
            self.doc.append(NoEscape("\\item $\\text{Si Δ < 0, il n'y a pas de solution réelle, mais deux solutions complexes.}$"))
            self.doc.append(NoEscape("\\end{itemize}"))
            self.doc.append(NoEscape("\\ }"))  # Ferme la redéfinition temporaire de labelitemi
            self.doc.append(NoEscape("  \\\\"))


            # terminer delta    
            if deltaValue > 0:
                self.doc.append(NoEscape("\\ \\parbox{ 450pt }{Ici Δ > 0, donc il y a \\textbf{deux solutions réelles distinctes} données par : }"))
                self.doc.append(NoEscape("\\begin{align*}"))            
                self.doc.append(NoEscape("\\ x1 = \\frac{-b - \\sqrt{Δ} }{2 \\cdot a}  ,  x2 = \\frac{-b + \\sqrt{Δ} }{2 \\cdot a} \\\\ "))
                self.doc.append(NoEscape("\\\\"))
                self.doc.append(NoEscape("\\end{align*}"))  
                
                self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\text{Calculons :}}"))
                self.doc.append(NoEscape("\\begin{align*}"))

                # x1
                num, den = self.SimplificationDeltaRacines(-self.b - sqrt(deltaValue), 2 * self.a)
                x1Value = num / den
                if den == 1:            
                    self.doc.append(NoEscape("\\ x1 = \\frac{-(%s) - \\sqrt{%s} }{2 \\cdot %s}  &=  %s \\\\" % (self.b, deltaValue, self.a, num)))
                elif abs(x1Value - round(x1Value, 2)) < 1e-10:
                    self.doc.append(NoEscape("\\ x1 = \\frac{-(%s) - \\sqrt{%s} }{2 \\cdot %s}  &=  %s \\\\" % (self.b, deltaValue, self.a, round(x1Value, 2))))
                else: 
                    self.doc.append(NoEscape("\\ x1 = \\frac{-(%s) - \\sqrt{%s} }{2 \\cdot %s}  &\\approx  \\frac{%s}{%s} \\\\" % (self.b, deltaValue, self.a, round(float(num),2), round(float(den),2))))

                # x2
                num2, den2 = self.SimplificationDeltaRacines(-self.b + sqrt(deltaValue), 2 * self.a)
                x2Value = num2 / den2
                if den2 == 1:            
                    self.doc.append(NoEscape("\\ x2 = \\frac{-(%s) + \\sqrt{%s} }{2 \\cdot %s}  &=  %s \\\\" % (self.b, deltaValue, self.a, num2)))
                elif abs(x2Value - round(x2Value, 2)) < 1e-10:
                    self.doc.append(NoEscape("\\ x2 = \\frac{-(%s) + \\sqrt{%s} }{2 \\cdot %s}  &=  %s \\\\" % (self.b, deltaValue, self.a, round(x2Value, 2))))
                else: 
                    self.doc.append(NoEscape("\\ x2 = \\frac{-(%s) + \\sqrt{%s} }{2 \\cdot %s}  &\\approx  \\frac{%s}{%s} \\\\" % (self.b, deltaValue, self.a, round(float(num2),2), round(float(den2),2))))

                self.doc.append(NoEscape("\\\\"))
                self.doc.append(NoEscape("\\end{align*}"))

            elif deltaValue == 0:
                self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ Ici Δ = 0, donc il y a \\textbf{une solution réelle unique (racine double)} données par : }"))

                self.doc.append(NoEscape("\\begin{align*}"))            
                self.doc.append(NoEscape("\\ x = \\frac{-b}{2 \\codt a} \\\\ "))
                self.doc.append(NoEscape("\\\\"))
                self.doc.append(NoEscape("\\end{align*}"))  

                self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\text{Calculons :}}"))
                self.doc.append(NoEscape("\\begin{align*}"))

                num, den = self.SimplificationDeltaRacines(-self.b, 2 * self.a)
                x1Value = num / den
                if den == 1:            
                    self.doc.append(NoEscape("\\ x = \\frac{-(%s)}{2 \\cdot %s}  &=  %s \\\\" % (self.b, self.a, num)))
                elif abs(x1Value - round(x1Value, 2)) < 1e-10:
                    self.doc.append(NoEscape("\\ x = \\frac{-(%s)}{2 \\cdot %s}  &=  %s \\\\" % (self.b, self.a, round(x1Value, 2))))
                else: 
                    self.doc.append(NoEscape("\\ x = \\frac{-(%s) }{2 \\cdot %s}  &\\approx  \\frac{%s}{%s} \\\\" % (self.b, self.a, round(float(num),2), round(float(den),2))))

            else:
                self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ Ici Δ < 0, donc il n'y a \\textbf{aucune solution réelle}}"))

                self.doc.append(NoEscape("\\begin{align*}"))            
                self.doc.append(NoEscape("\\ x = \\emptyset \\\\ "))
                self.doc.append(NoEscape("\\\\"))
                self.doc.append(NoEscape("\\end{align*}"))




        # forme canonique
            self.doc.append(NoEscape("\\parbox{ 450pt }{\\textbf{Etape 5 : Déterminer la forme canonique} \\\\ La forme canonique d’un polynôme est donnée par :}"))
            self.doc.append(NoEscape("\\begin{align*}"))            
            self.doc.append(NoEscape("\\ f(x) = a(x - α)^2 + β \\\\"))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))


            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{Ainsi, la forme canonique est :}}"))
            self.doc.append(NoEscape("\\begin{align*}"))
            if denAlpha == 1 or denBeta == 1:
                if denAlpha == 1 and denBeta == 1:
                    self.doc.append(NoEscape("\\ f(x) = %s(x - (%s))^2 + (%s) \\\\" % (self.a, numAlpha, numBeta)))
                elif denBeta == 1 :
                    self.doc.append(NoEscape("\\ f(x) = %s(x - \\frac{%s}{%s})^2 + (%s) \\\\" % (self.a, numAlpha,denAlpha, numBeta)))
                elif denAlpha == 1 :
                    self.doc.append(NoEscape("\\ f(x) = %s(x - (%s))^2 + \\frac{%s}{%s} \\\\" % (self.a, numAlpha, numBeta, denBeta)))
            else:
                self.doc.append(NoEscape("\\ f(x) = %s(x - \\frac{%s}{%s})^2 + \\frac{%s}{%s} \\\\" % (self.a, numAlpha, denAlpha, numBeta, denBeta)))

            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}")) 

        # sommet S
            self.doc.append(NoEscape("\\parbox{ 450pt }{\\textbf{Etape 6 : Déterminer le sommet $S$} \\\\ Le sommet $S$ est donné par les coordonnées (α,β).}"))
            self.doc.append(NoEscape("\\begin{align*}"))    
            if denAlpha == 1 or denBeta == 1:
                if denAlpha == 1 and denBeta == 1:
                    self.doc.append(NoEscape("\\ S = (%s, %s) \\\\" % (numAlpha, numBeta)))
                elif denBeta == 1 :
                    self.doc.append(NoEscape("\\ S = (\\frac{%s}{%s}, %s) \\\\" % (numAlpha,denAlpha, numBeta)))
                elif denAlpha == 1 :
                    self.doc.append(NoEscape("\\ S = (%s, \\frac{%s}{%s}) \\\\" % (numAlpha, numBeta, denBeta)))
            else:
                self.doc.append(NoEscape("\\ S = (\\frac{%s}{%s}, \\frac{%s}{%s}) \\\\" % (numAlpha, denAlpha, numBeta, denBeta)))

            self.doc.append(NoEscape("\\\\"))
            self.Scoord = (round(numAlpha/denAlpha, 2), round(numBeta/denBeta, 2))
            self.doc.append(NoEscape("\\end{align*}"))

        # point A
            self.doc.append(NoEscape("\\parbox{ 450pt }{\\textbf{Etape 7 : Déterminer le spoint $A$ ayant pour abscisse 0} \\\\ Pour $x$ = 0, calculons $f(0)$.}"))
            self.doc.append(NoEscape("\\begin{align*}"))
            if self.b < 0 or self.c < 0:
                if self.b < 0 and self.c < 0:
                    self.doc.append(NoEscape("\\ f(0) &=  %s \\cdot 0^2  %s \\cdot 0  %s \\\\" % (self.a, self.b, self.c)))
                elif self.b < 0:
                    self.doc.append(NoEscape("\\ f(0) &=  %s \\cdot 0^2  %s \\cdot 0 + %s \\\\" % (self.a, self.b, self.c)))
                else:
                    self.doc.append(NoEscape("\\ f(0) &=  %s \\cdot 0^2 + %s \\cdot 0  %s \\\\" % (self.a, self.b, self.c)))
            else:
                self.doc.append(NoEscape("\\ f(0) &=  %s \\cdot 0^2 + %s \\cdot 0 + %s \\\\" % (self.a, self.b, self.c)))

            self.doc.append(NoEscape("\\ f(0) &= %s \\\\" %(self.c) )) # self.c car les autres éléments s'annulent en 0
            self.Acoord = (0, self.c)
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))
            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{Ainsi, le point $A$ est (0,%s):}}"% (self.c)))
            self.doc.append(NoEscape("\\\\"))



        # allure courbe avec les 2 pts
            courbe = CourbeRepresentation(self.doc, self.a, self.b, self.c, self.Scoord, self.Acoord)
            courbe.generate_graph()
            courbe.courbe_poly(width=r'1\textwidth', dpi=300)


        # tableau de signe de f(x)
            self.doc.append(NoEscape("\\parbox{ 450pt }{\\textbf{Question 1 : Déterminer le tableau de signes de $f(x)$} \\\\ Les signes de $f(x)$ sont calculés en fonction des valeurs de $a$ et $\\Delta$.}"))
            self.doc.append(NoEscape("\\begin{align*}"))


    def Setup(self):
        self.CreateExoPoly2degNv()
        self.doc.append(NewPage())
        self.CreateCorrectionPolyNv()
        self.doc.append(NewPage())

        
#------------------------------------------------------------------------------------


    # #On affiche si a est supérieur ou inférieur à 0 et si delta est inférieur, suppérieur ou égale à 0
    # with doc.create(Subsection("", numbering=False)):
    #     doc.append("Valeurs nécéssaire, pour déterminer les deux tableau suivants : ")
    #     doc.append(NewLine())
    #     if a > 0:
    #         if Delta < 0:
    #             doc.append('a > 0')
    #             doc.append(Command('hspace', '1cm'))
    #             doc.append('Δ < 0')
    #         elif Delta == 0:
    #             doc.append('a > 0')
    #             doc.append(Command('hspace', '1cm'))
    #             doc.append('Δ = 0')
    #         elif Delta > 0:
    #             doc.append('a > 0')
    #             doc.append(Command('hspace', '1cm'))
    #             doc.append('Δ > 0')
    #     elif a < 0:
    #         if Delta < 0:
    #             doc.append('a < 0')
    #             doc.append(Command('hspace', '1cm'))
    #             doc.append('Δ < 0')
    #         elif Delta == 0:
    #             doc.append('a < 0')
    #             doc.append(Command('hspace', '1cm'))
    #             doc.append('Δ = 0')
    #         elif Delta > 0:
    #             doc.append('a < 0')
    #             doc.append(Command('hspace', '1cm'))
    #             doc.append('Δ > 0')


    # #On affiche les deux tableaux
    # with doc.create(Subsection("", numbering=False)):

    #     #Tableau de signes
    #     doc.append('Tableau de Signes : ')
    #     doc.append(Command('hspace', '2cm'))
    #     if Delta > 0:
    #         doc.append(f"Rappel = x1 = {x1}; x2 = {x2}")
    #     elif Delta==0:
    #         doc.append(f"Rappel x = α = {Alpha}")
    #     elif Delta < 0:
    #         doc.append(f"Rappel : Δ n'a pas de solution en R")

    #     doc.append(NewLine())
    #     with doc.create(TikZ()):
    #         if a > 0:
    #             if Delta < 0:
    #                 doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $+ ∞$}"))
    #                 doc.append(NoEscape("\\tkzTabLine{, +}"))

    #             elif Delta == 0:
    #                 doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $α$, $+ ∞$}"))
    #                 doc.append(NoEscape("\\tkzTabLine{, +, z, +}"))
                    
    #             elif Delta > 0:
    #                 doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $x1$, $x2$, $+ ∞$}"))
    #                 doc.append(NoEscape("\\tkzTabLine{, +, z, -, z, +, }"))
    #         elif a < 0:
    #             if Delta < 0:
    #                 doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $+ ∞$}"))
    #                 doc.append(NoEscape("\\tkzTabLine{, -}"))

    #             elif Delta == 0:
    #                 doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $α$, $+ ∞$}"))
    #                 doc.append(NoEscape("\\tkzTabLine{, -, z, -}"))
                    
    #             elif Delta > 0:
    #                 doc.append(NoEscape("\\tkzTabInit{$-∞$ / 1, $f (x)$ / 1}{$- ∞$, $x1$, $x2$, $+ ∞$}"))
    #                 doc.append(NoEscape("\\tkzTabLine{, -, z, +, z, -, }"))

    #     doc.append(Command('vspace', '1cm'))
    #     doc.append(NewLine())

    #     #Tableau de variations
    #     doc.append('Tableau de Variations : ')

    #     doc.append(Command('hspace', '2cm'))
    #     doc.append(f"Rappel : α = {Alpha}; β = {Beta} ")

    #     doc.append(NewLine())
    #     with doc.create(TikZ()):
    #         if a > 0:
    #             doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $α$, $+ ∞$}"))
    #             doc.append(NoEscape("\\tkzTabVar{+/, -/ $β$, +/}"))
    #         elif a < 0:
    #             doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $α$, $+ ∞$}"))
    #             doc.append(NoEscape("\\tkzTabVar{-/, +/ $β$, -/}"))



class CourbeRepresentation(object):
    def __init__(self, doc, a, b, c, Scoord, Acoord):
        self.doc = doc
        self.a = a
        self.b = b
        self.c = c
        self.Scoord = Scoord
        self.Acoord = Acoord

    def courbe_poly(self, width, dpi=300):
        """
        Ajout de la représentation graphique de la fonction avec description
        dans le document latex / pdf.
        """
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\parbox{ 450pt }{\\textbf{Etape 8 : Représenter l’allure de la courbe avec les deux points demandés} \\\\ On représente la parabole $f(x)$ avec les points $S$ (sommet) et $A$}."))

        # Ajout du graphique
        with self.doc.create(Figure(position='htbp')) as plot:
            plot.add_plot(width=NoEscape(width), dpi=dpi)

    def plot(self, func):
        """
        Création du graphique avec matplotlib.
        """

        plt.axvline(x=0, color='r')
        plt.axhline(y=0, color='r')
        axes = plt.gca()
        axes.set_xlabel('x : abscisse')
        axes.set_ylabel('f(x) : ordonnée')

        # Coordonnées des points
        x_point_S = self.Scoord[0]
        y_point_S = self.Scoord[1]
        x_point_A = self.Acoord[0]
        y_point_A = self.Acoord[1]

        # Tracé de la courbe
        x = np.linspace(-x_point_S * 5, x_point_S * 5, 100)
        y = func(x)
        plt.plot(x, y, label="f(x)")

        # Ajout des points sur la courbe
        plt.scatter(x_point_S, y_point_S, color='g', label=f'S({x_point_S}; {y_point_S})')
        plt.scatter(x_point_A, y_point_A, color='black', label=f'A({x_point_A}; {y_point_A})')

        # Légende
        plt.legend(loc=0, fontsize=10)

    def generate_graph(self):
        """
        Génère et affiche le graphique à partir des coefficients donnés.
        """
        func = lambda x: (self.a * x**2) + (self.b * x) + self.c
        self.plot(func)