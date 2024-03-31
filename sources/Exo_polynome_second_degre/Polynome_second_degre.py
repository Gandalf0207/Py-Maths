### FICHIER EXO SECOND DEGRE ###

## Importation des Librairies : 

# Module de création du Fichier Tex et convertion en pdf et autre
from pylatex import *
from pylatex.utils import *

#Modules de création, graphes, courbes.....
# backend_pdf est importé directement car il peut causer des problème de création des graphes sur une version pdf depuis un executable (.exe)
import matplotlib.backends.backend_pdf
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Modules de calcul...
import math
import random

# Modle de convertion / création des formules / la forme
import latexify
from sympy import *



#Fonction génération de l'exo
def write(doc, num_exo):

    #Avec sympy, définition du symbole pour le polynôme 
    x = Symbol('x')

    # Création des valeurs a, b, c de manière aléatoire 
    
    value_a = random.randint(0,1)
    if value_a == 0:
        a = random.randint(-25,-1)
    else:
        a = random.randint(1,25)
    b = random.randint(-25,25)
    c = random.randint(-25,25)

## Formation des différents élément nécéssaire au calcul 
## et aussi à l'affichage nécéssaire 
## Utilisation de latexify pour afficher correctement les éléments

    # Element polynôme
    @latexify.function
    def poly(a, b, c):
        return ((a*x**2) + (b*x) + c)

    poly_brute_formule = poly
    poly_formule = latex(poly(a,b,c))

    # Element alpha
    @latexify.function(use_math_symbols=True)
    def alpha(a, b):
        return (-b)/(2*a)

    Alpha_brute = alpha
    Alpha = round(alpha(a, b),2)

    # Element delta
    @latexify.function(use_math_symbols=True)
    def Delta(a, b, c):

        return (b**2)-(4*a*c)

    Delta_brute = Delta
    Delta = round(Delta(a, b, c),2)

    # Element beta
    @latexify.function(use_math_symbols=True)
    def Beta(Delta, a):
        return -Delta/(4*a)

    Beta_brute = Beta
    Beta = round(Beta(Delta, a),2)
    
    # Element solution de delta
    @latexify.expression(use_math_symbols=True)
    def Solution_Delta_sup0():
        x1 = (-b-sqrt(Delta))/(2*a)
        x2 = (-b+sqrt(Delta))/(2*a)
        return ''

     # le roud à 1 dixième est important sinon quand ce n'est pas exact, python calcul pas 
    x1 = round((-b-sqrt(Delta))/(2*a),2)
    x2 = round((-b+sqrt(Delta))/(2*a),2)

    @latexify.expression(use_math_symbols=True)
    def Solution_Delta_eg0():
       return 'x = α'

    @latexify.expression(use_math_symbols=True)
    def Solution_Delta_inf0():
        return ("Δ = Ø")



    # Element sommet S
    @latexify.function(use_math_symbols=True)
    def S(alpha, beta):
        return alpha, beta

    sommet_brute = S
    Sommet_S = S(Alpha, Beta)


    # Element point A
    @latexify.function(use_math_symbols=True)
    def A(f):
        return 0 ,f(0)

    point_A_brute = A
    f = lambda x:(a*x**2) + (b*x) + c
    point_A = A(f)


    # Element forme canonique (mise en page)
    @latexify.function(use_math_symbols=True)
    def f(x):
        return (a*(x-alpha)**2 + beta)

    Forme_canonique_brute = f

    # Element forme canonique
    def Forme_canonique(a, alpha, beta):
        return f"{a}(x - ({alpha}))² + ({beta})"

    forme_canonique = latex(Forme_canonique(a, Alpha, Beta))


