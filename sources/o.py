from pylatex import *

# Créez un document
doc = Document()

# Ajoutez une section
with doc.create(Section('Ma section')) as section:
    # Ajoutez une sous-section centrée
    with section.create(Subsection('Contenu centré')) as subsection:
        # Utilisez l'environnement Center pour centrer le texte
        with subsection.create(Center()):
            subsection.append("Ceci est un exemple de texte centré dans une sous-section.")
            # subsection.append(NewLine())
            subsection.append("Ceci est un exemple de texte centré dans une sous-section.")

# Générez le document
doc.generate_pdf('centrage_sous_section', clean_tex=False, compiler='pdflatex')