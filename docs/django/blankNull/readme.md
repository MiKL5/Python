# **Les paramètres `blank` ou `null`**
## **Blank**
Et utile pour les formulaires. Il évite qu'aucune valeur ne soit entrée, grâce à `blank = False`.  
À l'inverse `blank = True` autorise que le champ soit vide.  
Nonobstant, il est utile siil n'y a pas de valeur par défault (e.g. `default = "0"`).
## **`Null`**
Il s'agit d'une valeur qui n'en a pas (`NULL` équivalent de none), quand `null = True`.  
`null = True` est à éviter avec les champs tels que les chaîne de caractères ; il prendre forcément la chaîne de caractère vide.