## Ecriture de tout les éléments sur le pdf

    # Définitions de la taille de police d'écriture
    doc.append(pylatex.Command('fontsize', arguments = ['15', '12']))
    doc.append(pylatex.Command('selectfont'))

    #Numéro de l'exos
    with doc.create(Section(f'Exo Polynome du second degré n°{num_exo + 1}', numbering = False)):
        doc.append("Avec le Polynome qui vous est donné : ")
    
    #On donne le polynôme généré
    with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
            math_eq.append(poly_formule)

    #Affichage des consignes
    with doc.create(Section("Consignes", numbering=False)):
        with doc.create(Itemize()) as itemize:
            itemize.add_item("Trouver Alpha")
            itemize.add_item("Trouver Delta")
            itemize.add_item("Trouver Beta")
            itemize.add_item("Donner le(s) solution(s) possible de Delta")
            itemize.add_item("Déterminer la forme canonique")
            itemize.add_item("Déterminer le Sommet S")
            itemize.add_item("Déterminer le point A ayant pour abscisse 0")
            itemize.add_item("Représenter l'allure de la coube avec les deux points demandés")
            itemize.add_item("Dresser le tableau de signes de f")
            itemize.add_item("Dresser le tableau de variations de f")

    # On ajoute une page entre les consignes et la correction
    doc.append(NewPage())
    

    #Début de la correction de l'exo numéro...
    with doc.create(Section(f'Correction exo Polynome du second degré n°{num_exo + 1}', numbering = False)):
        doc.append("Rappel de ce qu'est un polynome du second degré")

    #Rappel de la formation d'un polynome du seconde degré
    with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
            math_eq.append(poly_brute_formule)

    #On redonne le polynôme étudié 
    with doc.create(Subsection("", numbering=False)):
        doc.append("Le polynome étudié")
    with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
            math_eq.append(poly_formule)

    #On affiche la forme brute et le résultat de Alpha
    with doc.create(Subsection("",numbering = False)):
        doc.append("Résolution de Alpha")
    with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
            math_eq.append(Alpha_brute)
    with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
            math_eq.append(Alpha)

    #On affiche la forme brute et le résultat de Delta
    with doc.create(Subsection("",numbering = False)):
        doc.append("Résolution de Delta")
    with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
            math_eq.append(Delta_brute)
    with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
            math_eq.append(Delta)

    #On affiche la forme brute et le résultat de Beta
    with doc.create(Subsection("",numbering = False)):
        doc.append("Résolution de Beta")
    with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
            math_eq.append(Beta_brute)
    with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
            math_eq.append(Beta)

    
    #On affiche la forme brute des solutions possible de Delta 
    with doc.create(Subsection("",numbering = False)):
        doc.append("Calcules des solutions potentielles de delta")

    #On affiche le(s) solution(s) e Delta

    with doc.create(Subsection("",numbering = False)):
        doc.append("Solution(s) : ")
    if Delta > 0:
        solution_delta_x1x2 = Solution_Delta_sup0
        with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
                math_eq.append(solution_delta_x1x2)
        doc.append(f'Les solutions sont : x1 = {x1}; x2 = {x2}')
    elif Delta ==0:
        solution_delta_eg0 = Solution_Delta_eg0
        with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
                math_eq.append(solution_delta_eg0)
        x = Alpha
        doc.append(f'La solution est : x = {x}')
    elif Delta < 0:
        solution_delta_inf0 = Solution_Delta_inf0
        with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
                math_eq.append(solution_delta_inf0)
        doc.append("Cette équation ne possède pas de solution dans R")

    
    #On affiche la forme brute et le résultat de la forme canonique du polynôme
    with doc.create(Subsection("",numbering = False)):
        doc.append("Détermination de la forme canonique")
    with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
            math_eq.append(Forme_canonique_brute)
            doc.append(Command('hspace', '2cm'))
            doc.append("f(x) = ")
            math_eq.append(forme_canonique)

    #On affiche la forme brute et le résultat du Sommet S de la courbe
    with doc.create(Subsection("", numbering=False)):
        doc.append("Détermination du sommet S : ")
    with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
        math_eq.append(sommet_brute)
    with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
            math_eq.append(Sommet_S)

    #On affiche la forme brute et le résultat du point A de la courbe avec comme abscisse 0
    with doc.create(Subsection("", numbering=False)):
        doc.append("Détermination du point A d'abscisse 0 : ")
    with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
        math_eq.append(point_A_brute)
    with doc.create(Alignat(numbering = False, escape = False)) as math_eq:
            math_eq.append(point_A)

    doc.append(NewPage())
    ## génération de la courbe avec Matplotlib ainsi que les deux points
    def courbe_poly(width, **kwargs):
        with doc.create(Subsection("", numbering=False)):
            doc.append("Représentation de la Fonction f(x) ainsi que les points demandé")
            with doc.create(Figure(position='htbp')) as plot:
                plot.add_plot(width=NoEscape(width))
                plt.close()
    

    def plot(func):
        plt.axvline(x=0, color ='r')
        plt.axhline(y=0, color ='r')   
        axes = plt.gca()
        axes.set_xlabel('x : abscisse')
        axes.set_ylabel('f(x) : ordonnée')

        x_point_S = Alpha
        y_point_S = Beta

        x = np.linspace(-x_point_S*5, x_point_S*5, 100)
        y = func(x)
        plt.plot(x, y, label="f(x)")

        plt.scatter(x_point_S, y_point_S, color='g',  label= f'S({x_point_S};{y_point_S})')  # Ajouter le point sur la courbe

        x_point_A = 0
        y_point_A = func(x_point_A)
        plt.scatter(x_point_A, y_point_A, color='black', label=f'A({x_point_A};{y_point_A})')  # Ajouter le point sur la courbe

        plt.legend(loc=0, fontsize=10)

    func = lambda x:(a*x**2) + (b*x) + c
    plot(func)

    courbe_poly(r'1\textwidth', dpi=300)

    #On affiche si a est supérieur ou inférieur à 0 et si delta est inférieur, suppérieur ou égale à 0
    with doc.create(Subsection("", numbering=False)):
        doc.append("Valeurs nécéssaire, pour déterminer les deux tableau suivants : ")
        doc.append(NewLine())
        if a > 0:
            if Delta < 0:
                doc.append('a > 0')
                doc.append(Command('hspace', '1cm'))
                doc.append('Δ < 0')
            elif Delta == 0:
                doc.append('a > 0')
                doc.append(Command('hspace', '1cm'))
                doc.append('Δ = 0')
            elif Delta > 0:
                doc.append('a > 0')
                doc.append(Command('hspace', '1cm'))
                doc.append('Δ > 0')
        elif a < 0:
            if Delta < 0:
                doc.append('a < 0')
                doc.append(Command('hspace', '1cm'))
                doc.append('Δ < 0')
            elif Delta == 0:
                doc.append('a < 0')
                doc.append(Command('hspace', '1cm'))
                doc.append('Δ = 0')
            elif Delta > 0:
                doc.append('a < 0')
                doc.append(Command('hspace', '1cm'))
                doc.append('Δ > 0')


    #On affiche les deux tableaux
    with doc.create(Subsection("", numbering=False)):

        #Tableau de signes
        doc.append('Tableau de Signes : ')
        doc.append(Command('hspace', '2cm'))
        if Delta > 0:
            doc.append(f"Rappel = x1 = {x1}; x2 = {x2}")
        elif Delta==0:
            doc.append(f"Rappel x = α = {Alpha}")
        elif Delta < 0:
            doc.append(f"Rappel : Δ n'a pas de solution en R")

        doc.append(NewLine())
        with doc.create(TikZ()):
            if a > 0:
                if Delta < 0:
                    doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $+ ∞$}"))
                    doc.append(NoEscape("\\tkzTabLine{, +}"))

                elif Delta == 0:
                    doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $α$, $+ ∞$}"))
                    doc.append(NoEscape("\\tkzTabLine{, +, z, +}"))
                    
                elif Delta > 0:
                    doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $x1$, $x2$, $+ ∞$}"))
                    doc.append(NoEscape("\\tkzTabLine{, +, z, -, z, +, }"))
            elif a < 0:
                if Delta < 0:
                    doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $+ ∞$}"))
                    doc.append(NoEscape("\\tkzTabLine{, -}"))

                elif Delta == 0:
                    doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $α$, $+ ∞$}"))
                    doc.append(NoEscape("\\tkzTabLine{, -, z, -}"))
                    
                elif Delta > 0:
                    doc.append(NoEscape("\\tkzTabInit{$-∞$ / 1, $f (x)$ / 1}{$- ∞$, $x1$, $x2$, $+ ∞$}"))
                    doc.append(NoEscape("\\tkzTabLine{, -, z, +, z, -, }"))

        doc.append(Command('vspace', '1cm'))
        doc.append(NewLine())

        #Tableau de variations
        doc.append('Tableau de Variations : ')

        doc.append(Command('hspace', '2cm'))
        doc.append(f"Rappel : α = {Alpha}; β = {Beta} ")

        doc.append(NewLine())
        with doc.create(TikZ()):
            if a > 0:
                doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $α$, $+ ∞$}"))
                doc.append(NoEscape("\\tkzTabVar{+/, -/ $β$, +/}"))
            elif a < 0:
                doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $α$, $+ ∞$}"))
                doc.append(NoEscape("\\tkzTabVar{-/, +/ $β$, -/}"))

                
### FIN DE L'EXO POLYNOME DU SECOND DEGRE