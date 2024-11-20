# Py math

### Qui sommes-nous
Nous sommes Quentin PLADEAU et Théo LUBAN, élèves au lycée général et technologique George Clemenceau à Montpellier. Tous deux “fan” de code nous voulions nous lancer dans un gros projet dont on pourrait être fier !

### Histoire du projet
Pyromath est l’origine du projet, il s’agissait d’un site utilisé par notre professeur de mathématique de 2nd qui permettait de générer de nombreux exercices avec leurs corrections. Seulement le site à disparu plus tard et ne pouvait donc plus être utilisé.
Suite à cela, lorsque nous cherchions une idée de projet pour [les trophées NSI](https://trophees-nsi.fr/), nous avons décidé de refaire Pyromath à notre manière.

### Fonctionnement
Installation du projet
Pour savoir comment installer le programme nous vous invitons à lire le [README](https://github.com/Gandalf0207/Py-Maths/edit/Dev-Principal/README.md) disponible sur GitHub.
D’un point de vue général, Py-math se présente à son lancement avec une interface graphique créée à l’aide de TkInter un module python.
Après son lancement l’utilisateur peut choisir son nombre d’exercices et l'exercice souhaité. Parmis les exercices proposés on retrouve :

- Polynômes du deuxième degré
- Equation du premier degré
- Équation à deux inconnus

Après avoir validé le choix de l’utilisateur, le programme va concevoir un code LateX qui grâce au compilateur MikTex sera converti en PDF.

### Langage et librairies utilisés
Py-math utilise majoritairement le langage Python et plusieurs de ses librairies. L’interface graphique est généré grâce à **Tkinter**, les créations de graphes et de courbes sont fait grâce à **matplotlib** et **numpy**, les calculs sont améliorés avec les imports **math** et **random**, la conversion est fait avec **PyLateX** ainsi que le langage LateX, la gestion des fichiers est fait avec **os** et **glob**.

### L’environnement
Pour supporter toutes les librairies utilisées, il a fallu créer un environnement python qui contient toutes les librairies.
Pour créer un environnement il faut utiliser, dans un invite de commande : 
    ```python -m venv```
Par la suite il vous faudra installer dans cet environnement le fichier ‘requirement.txt’ avec la commande : 
    ```pip install requirement.txt```
Pour des informations plus précises, le [README](https://github.com/Gandalf0207/Py-Maths/edit/Dev-Principal/README.md) disponible sur GitHub peut vous aider.
Après avoir fait cela, il vous suffit de placer tous les scripts python dans le dossier qui contient l’environnement.
> [!TIP]
> Vous pouvez mettre à jour votre environnement avec cette commande si vous possédez déjà une version entérieure de Py-Maths :
> ```pip install --upgrade -r requirements.txt```

### Le compilateur MikTek
[MikTek](https://miktex.org/download) est le compilateur de fichier .tex en .pdf que nous utilisons pour ce projet. En effet, dans notre script le module pdfLaTex est nécessaire pour pouvoir exécuter cette conversion. De plus d’autres dépendances latex sont nécessaires et vous seront proposées à l’installation dès lors que vous exécutez le script ‘Py_Maths.py’ pour la première fois.

> [!NOTE]
> A noter qu'après l'installation de MikTex il est fortement conseillé de redémarrer votre machine

Les dépendances qui vous seront demandées à l’installation pour la formation des documents sont :

- dernièrepage.sty
- géométrie.sty
- tkz-tab.sty
- fantaisiehdr.sty
- newunicodechar.sty
- latexmk.pl


Télécharger les scripts python depuis github avec la commande dans votre terminal : “git clone https://github.com/Gandalf0207/Py-Maths.git”
