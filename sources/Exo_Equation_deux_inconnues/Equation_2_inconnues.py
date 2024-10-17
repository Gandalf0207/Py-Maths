### DÉBUT DE L'EXO ÉQUATION à 2 INCONNUES ###

## Importation des Librairies : 

from settings import *


def write(doc,i):

    def pgcd(a,b):
        # pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b
        while b != 0:
            a,b=b,a%b
        return a

    # on génère les valeurs aléatoirement pour avoir de nouveau exercices !
    nb1 = random.randint(1,50)
    nb2 = random.randint(1,50)
    nb3 = random.randint(1,50)
    nb4 = random.randint(1,50)
    nb5 = random.randint(1,50)
    nb6 = random.randint(1,50)

# on définit la taille de l'écriture pour le document
    doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
    doc.append(pylatex.Command('selectfont'))
    
    with doc.create(Section(f" Exo Équation à 2 inconnues n°{i+1}", numbering = False)):
            # pour chauque niveau on crée un environement avec la librairie amsmaths (latex) : begin{align*} et end{align*}
            # \\Leftrightarrow permet de mettre les doubles flêches
            # \\times pour les signes de multiplication
            # pour aligner tout les element entre eux (signes égales) et au pour les séparer on utilise '&' de la lib amsmath 
            # pour résoudre chaque équation on développe chaque étape dans la partie correction
            # on utilise le module 'cases' de latex pour générer le symbol d'acollade au débus pour la mise en page
        
            # l'element NoEscape permet d'écrire du code brute directement en dans le ficheir latex créé
        doc.append(NoEscape("\\ \\text{Pour chaque système d'équation ci-dessous; calculez la valeur (arrondie si nécéssaire) de $x$ et $y$}\\\\ " % ()))
        doc.append(NoEscape("\\\\"))

# Niveau 1 exo
        doc.append("Niveau 1 :")
        doc.append(NoEscape("\\begin{align*}"))
        doc.append(NoEscape("\\begin{cases}"))
        doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (nb1, nb2, nb5)))
        doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (nb3, nb4, nb6)))
        doc.append(NoEscape("\\end{cases}"))
        doc.append(NoEscape("\\\\"))
        doc.append(NoEscape("\\end{align*}"))


# On ajoute une page entre la correction et les exercices
    doc.append(NewPage())

    with doc.create(Section(f"Correction Exo n°{i+1}", numbering = False)):
# Niveau 1 correction
        doc.append("Niveau 1 :")
# on redonne l'exercices
    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\begin{cases}"))
    doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (nb1, nb2, nb5)))
    doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (nb3, nb4, nb6)))
    doc.append(NoEscape("\\end{cases}"))
    doc.append(NoEscape("\\\\"))
    doc.append(NoEscape("\\end{align*}"))

