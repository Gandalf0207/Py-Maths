# Module de création du Fichier Tex et convertion en pdf
from pylatex import *
from pylatex.utils import *


def generate_header(doc, type_exo):
    
    # Add document header
    header = PageStyle("header")

    # Create center header
    with header.create(Head("C")): 
        header.append(HugeText(bold(f"{type_exo}")))
    # Create left footer

    with header.create(Foot("L")):
        header.append(italic("Théo LUBAN"))
    # Create center footer
    with header.create(Foot("C")):
        header.append(italic("Quentin PLADEAU"))
    # Create right footer
    with header.create(Foot("R")):
        header.append(italic("Gabriel CADEAU-FLAUJAT"))

    doc.preamble.append(header)
    doc.change_document_style("header")