### FICHIER TÊTES ET PIEDS DE PAGE###

# Module de création du Fichier Tex et convertion en pdf et autre
from pylatex import *
from pylatex.utils import *


def generate_header(doc, type_exo):
    
    # Ajout d'un haut de page
    header = PageStyle("header")

    # On crée un element au centre avec le type de l'exo 
    with header.create(Head("C")): 
        header.append(HugeText(bold(f"{type_exo}")))
    # On crée les crédits en bas à gauche
    with header.create(Foot("L")):
        header.append(italic("Théo LUBAN"))
    # On crée les crédits en bas à droite
    with header.create(Foot("R")):
        header.append(italic("Quentin PLADEAU"))

# On fait en sorte que les éléments apparaissent sur chaque page
    doc.preamble.append(header)
    doc.change_document_style("header")

### FIN FICHIER TÊTES ET PIEDS DE PAGE###