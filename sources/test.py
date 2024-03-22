from pylatex import *
from pylatex.utils import * 
import random

nb1 = random.randint(1,10)
nb2 = random.randint(1,10)
nb3 = random.randint(1,10)
nb4 = random.randint(1,10)
nb5 = random.randint(1,10)
nb6 = random.randint(1,10)
nb7 = random.randint(1,10)
nb8 = random.randint(1,10)
nb9 = random.randint(1,10)
nb10 = random.randint(1,10)
nb11= random.randint(1,10)
nb12 = random.randint(1,10)
nb13 = random.randint(1,10)
nb14= random.randint(1,10)

# Créez un document
doc = Document()

doc.packages.append(NoEscape("\\usepackage{amsmath}"))


doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
doc.append(pylatex.Command('selectfont'))

with doc.create(Section("Section de test", numbering = False)):
    doc.append("Niveau 1 :")

    doc.append(NoEscape("\\begin{align*}"))

    doc.append(NoEscape("\\begin{cases}"))
    doc.append(NoEscape("\\  %s(%sy + %sx) &= %s \\\\" % (nb1, nb2,nb3, nb4)))
    doc.append(NoEscape("\\  %sx + %sy &= %s(%sy + %s) \\\\" % (nb5,nb6, nb7, nb8, nb9)))
    doc.append(NoEscape("\\end{cases}"))
    doc.append(NoEscape("\\\\"))
    
    doc.append(NoEscape("\\end{align*}"))

    doc.append(NoEscape("\\ \\text{L'équation ligne 1 permet d'écrire :}\\\\" % ()))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    doc.append(NoEscape("\\begin{align*}"))
    doc.append(NoEscape("\\  \\Leftrightarrow %s \\times %sy + %s \\times %sx &= %s \\\\" % (nb1, nb2,nb1,nb3, nb4)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    new_y_1_nv1 = (nb1*nb2)
    new_x_1_nv3 = (nb1*nb3)
    doc.append(NoEscape("\\  \\Leftrightarrow %sy + %sx &= %s \\\\" % (new_y_1_nv1, new_x_1_nv3, nb4)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    doc.append(NoEscape("\\  \\Leftrightarrow %sy - %sy + %sx &= %s - %sy \\\\" % (new_y_1_nv1, new_y_1_nv1, new_x_1_nv3, nb4, new_y_1_nv1)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{%s - %sy}{%s} \\\\" % (new_x_1_nv3,new_x_1_nv3, nb4, new_y_1_nv1,new_x_1_nv3)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s - %sy}{%s} \\\\" % (nb4, new_y_1_nv1,new_x_1_nv3)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())


    doc.append(NoEscape("\\end{align*}"))
    
    doc.append(NoEscape("\\\\"))
    doc.append(NoEscape("\\ \\text{On remplace x par $\\frac{%s - %sy}{%s}$ dans l'équation 2}\\\\" % (nb4, new_y_1_nv1,new_x_1_nv3)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    doc.append(NoEscape("\\begin{align*}"))

    doc.append(NoEscape("\\ \\Leftrightarrow %s \\times \\frac{%s - %sy}{%s} + %sy &= %s \\times %sy + %s \\times %s \\\\" % (nb5,nb4, new_y_1_nv1,new_x_1_nv3,nb6, nb7,nb8 ,nb7, nb9)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    new_y_2_nv3 = (nb7*nb8)
    new_nb_2_nv3 = (nb7*nb9)
    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s \\times (%s - %sy)}{%s} + %sy - %sy &= %sy - %sy + %s \\\\" % (nb5,nb4, new_y_1_nv1,new_x_1_nv3,nb6,new_y_2_nv3,new_y_2_nv3,new_y_2_nv3,new_nb_2_nv3)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    new_nb_3_nv3 = (nb5*nb4)
    new_y_3_nv3 = (nb5*new_y_1_nv1)
    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s - %sy}{%s} + %sy - %sy &= %s \\\\" % (new_nb_3_nv3,new_y_3_nv3,new_x_1_nv3,nb6,new_y_2_nv3,new_nb_2_nv3)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s} - \\frac{%sy}{%s} + %sy -%sy &= %s \\\\" % (new_nb_3_nv3,new_x_1_nv3,new_y_3_nv3,new_x_1_nv3,nb6,new_y_2_nv3,new_nb_2_nv3)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    new_y_4_nv3 = round(((- new_y_3_nv3 / new_x_1_nv3) + nb6 - new_y_2_nv3),2)
    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s} - \\frac{%s}{%s} + %sy &= %s - \\frac{%s}{%s} \\\\" % (new_nb_3_nv3,new_x_1_nv3,new_nb_3_nv3,new_x_1_nv3,new_y_4_nv3, new_nb_2_nv3,new_nb_3_nv3,new_x_1_nv3)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    new_nb_5_nv3 = round((new_nb_2_nv3 +(- new_nb_3_nv3 / new_x_1_nv3)),2)
    doc.append(NoEscape("\\  \\Leftrightarrow %sy &= %s \\\\" % (new_y_4_nv3, new_nb_5_nv3)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%sy}{%s} &= \\frac{%s}{%s} \\\\" % (new_y_4_nv3,new_y_4_nv3,new_nb_5_nv3,new_y_4_nv3)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    result_y_nv3 = round((new_nb_5_nv3 / new_y_4_nv3),2)
    doc.append(NoEscape("\\  \\Leftrightarrow y &\\approx %s \\\\" % (result_y_nv3)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    doc.append(NoEscape("\\end{align*}"))


    doc.append(NoEscape("\\ \\text{En remplaçant y par la valeur obtenue dans l'équation 2 :}\\\\" % ()))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    doc.append(NoEscape("\\begin{align*}"))

    doc.append(NoEscape("\\  %s(%s \\times %s + %sx) &= %s \\\\" % (nb1, nb2,result_y_nv3 ,nb3, nb4)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    new_nb_6_nv3 = round((nb2 * result_y_nv3),2)
    doc.append(NoEscape("\\  %s \\times %s + %s \\times %sx &= %s \\\\" % (nb1, new_nb_6_nv3,nb1 ,nb3, nb4)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    new_nb_7_nv7 = round((nb1 * new_nb_6_nv3),2)
    new_x_2_nv3 = round((nb1*nb3),2)
    doc.append(NoEscape("\\  %s - (%s) +  %sx &= %s -(%s)\\\\" % (new_nb_7_nv7,new_nb_7_nv7,new_x_2_nv3, nb4,new_nb_7_nv7)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    new_nb_8_nv3 = round((nb4 - new_nb_7_nv7),2)
    doc.append(NoEscape("\\  %sx &= %s\\\\" % (new_x_2_nv3,new_nb_8_nv3)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    doc.append(NoEscape("\\  \\frac{%sx}{%s} &= \\frac{%s}{%s}\\\\" % (new_x_2_nv3,new_x_2_nv3,new_nb_8_nv3,new_x_2_nv3)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    result_x_nv3 = round((new_nb_8_nv3 / new_x_2_nv3),2)
    doc.append(NoEscape("\\  x &\\approx %s\\\\" % (result_x_nv3)))
    doc.append(Command('vspace', '5mm'))
    doc.append(NewLine())

    doc.append(NoEscape("\\end{align*}"))



# Générez le fichier PDF
doc.generate_pdf('test',clean_tex=False, compiler='pdflatex')