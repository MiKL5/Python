# **Les compréhensions**

_**Les compréhensions sont des fonctions comme des boucles for ordinaires**._

On utilise une comprehension pour créer une nouvelle collection à partir d’un autre itérable. Cependant, il y a des cas où on veut créer une nouvelle collection et où une compréhension n’est pas nécessaire. La compréhension est utilisée que lorsque l'on veut changer quelque chose concernant les valeurs lorsque nous créons cette nouvelle collection.  
On puet considérer les comprehensions comme un moyen d’exécuter une action pour chaque élément d’un itérable, puis de stocker les résultats.

## **La compréhension de liste**

Les plus couramment utilisés sont les compréhensions de listes (ou liste en compréhension ou list comprehension ).  
Les compréhensions de liste sont utilisées pour créer une nouvelle liste à partir d’un autre itérable. Il peut s’agir d’une autre liste, ou même d’un objet zip.
```py
names = ["mary", "Richard", "Noah", "KATE"]
```
Pour s’assurer que les prénoms ont tous une majuscule pour la première lettre, donc il faut itérer sur la liste et créer une nouvelle chaîne de majuscules à partir de chaque prénom.
```py
names = ["mary", "Richard", "Noah", "KATE"]
names = [name.title() for name in names]
```
Il est possibe de définir des compréhensions plus complexes où nous avons plusieurs variables de boucle.
```py
names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)
people = [(name.title(), age) for name, age in zip(names, ages)]
```
_Note de style_:
Les compréhensions peuvent devenir assez longues, surtout si les noms de variables sont longs. Dans ces cas, il peut être utile de répartir la compréhension sur plusieurs lignes.
```py
people = [
    (name.title(), age)
    for name, age in zip(names, ages)
]
```

## **La compréhension d'ensemble (de set)**

Fonction comme la compréhension de liste, maiś produit un ensemble.  

La structure interne de l'interprétation et identique à celle de la liste. Les accolades entourent au lieu des crochets.
```py
{'Mary', 'Richard', 'Noah', 'Kate'}
```

## **La compréhension de dictinnaire**

La compréhensin par dictionnaire est entourée d'une accolade et a besoin d'une clé et d'une valeur pour chaque élément.  

La paire clé-valeur à la même syntaxe qu'un dictionnaire (défini normalement). Tout d'abord, la clé suivie de `:`, puis la valeur
```py
student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")
students = {}
for student_id, name in zip(student_ids, names):
    student = {student_id: name.title()}
    students.update(student)
```

## **La compréhension de scope**

Comment il se fait que je puisse utiliser un nom de variable dans la compréhension et l’assigner au même nom de variable ? Est-ce que je remplace des valeurs en y accédant ? Et n’est-ce pas dangereux ?

je ne peux pas faire référence aux variables que je définis dans la boucle de l’interprétation depuis l’extérieur de l’interprétation.
```py
names = ["Mary", "Richard", "Noah", "Kate"]
names_lower = []
for name in names:
    names_lower.append(name.lower())
print(name)  # Ceci fait référence à la variable nom que nous avons définie dans la boucle
```
`name` est juste une variable normale, et une fois la boucle terminée, cette variable existe toujours. Sa valeur sera la dernière valeur qui lui a été attribuée dans la boucle. Dans le cas ci-dessus, `name` se réfère à la chaîne "Kate".  

En utilisant une compréhension de l'autre main, on ne peut pas faire ça.
```py
names = ["Mary", "Richard", "Noah", "Kate"]
names_lower = [name.lower() for name in names]
print(name)  # NameError car name n'est pas défini
```
La raison de ces différences est que les compréhensions sont en fait des fonctions.