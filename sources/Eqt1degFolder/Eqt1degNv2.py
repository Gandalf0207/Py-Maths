from settings import *

class Eqt1degNv2(object):
    def __init__(self, doc, nb1, nb2, nb3, nb4,nb5, nb6,  i) -> None:
        self.doc = doc
        self.i = i

        self.nb1 = nb1  
        self.nb2 = nb2  
        self.nb3 = nb3  
        self.nb4 = nb4  
        self.nb5 = nb5
        self.nb6 = nb6

    def pgcd(self, a,b):
        # pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b
        while b != 0:
            a,b=b,a%b
        return a

    def CreateExoEqt1degNv2(self):
        with self.doc.create(Section(f'Exo Equation du premier degré n°{self.i + 1}', numbering = False)):
            self.doc.append(NoEscape("\\ \\text{Trouver la valeur de $x$ dans cette équation du premier degré :}\\\\ " % ()))
            self.doc.append(NoEscape("\\\\"))

    # Niveau 1 exo
        self.doc.append("Niveau 2 :")
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s &= \\frac{%s}{%s} - %sx \\\\" % (self.nb1,self.nb2,self.nb3,self.nb4,self.nb5,self.nb6)))
        self.doc.append(NoEscape("\\end{align*}"))


    def CreateCorrectionEqt1degNv2(self):
        """Crée la correction détaillée pour l'équation."""

        with self.doc.create(Section(f"Correction Exo n°{self.i + 1}", numbering=False)):
            self.doc.append("Niveau 2 :")

            self.doc.append(NoEscape("\\text{L'équation donnée est : }"))
            
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s &= \\frac{%s}{%s} - %sx \\\\" % (self.nb1, self.nb2, self.nb3, self.nb4, self.nb5, self.nb6)))
            self.doc.append(NoEscape("\\end{align*}"))

        # Étape 1 : Simplification des fractions et dénominateur commun
        self.doc.append(NoEscape("\\textbf{Étape 1 : Simplification des fractions et mise au même dénominateur.}\\\\"))
        den_common = self.nb2 * self.nb5  # Dénominateur commun

        # Fractions simplifiées si nécessaire
        num1 = self.nb1 * self.nb5  # Ajustement des numérateurs pour dénominateur commun
        num2 = self.nb4 * self.nb2
        self.doc.append(NoEscape("\\text{Nous multiplions chaque terme par le dénominateur commun } %s \\text{ :}" % den_common))

        # Nouvelle équation après mise au dénominateur commun
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  \\Leftrightarrow %sx + %s \\cdot %s &= %s - %s \\cdot %sx \\\\" % (num1, self.nb3, den_common, num2, self.nb6, den_common)))
        num3 = self.nb3 * den_common  # Multiplication des termes constants
        num6 = self.nb6 * den_common
        self.doc.append(NoEscape("\\  \\Leftrightarrow %sx + %s &= %s - %sx \\\\" % (num1, num3, num2, num6)))
        self.doc.append(NoEscape("\\end{align*}"))

        # Étape 2 : Regroupement des termes
        self.doc.append(NoEscape("\\textbf{Étape 2 : Regroupement des termes en } x \\text{ d’un côté et les constantes de l’autre côté.}\\\\"))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  \\Leftrightarrow %sx + %sx &= %s - %s \\\\" % (num1, num6, num2, num3)))

        # Calcul des coefficients
        numx = num1 + num6
        num_const = num2 - num3
        self.doc.append(NoEscape("\\  \\Leftrightarrow %sx &= %s \\\\" % (numx, num_const)))
        self.doc.append(NoEscape("\\end{align*}"))

        # Étape 3 : Isolation de x
        self.doc.append(NoEscape("\\textbf{Étape 3 : Isolation de } x \\text{ en divisant par le coefficient.}\\\\"))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s}{%s} \\\\" % (num_const, numx)))

        # Simplification finale de la fraction
        gcd = self.pgcd(num_const, numx)
        num_const //= gcd
        numx //= gcd
        if numx == 1:
            self.doc.append(NoEscape("\\  \\Leftrightarrow x &= %s \\\\" % num_const))
        else:
            self.doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s}{%s} \\\\" % (num_const, numx)))
        self.doc.append(NoEscape("\\end{align*}"))


    def Setup(self):
        self.CreateExoEqt1degNv2()
        self.doc.append(NewPage())
        self.CreateCorrectionEqt1degNv2()
        self.doc.append(NewPage())


        