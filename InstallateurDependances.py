import subprocess
import sys

# Liste des packages nécessaires
packages = [
    "lastpage",
    "geometry",
    "tkz-tab",
    "fancyhdr",
    "newunicodechar",
    "latexmk"
]

def check_miktex_package(package):
    """Vérifie si un package MiKTeX est installé."""
    try:
        # Exécute la commande mpm pour vérifier l'installation du package
        result = subprocess.run(
            ["mpm", "--list", package],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        
        # Si le package est trouvé, la sortie standard le contiendra
        if package in result.stdout:
            return True
        return False
    
    except FileNotFoundError:
        print("MiKTeX Package Manager non trouvé. Assurez-vous que MiKTeX est installé et que 'mpm' est dans votre PATH.")
        sys.exit(1)

def install_miktex_package(package):
    """Installe un package MiKTeX."""
    try:
        print(f"Installation de {package}...")
        subprocess.run(
            ["mpm", "--install", package],
            check=True
        )
        print(f"{package} a été installé avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Échec de l'installation de {package}. Erreur: {e}")

def main():
    for package in packages:
        if check_miktex_package(package):
            print(f"{package} est déjà installé.")
        else:
            print(f"{package} n'est pas installé.")
            install_miktex_package(package)

    # Vérifie si pip est installé et l'installe si nécessaire
    subprocess.run(["python", "-m", "ensurepip"], check=True)

    # Installe les dépendances à partir du fichier Requirements.txt
    try:
        subprocess.run(["pip", "install", "pylatex"], check=True)
        subprocess.run(["pip", "install", "matplotlib"], check=True)
        subprocess.run(["pip", "install", "numpy"], check=True)
        subprocess.run(["pip", "install", "sympy"], check=True)
        print("Les dépendances ont été installées avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation des dépendances: {e}")




if __name__ == "__main__":
    main()
