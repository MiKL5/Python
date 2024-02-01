# **Séparer le code en plusieurs fichiers** <a href="../"><img align="right" src="../../src/images/Python-logo-notext.svg" alt="Python" title="Phthon" widht="auto" height="64px"></a>

## **Pourquoi ?**

Conserver le code dans un seul fichier facilite l'écriture au début, mais devient plus dificile à lire et à maintenir.  

La lisibilité et la maintenabilité sont plus importante que la vitesse d'écriture.  

### **Organisation**

Il est important de savoir pourquoi on met le code dans un autre fichier. On procéde par préoccupations. Les fonctions dans un fichier 'fn.py', un fichier pour les interaction avec les utlisateur, un fichier pour stocker les données, par exemple.  

### **La lisibilité**

Cela permet d'avoir des fichiers plus petits est plus ciblés. Donc, il est plus facile d'aller d'un fichier à l'autre. Le contenu des fichiers est plus facile à comprendre.

### **Bien réutiliser le code**

Il est plus facile d'utiliser un fichier dans d'autre en l'important.   

Attention à ne pas avoir trop de fichier. L'intérêt n'est pas de faire les fichiers les plus petits, mais les plus ciblés. Un fichier traite un aspet et porte un nom correspondant.

## **Travailler avec deux fichiers**

### **Que se passe t-il à l'importation**

Python lit le fichier pour déterminer les noms qui s'y trouvent. Puis, le met à disposition dans 'main.py' en plaçant une référence au module dans le namespace global.  

Python recherche d'abord les fichiers du projet avant de regarder la paquets intégrés ou installés, c'est pourquoi il ne faut pas donner aux fichiers le nom des modules intégrés.

### **Les fichiers que l'on créer fonctionnent de la même manière que les modules**

On peut faire avec les fichiers tout ce que l'on peut faire avec les modules externes :
* importer le fichier `import monfichier` et se référer à `monfichier.x` ;
* importer des élément spécifique `from monfichier import x` ;
* importer des alias ;
* faire `from monfichier import *` qui est déconseillé.

### **Utiliser des fichiers et dossiers**


```py
from folder.subfolder.module import something_in_the_module
```
Le `.` signifie à "l'intérieur".  

Lors d'importations comme celles-ci, on importe soit des éléments spécifiques, soit des importations d'alias. La première méthode est souvant meilleure :
* `from user_interactions.myfile import get_user_age` ;
* `import user_interactions.myfile as interactions`.

### **Script mode versus module mode**

Le fichier 'main.py' est exécuté en mode script, un fichier importé est exécuté en mode module.  
Tout fichier dans la variable `_ _nalme_ _` n'est pas égale à `_ _main.py_ _` est importé.

### **Exécution du code uniquement en mode script**

Parfois, il est nécessaire d'inclure du code dans un fichier, et de vouloir que ce code s'exécute uniquement lorsque le fichier est lancé directement, et non lors de son importation.

Par exemple dans 'monfichier.py'
```py
def get_user_age():
    return int(input("Indiquez votre âge : "))

if __name__ == "__main__":
    get_user_age()
```
* * l’un des principaux cas d’utilisation :  voir si le contenu d’un fichier fonctionne alors que l'on ne veut pas qu’il s’exécute.
* un autre cas d’utilisation concerne les fichiers que l'on n’exécutez pas normalement soi-même. Parfois, on peut écrire un fichier destiné à être utilisé par un autre programme, par exemple.

L’utilisation de cette construction permettra d’exécuter le fichier pour le tester, tout en n’affectant pas sa fonctionnalité lorsqu’il est importé par un autre programme.