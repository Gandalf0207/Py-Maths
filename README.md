# Py-Maths

Py-Maths est un générateur d'exercices de Maths avec leurs corrections. Inspiré de l'ancien site **PyroMaths**

Téléchargez les scripts python depuis github avec la commande dans votre terminal  : 

      git clone https://github.com/Gandalf0207/Py-Maths.git

### Utilisation et mise en place de Py-Maths
>Installation d'un environnement virtuel avec python 3.11 
>
>Installation des Requirement
> 
>Installation de MikteK avec plusieurs dépendances
>
>Execution du script python 3.11 : "Py_Maths.py"

Ci-dessous; tous les éléments sont expliqués pour une installation correcte


#### Environnement virtuel

Veuillez installer python 3.11 sur votre machine : [Python 3.11](https://www.python.org/downloads/release/python-3110/). Après avoir fait cela ; dans votre terminal éxécutez cette commande afin de créer un environnement virtuel : 

Dans votre terminal tapez les commandes suivantes : 

Pour trouver l'emplacement de python (Nécéssaire uniquement si vous avez plusieurs version de python d'installé.) : 

      where python
<br>

Une fois l'emplacement python 3.11 trouvé, copiez le et placez le devant la commande suivante (uniquement si vous avez plusieurs version de python) : 

      <l'emplacement de python> -m venv <nom de l'environnement>

> Vérifiez l'endroit de création de votre environnement en vous plaçant à l'endroit souhaité avant de créer l'environnement.


#### Requirement
Veuillez installer le fichier requirements.txt afin d'installer toutes les librairies python nécéssaires au bon fonctionnement du projet.
Pour ce faire, éxécutez cette ligne de commande dans votre terminal : 

Pour activer votre environnement : 


Sur windows

      <environment name>\Scripts\activate.bat 

Pour installer les requirements : 

      pip install -r requirements.txt


##### MikteK
Pour installer MikteK, rendez-vous sur leur site Web afin de le télécharger : [Télécharger MikTeK](https://miktex.org/download)
Après l'installation, veuillez redémmarer votre machine.




#### Les Scripts Python
Téléchargez les scripts pythons et déposez-les dans le dossier qui contient l'environnement.


### Lancement
Après avoir tout installé et redémmaré votre machine; éxécutez le script *Py_Maths.py*. Il vous faudra installer de nouvelles dépendances de MikteK. À l'ouverture du pop up après l'éxécution du script, cliquez sur **install**.

Voici les dépendances qui s'afficheront et que vous devrez installer : 

##### lastpage.sty
##### geometry.sty
##### tkz-tab.sty
##### fancyhdr.sty
##### newunicodechar.sty
##### latexmk.pl

Fermez et réouvrez le fichier script et éxecutez-le à nouveau.


*Si la fenêtre Tkinter ne se lance pas, vérifiez bien que l'environnement est bien utilisée / que les dépendances de MikTek et python soient bien installés également*

## Voilà, Py-Maths fonctionne sur votre Machine ! 


*by Théo LUBAN & Quentin PLADEAU*