#puis on développe chaque étape avec un commentaire de ce que l'on fait
    #Etape 1 
    doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 1} : Multiplier chaque équation pour aligner les coefficients d'une variable. Pour aligner les coefficients de x, nous pouvons multiplier les deux équations pour obtenir le même coefficient de x. Par exemple, nous pouvons multiplier l'équation 1 par %s et l'équation 2 par %s: }" % (nb3,nb1)))

    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\  %s \\times (%sx + %sy) &= %s \\times %s \\\\" % (nb3, nb1, nb2, nb5, nb3)))
    doc.append(NoEscape("\\  %s \\times (%sx + %sy) &= %s \\times %s \\\\" % (nb1, nb3, nb4, nb6, nb1)))
    doc.append(NoEscape("\\end{align*}"))

    newNb1 = nb3*nb1
    newNb2 = nb3*nb2
    newNb5 = nb3*nb5
    newNb3 = nb1*nb3
    newNb4 = nb1*nb4
    newNb6 = nb1*nb6
    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (newNb1, newNb2, newNb5)))
    doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (newNb3, newNb4, newNb6)))
    doc.append(NoEscape("\\end{align*}"))

    #Etape 2 
    doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 2} : Soustraire les équations. En soustrayant l'équation 1 de l'équation 2, nous éliminons la variable x:}"))

    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\ \\Leftrightarrow  (%sx + %sy) - (%sx + %sy) &= %s - %s\\\\" % (newNb1, newNb2, newNb3, newNb4, newNb5, newNb6)))
    newY = newNb2 - newNb4
    newValue = newNb5 - newNb6
    doc.append(NoEscape("\\ \\Leftrightarrow  %sy &= %s\\\\" % (newY, newValue)))
    doc.append(NoEscape("\\end{align*}"))

    #Etape 3 
    doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 3} : Résoudre pour y}"))
    division = pgcd(newValue, newY)
    newValue = newValue// division
    newY = newY // division

    doc.append(NoEscape("\\begin{align*}"))
    if newY ==1:
        doc.append(NoEscape("\\ \\Leftrightarrow  y  &= %s\\\\" % (newValue)))
    else:
        doc.append(NoEscape("\\ \\Leftrightarrow  y  &= \\frac{%s}{%s} \\\\" % (newValue, newY)))
    doc.append(NoEscape("\\end{align*}"))
    
    
    #Etape 4
    doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 4} : Substituer y dans l'une des équations d'origine pour résoudre pour x}"))

    doc.append(NoEscape("\\begin{align*}"))
    if newY ==1 : 
        doc.append(NoEscape("\\ \\Leftrightarrow  %sx + %s &= %s\\\\" % (nb1, nb2, nb5)))
        doc.append(NoEscape("\\ \\Leftrightarrow  %sx &= %s - %s\\\\" % (nb1, nb5, nb2)))
        newValue2 = nb5 - nb2
        doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= %s \\\\" % (nb1, newValue2)))
        division = pgcd(nb1, newValue2)
        newX = nb1 // division
        newValue2 = newValue2 // division

        if newX ==1:
            doc.append(NoEscape("\\ \\Leftrightarrow  x  &= %s \\\\" % (newValue2)))
        else:
            doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\\\" % (newValue2, newX)))
    else:
        doc.append(NoEscape("\\ \\Leftrightarrow  %sx + %s \\times \\frac{%s}{%s} &= %s\\\\" % (nb1, nb2, newValue, newY, nb5)))
        newValue_ = nb2*newValue
        division = pgcd(newValue_, newY)
        newValue_ = newValue_// division
        newY_ = newY // division
        if newY_ ==1:
            doc.append(NoEscape("\\ \\Leftrightarrow  %sx + %s &= %s\\\\" % (nb1, newValue_, nb5)))
            doc.append(NoEscape("\\ \\Leftrightarrow  %sx &= %s - %s\\\\" % (nb1, nb5, newValue_)))
            newValue2 = nb5 - newValue_
            doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= %s \\\\" % (nb1, newValue2)))
            division = pgcd(nb1, newValue2)
            newX = nb1 // division
            newValue2 = newValue2 // division

            if newX ==1:
                doc.append(NoEscape("\\ \\Leftrightarrow  x  &= %s \\\\" % (newValue2)))
            else:
                doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\\\" % (newValue2, newX)))
        else:
            doc.append(NoEscape("\\ \\Leftrightarrow  %sx + \\frac{%s}{%s}  &= %s\\\\" % (nb1, newValue_, newY_, nb5)))
            doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= %s - \\frac{%s}{%s}\\\\" % (nb1, nb5, newValue_, newY_)))
            newValue2 = newValue_ - nb5*newY_  
            division = pgcd(newValue2, newY_)
            newValue2 = newValue2// division
            newY_ = newY_ // division

            if newY_ ==1:
                doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= %s \\\\" % (nb1, newValue2)))
                division = pgcd(nb1, newValue2)
                newX = nb1 // division
                newValue2 = newValue2 // division

                if newX ==1:
                    doc.append(NoEscape("\\ \\Leftrightarrow  x  &= %s \\\\" % (newValue2)))
                else:
                    doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\\\" % (newValue2, newX)))
            else:
                doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= \\frac{%s}{%s} \\\\" % (nb1, newValue2, newY_)))
                doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\times \\frac{1}{%s} \\\\" % (newValue2, newY_, nb1)))
                newX = newY_*nb1
                division = pgcd(newValue2, newX)
                newValue2 = newValue2// division
                newX = newX // division

                if newX ==1:
                    doc.append(NoEscape("\\ \\Leftrightarrow  x  &= %s \\\\" % (newValue2)))
                else:
                    doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\\\" % (newValue2, newX))) 
    
    doc.append(NoEscape("\\end{align*}"))          


### Partis triviales sur les simplifications car jamais simplifiables, repasser plus tard


