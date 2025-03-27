# Py-Maths

> [!NOTE]
> Le projet **Py-Maths** a été récompensé aux trophées NSI 2024 par le prix territoriale de l'originalité ! [Résultats](https://trophees-nsi.fr/resultats-2024) :tada:

> [!IMPORTANT]
> Pour toute information complémentaire au niveau des droits d'auteur et de distribution, veuillez vous référer à la licence.

Py-Maths est un projet étudiant réalisé par 2 élèves en première NSI : **LUBAN Théo** & **PLADEAU Quentin**. Le but de ce projet est de réaliser un exerciseur de mathématique (inspiré de **PyroMaths**) avec leurs corrections détaillés pas à pas, sur différents niveaux (seconde, première et terminale). Ce projet a été développé avec le langage de programmation python et utilise le langage LaTeX pour pouvoir respecter l'ecriture mathématique. En effet toutes les valeurs présentes dans les exercices sont sélectionnées aléaoirement et les correction sont adpaté pour cela. Chaque exercice est donc unique pour un entrainement optimal !

Le projet propose différents exercices selon diffférents niveaux : 
  - Polynôme du second degrés
  - Equation à un inconnus
  - Equation à deux inconnus
  - Calculs de volumes
  - Dérivés

- Terminale
  - A venir

<br>

 Le projet utilise différentes ressources, en voici les principales : 
- Utilisation du module Python
- Utilisation du langage LaTeX pour respecter les normes d'écriture mathématique
- Utilisation des dépendances des modules Python & LaTeX

<br> </br>
### Comment Fonctionne le projet ?

A venir

<br> </br>

### Installation :

> [!NOTE]
> Le jeu et le système d'installation ont été développés pour les machines utilisant Windows 10 et plus.
> Si vous utilisez des versions antérieures ou encore un autre système d'exploitation (Linux / MacOS), veillez à ce que chaque élément d'installation soit compatible, téléchargez les éléments en compatibilité avec votre machine.

  > Télécharger le compilateur latex MikTek
  [MikTeX](https://miktex.org/download)

  > Télécharger Visual C++ 64
  [Visual C++ x64](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)

  > Récupérer le projet **Py-Maths**
  ```cmd
  git clone https://github.com/Gandalf0207/Maths-Quest.git
  ```
  > Installation extension LaTeX : type1cm.sty
  ```cmd
  mpm --install type1cm
  ```
  > Installation extension LaTeX : type1ec.sty
  ```cmd
  mpm --install cm-super
  ```
  > Installation extension LaTeX : geometry.sty
  ```cmd
  mpm --install geometry
  ```
  > Installation extension LaTeX : underscore.sty
  ```cmd
  mpm --install underscore
  ```
  > Installation extension LaTeX : ttfonts.map
  ```cmd
  mpm --install zhmetrics
  ```
  > Installation extension LaTeX : amsmath
  ```cmd
  mpm --install amsmath
  ```
  > Intaller les dépendences
  ```cmd
  python -m pip install -r requirements.txt
  ```

> [!NOTE]
> Pour toutes les dépendances LaTeX, un pop-up peut s'ouvrir, vous devez cliquer sur "Install" pour pouvoir l'installer.

> [!TIP]
> Si vous utilisez une ancienne version de Windows ou bien que vous rencontrez toujours une erreur avec Visual C++ x64, installez également [Visual C++ x86](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170).

> [!TIP]
> Veillez à redémarer votre machine après l'installation du compilateur LaTeX.

<br> </br>

### Partie developpeur :

Avenir



#
__Py-Maths © Tous droits réservés 2024__

*by LUBAN Théo & PLADEAU Quentin with* :heart: 
