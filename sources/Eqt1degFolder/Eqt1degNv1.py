from settings import *

class Eqt1degNv1(object):
    def __init__(self, doc, nb1, nb2, nb3, nb4, i) -> None:
        self.doc = doc
        self.i = i

        self.nb1 = nb1  
        self.nb2 = nb2  
        self.nb3 = nb3  
        self.nb4 = nb4  


    def pgcd(self, a, b):
        # pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b
        while b != 0:
            a,b=b,a%b
        return a   

    def CreateExoEqt1degNv1(self):
        with self.doc.create(Section(f'Exo Equation du premier degré n°{self.i + 1}', numbering = False)):
            self.doc.append(NoEscape("\\ \\text{Trouver la valeur de $x$ dans cette équation du premier degré :}\\\\ " % ()))
            self.doc.append(NoEscape("\\\\"))

    # Niveau 1 exo
            self.doc.append("Niveau 1 :")
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\  \\Leftrightarrow %sx - %s &= %s + %sx \\\\" % (self.nb1, self.nb2, self.nb3, self.nb4)))
            self.doc.append(NoEscape("\\end{align*}"))


    def CreateCorrectionEqt1degNv1(self):
        with self.doc.create(Section(f"Correction Exo n°{self.i+1}", numbering = False)):
        # Niveau 1 correction
            self.doc.append("Niveau 1 :")

        self.doc.append(NoEscape("\\ \\text{L'équation à résoudre est : } " % ()))

        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  \\Leftrightarrow %sx - %s &= %s + %sx \\\\" % (self.nb1,self.nb2,self.nb3,self.nb4)))
        self.doc.append(NoEscape("\\end{align*}"))


        # Etape 1
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 1} : Regroupons les termes contenant la variable x d’un côté de l’équation et les termes constants de l’autre côté. Retirons %sx des deux côtés et ajoutons %s des deux côtés également : }" % (self.nb4,self.nb2)))

        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  \\Leftrightarrow %sx - %s + %s -%sx &= %s + %sx -%sx +%s \\\\" % (self.nb1,self.nb2,self.nb3,self.nb4,self.nb3,self.nb4,self.nb4,self.nb2)))
        nb = self.nb3 + self.nb2
        nbx = self.nb1 - self.nb4

        if nbx != 1:
            self.doc.append(NoEscape("\\  \\Leftrightarrow %sx &= %s \\\\" % (nbx,nb)))
            self.doc.append(NoEscape("\\end{align*}"))
        else:
            self.doc.append(NoEscape("\\  \\Leftrightarrow x &= %s \\\\" % (nb)))
            self.doc.append(NoEscape("\\end{align*}"))



        # Etape 2 
        #que si x != 0

        if nbx != 1:
            self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 2} : Divisons les deux côtés de l’équation par %s pour isoler x et simplifions: }" % (nbx)))

            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{%s}{%s} \\\\" % (nbx,nbx,nb,nbx)))
            pgcd_frac3 = self.pgcd(nb,nbx)
            nb = nb//pgcd_frac3
            nbx = nbx//pgcd_frac3
            
            if nbx !=1:
                self.doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s}{%s} \\\\" % (nb,nbx)))
                self.doc.append(NoEscape("\\end{align*}"))
            else:
                self.doc.append(NoEscape("\\  \\Leftrightarrow x &= %s \\\\" % (nb)))
                self.doc.append(NoEscape("\\end{align*}"))      


    def Setup(self):
        self.CreateExoEqt1degNv1()
        self.doc.append(NewPage())
        self.CreateCorrectionEqt1degNv1()
        self.doc.append(NewPage())



        