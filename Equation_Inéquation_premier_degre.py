# Module de création du Fichier Tex et convertion en pdf et autre
from pylatex import *
from pylatex.utils import *

#Modules de création, g raphe, courbe.....
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

#Module de gestion fichier sur la machine
import os
import glob



def write(doc, num_exo):

    #Avec sympy, définition du symbole pour le polynôme 
    x = Symbol('x')


    nb1 = random.randint(-50,50)
    nb2 = random.randint(-50,50)

    value_nbx1 = random.randint(0,1)
    value_nbx2 = random.randint(0,1)

    if value_nbx1 == 0:
        nbx1 = random.randint(-25,-1)
    else:
        nbx1 = random.randint(1,25)

    if value_nbx2 == 0:
        nbx2= random.randint(-25,-1)
    else:
        nbx2 = random.randint(1,25)

    Eq = fr"{nb1} + {nbx1}*x = {nb2} - {nbx2}*x"
    # aaa = f"{nb1} + {nbx1}",*x,f"{nb2} - {nbx2}",*x
    print(Eq)

    
    print(nb1, '> nb1')
    print(nb2, '> nb2')
    print(nbx1, '> nbx1')
    print(nbx2, '> nbx2')

    a = '$x^{p-2}\$'
    print(a)
    nomP = 15
    var = 12
    aab = 5
    with doc.create(Section("Hello")):
        doc.append(NoEscape("\\ Factoriser $%s(%s + 5x)=%s$" % (nomP, var, aab)))
