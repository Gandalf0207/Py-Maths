from pylatex import *
from pylatex.utils import * 
import random






def write(doc,i):
    nb1 = random.randint(1,50)
    nb2 = random.randint(1,50)
    nb3 = random.randint(1,50)
    nb4 = random.randint(1,50)
    nb5 = random.randint(1,50)
    nb6 = random.randint(1,50)
    nb7 = random.randint(1,50)
    nb8 = random.randint(1,50)
    nb9 = random.randint(1,50)
    nb10 = random.randint(1,50)
    nb11= random.randint(1,50)


    doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
    doc.append(pylatex.Command('selectfont'))

    with doc.create(Section(f"Correction Exo n°{i+1}", numbering = False)):
        doc.append("Niveau 1 :")

        doc.append(NoEscape("\\begin{align*}"))

        doc.append(NoEscape("\\begin{cases}"))
        doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (nb1, nb2, nb5)))
        doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (nb3, nb4, nb6)))
        doc.append(NoEscape("\\end{cases}"))
        doc.append(NoEscape("\\\\"))
        
        doc.append(NoEscape("\\end{align*}"))
        doc.append(NoEscape("\\ \\text{L'équation ligne 2 permet d'écrire :}\\\\" % ()))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\begin{align*}"))
        doc.append(NoEscape("\\  \\Leftrightarrow %sx + %sy - %sy &= %s - %sy \\\\" % (nb3,nb4,nb4,nb6,nb4)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\  \\Leftrightarrow %sx &= -%sy + %s\\\\" % (nb3, nb4,nb6)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{-%sy + %s}{%s}\\\\" % (nb3,nb3,nb4,nb6,nb3)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())
        doc.append(NoEscape("\\end{align*}"))
        
        doc.append(NoEscape("\\\\"))
        doc.append(NoEscape("\\ \\text{On remplace x par $\\frac{-%sy + %s}{%s}$ dans l'équation 1}\\\\" % (nb4,nb6,nb3)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\begin{align*}"))
        doc.append(NoEscape("\\ \\Leftrightarrow  %s \\times \\frac{-%sy + %s}{%s} + %sy &= %s\\\\" % (nb1,nb4,nb6,nb3,nb2,nb5)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\ \\Leftrightarrow  %s \\times \\frac{-%sy}{%s} + %s \\times \\frac{%s}{%s} + %sy &= %s\\\\" % (nb1,nb4,nb3,nb1,nb6, nb3,nb2,nb5)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        new_y_1_nv1 = round((nb1*((-nb4)/nb3) + nb2),2)
        new_nb_1_nv1 = round((nb1*(nb6 / nb3)),2)
        doc.append(NoEscape("\\ \\Leftrightarrow  %sy + %s &= %s\\\\" % (new_y_1_nv1, new_nb_1_nv1,nb5)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\ \\Leftrightarrow  %sy + %s - %s &= %s - %s\\\\" % (new_y_1_nv1, new_nb_1_nv1,new_nb_1_nv1,nb5,new_nb_1_nv1)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        new_nb_2_nb1 = round(nb5 - new_nb_1_nv1,2)
        doc.append(NoEscape("\\ \\Leftrightarrow  %sy  &= %s\\\\" % (new_y_1_nv1, new_nb_2_nb1)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\ \\Leftrightarrow  \\frac{%sy}{%s}  &= \\frac{%s}{%s}\\\\" % (new_y_1_nv1,new_y_1_nv1, new_nb_2_nb1,new_y_1_nv1)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        result_y_nv1 = round((new_nb_2_nb1 / new_y_1_nv1),2)
        doc.append(NoEscape("\\ \\Leftrightarrow  y  &\\approx %s\\\\" % (result_y_nv1)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())


        

        doc.append(NoEscape("\\end{align*}"))


        doc.append(NoEscape("\\ \\text{En remplaçant y par la valeur obtenue dans l'équation 1 :}\\\\" % ()))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\begin{align*}"))

        doc.append(NoEscape("\\ \\Leftrightarrow  %sx + %s \\times %s &= %s \\\\" % (nb1,nb2,result_y_nv1,nb5)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        nb = round((result_y_nv1*nb2),2)
        doc.append(NoEscape("\\ \\Leftrightarrow  %sx + %s -%s &= %s - %s \\\\" % (nb1,nb,nb,nb5, nb)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        new_nb_3_nv1 = round(nb5 - nb,2)
        doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= %s \\\\" % (nb1, new_nb_3_nv1)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())


        doc.append(NoEscape("\\ \\Leftrightarrow  \\frac{%sx}{%s} &= \\frac{%s}{%s}\\\\" % (nb1, nb1,new_nb_3_nv1,nb1)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        approche = round((new_nb_3_nv1/nb1),2)
        doc.append(NoEscape("\\ \\Leftrightarrow  x &\\approx %s \\\\" % (approche)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\end{align*}"))

















        doc.append("Niveau 2 :")

        doc.append(NoEscape("\\begin{align*}"))

        doc.append(NoEscape("\\begin{cases}"))
        doc.append(NoEscape("\\  \\frac{%s}{%s}x + %sy &= %sy - %s \\\\" % (nb1, nb2, nb3, nb4, nb5)))
        doc.append(NoEscape("\\  %sx + %sy &= %sy + \\frac{%s}{%s} \\\\" % (nb6,nb7 ,nb8,nb9,nb10 )))
        doc.append(NoEscape("\\end{cases}"))
        doc.append(NoEscape("\\\\"))
        
        doc.append(NoEscape("\\end{align*}"))
        doc.append(NoEscape("\\ \\text{L'équation ligne 1 permet d'écrire :}\\\\" % ()))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\begin{align*}"))
        doc.append(NoEscape("\\  \\Leftrightarrow  \\frac{%s}{%s}x + %sy - %sy &= %sy - %s - %sy \\\\" % (nb1, nb2, nb3,nb3, nb4, nb5,nb3)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        new_y_1_nv2 = nb4-nb3
        doc.append(NoEscape("\\  \\Leftrightarrow  \\frac{%s}{%s}x &= %sy - %s \\\\" % (nb1, nb2, new_y_1_nv2, nb5)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\  \\Leftrightarrow  \\frac{%s}{%s}x \\times \\frac{%s}{%s} &= (%sy - %s) \\times \\frac{%s}{%s} \\\\" % (nb1, nb2,nb2,nb1, new_y_1_nv2, nb5,nb2,nb1)))    
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        new_y_2_nv2 = round(new_y_1_nv2/(nb1/nb2),2)
        new_nb_1_nv2 = round(nb5/(nb1/nb2),2)
        doc.append(NoEscape("\\  \\Leftrightarrow  x &= %sy - %s\\\\" % (new_y_2_nv2,new_nb_1_nv2)))    
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())
        doc.append(NoEscape("\\end{align*}"))
        
        doc.append(NoEscape("\\\\"))
        doc.append(NoEscape("\\ \\text{On remplace x par $%sy - %s$ dans l'équation 2}\\\\" % (new_y_2_nv2,new_nb_1_nv2)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\begin{align*}"))
        doc.append(NoEscape("\\ \\Leftrightarrow  %s(%sy - %s) + %sy &= %sy + \\frac{%s}{%s} \\\\" % (nb6,new_y_2_nv2,new_nb_1_nv2,nb7,nb8,nb9,nb10)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        new_y_3_nv2 = round((nb6*new_y_2_nv2),3)
        new_nb_2_nv2 = round((nb6*new_nb_1_nv2),3)
        doc.append(NoEscape("\\ \\Leftrightarrow  %sy - %s + %sy &= %sy + \\frac{%s}{%s} \\\\" % (new_y_3_nv2,new_nb_2_nv2,nb7,nb8,nb9,nb10)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())


        doc.append(NoEscape("\\ \\Leftrightarrow  %sy - %s +%s + %sy &= %sy + \\frac{%s}{%s} +%s \\\\" % (new_y_3_nv2,new_nb_2_nv2,new_nb_2_nv2,nb7,nb8,nb9,nb10,new_nb_2_nv2)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        new_nb_4_nv2 = round(((nb9 / nb10) + new_nb_2_nv2),2)
        doc.append(NoEscape("\\ \\Leftrightarrow  %sy +%sy - %sy &= %sy -%sy + %s \\\\" % (new_y_3_nv2,nb7,nb8,nb8,nb8,new_nb_4_nv2)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        new_y_4_nv2 = (new_y_3_nv2 +nb7 - nb8)
        doc.append(NoEscape("\\ \\Leftrightarrow  %sy &= %s \\\\" % (new_y_4_nv2, new_nb_4_nv2)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\ \\Leftrightarrow  \\frac{%sy}{%s} &= \\frac{%s}{%s} \\\\" % (new_y_4_nv2,new_y_4_nv2, new_nb_4_nv2,new_y_4_nv2)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        result_y_nv2 = round((new_nb_4_nv2/ new_y_4_nv2),2)
        doc.append(NoEscape("\\ \\Leftrightarrow y &\\approx %s \\\\" % (result_y_nv2)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())


        

        doc.append(NoEscape("\\end{align*}"))


        doc.append(NoEscape("\\ \\text{En remplaçant y par la valeur obtenue dans l'équation 2 :}\\\\" % ()))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\begin{align*}"))

        doc.append(NoEscape("\\  %sx + %s \\times %s &= %s \\times %s + \\frac{%s}{%s} \\\\" % (nb6,nb7, result_y_nv2 ,nb8,result_y_nv2,nb9,nb10 )))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        new_nb_5_nv2 = round((nb7*result_y_nv2),2)
        new_nb_6_nv2 = round((nb8 * result_y_nv2),2)
        doc.append(NoEscape("\\ \\Leftrightarrow %sx + %s - %s &= %s +\\frac{%s}{%s} -%s \\\\" % (nb6, new_nb_5_nv2, new_nb_5_nv2, new_nb_6_nv2,nb9,nb10, new_nb_5_nv2 )))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        new_nb_7_nv2 = round((new_nb_6_nv2 + (nb9/nb10)-new_nb_5_nv2),2)
        doc.append(NoEscape("\\ \\Leftrightarrow %sx &= %s \\\\" % (nb6, new_nb_7_nv2)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\ \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{%s}{%s} \\\\" % (nb6,nb6 ,new_nb_7_nv2,nb6)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        result_x_nv_2 = round((new_nb_7_nv2/nb6),2)
        doc.append(NoEscape("\\ \\Leftrightarrow x &\\approx %s \\\\" % (result_x_nv_2)))
        doc.append(Command('vspace', '5mm'))
        doc.append(NewLine())

        doc.append(NoEscape("\\end{align*}"))
