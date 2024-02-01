# **Les gestion des exceptions** <a href="../"><img align="right" src="../../src/images/Python-logo-notext.svg" alt="Python" title="Phthon" widht="auto" height="64px"></a>

## **Définition**

La plupart des excéptions sont des erreurs, mais c'est parfois la notification de la survenue d'un évênement.  
Par exemple `stopIteration` est l'exception la plus courante. Il survient lors de l'itération d'une boucle `for` pour dire que toutes les valeurs ont été utilisées et qu'il n'y pas d'autres valeurs à nous donner. C'est ce qui permet à Python de savoir mettre fin au boucles `for`, mais aussi lors de la décomposition pour assigner à plusieurs variables.  

L'utilisation d'exception comme signal est très commune en Python.

## **Demander la permission vs demander le pardon**

Le fait de traiter manuellement des cas limites (dont il peut être difficile de savoir si nous avons marqué quelque chose) pour vérifier si quelque chose peut être fait à l'avance, s'appel _'`la demande de permission`'_.  
En Python, l'approche préférée est de tenté ce qu'on pense pouvoir échouer, et récupé éventuellemnt une excéption. C'est donc beaucoup plus simple de s'avoir quelles expcéptions peuvent se produirent. C'est la _'`demande de pardon`'_.

## **La déclaration `try`**

Une déclaration `try` permet de géer les exception de manière controlée afin déviter que le programme se termine brutaleemnt s'il y a une erreur en signalant de manière appropriée. Elle contient au moins deux parties, les clauses `try` et `except`, mais peut aussi contenir `else` et `finally`.  

```py
while True:
    try:
        number = int(input("Veuillez saisir un nombre entier : "))
        break
    except ValueError:
        print("Vous n'avez pas saisi un nombre entier valide !")
```


Le bloc try contient le code pouvant générer une exception. Si une exception se produit à l'intérieur de ce bloc, elle est levée et le reste du bloc try est ignoré.  

Si une exception est levée, Python cherche un bloc except correspondant pour gérer cette exception. Chaque bloc except spécifie le type d'exception qu'il peut gérer. Si l'exception correspond au type spécifié, le code à l'intérieur du bloc except est exécuté.  
Ici, la clause `except`attend la levée d'une `valueError` lors de l'exécution des options dans la clause `try`, le code de la clause `try` est abandonée au profit du code d'`ecept`.  
Il n'y pas de message d'erreur lorsque `valueError` se produit.  
La clause `except` permet de fournir une alternative d'action.  
Seuls les cas non gérés mettent fin au programme, c'est le dernier recours.

Parfois, il n'y a rien à faire pour corriger un problème, alors il est acceptable de mettre fin au programme

**Important !**
Le bloc try va cesser de s’exécuter dès qu’une exception se produit. Si quelque chose ne va pas, c’est comme si le code du bloc try n’avait jamais été exécuté.

## **Le traitement de plusieurs exceptions**

```py
import math
def average(numbers):
    try:
        mean = math.fsum(numbers) / len(numbers)
        print(mean)
    except (ZeroDivisionError, TypeError):
        print("Une moyenne ne peut pas être calculée pour les valeurs que vous avez fournies.")
```

Ci-aprés pas d’exceptions listées après la clause except. C’est une clause except nue, elle attrape toutes les exceptions qui se produisent.
```py
import math
def average(numbers):
    try:
        mean = math.fsum(numbers) / len(numbers)
        print(mean)
    except:
        print("Une moyenne ne peut pas être calculée pour les valeurs que vous avez fournies.")
```
Bien que cela ait son utilité, c’est généralement une très mauvaise chose à faire dans le code. En effet, elle attrape de nombreuses exceptions imprévues mais elle peut aussi masquer de graves problèmes de mise en œuvre.

## **La clause `else`**

Le code de la clause optionnelle `else` ne s’exécute que si aucune exception ne survient.

Il est possible de mettre plus de code dans le bloc `try`, mais ça peut être une très mauvaise idée :
* accidentellement attraper des exceptions imprévues.  
Plus il y a de code dans la clause try, plus cela risque de se produire. Cela peut rendre le traitement de l’exception inapproprié, car nous nous retrouvons à gérer une situation qui ne s’est pas réellement produite.
* Cela nuit à la lisibilité. La clause `try` exprime ce qui est attendu à voir échouer, et les clauses `except` expriment la manière dont nous prévoyons de traiter les échecs spécifiques de ce code. Plus le code est ajouté à la clause try, moins ce que nous essayons réellement est clair, ce qui rend l’ensemble de la structure plus difficile à comprendre.  

Nonobstant, nous n'avons pas toujours besoin de la clause `else`.

Utilisez votre jugement. Pour des exemples très simples, cela peut être exagéré, comme dans cet exemple :

## **La clause `finally`**

La clause `finally` aussi facultative, car sa présence est déterminée par les besoins.  
La clause `finally` est importante pour les instructins `try`. `Finally` est très spèciale car elle s'exécute toujours.  

Si une exception non gérée se produit, `finally` exécutera toujours son code avant que l'exception arrête le programme.

Cette propriété est extrêmement utile dans toutes les situations où un nettoyage essentiel est nécessaire après une opération. Par exemple, lorsque l'on travaille avec des fichiers. Si nous rencontrons un problème lors du traitement des données d’un fichier et que l'on veut toujours fermer le fichier lorsque nous avons terminé, et avec `finally` nous pouvons nous assurer que la libération des ressources se produit.

Le gestionnaire de contexte utilisé pour travailler avec des fichiers utilise en fait quelque chose de très similaire à cette clause `finally` en coulisses, pour s’assurer que les fichiers sont fermés quoi qu’il arrive. C’est tellement similaire en fait qu’il existe des moyens de créer nos propres gestionnaires de contexte en utilisant des instructions `try` avec des clauses finally.