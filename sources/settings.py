# Module de création du Fichier Tex et convertion en pdf et autre
from pylatex import *
from pylatex.utils import *

# Module de GUI de python
from tkinter import *

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
# import latexify
from sympy import *

#Module de gestion fichier sur la machine
import os
import glob