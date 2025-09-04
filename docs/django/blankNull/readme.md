# **Les paramètres `blank` ou `null`** <a href="../../"><img align="right" src="https://www.djangoproject.com/m/img/logos/django-logo-negative.svg" alt="Django" height="64px"></a>
## **Blank**
Et utile pour les formulaires. Il évite qu'aucune valeur ne soit entrée, grâce à `blank = False`.  
À l'inverse `blank = True` autorise que le champ soit vide.  
Nonobstant, il est utile siil n'y a pas de valeur par défault (e.g. `default = "0"`).
## **`Null`**
Il s'agit d'une valeur qui n'en a pas (`NULL` équivalent de none), quand `null = True`.  
`null = True` est à éviter avec les champs tels que les chaîne de caractères ; il prendre forcément la chaîne de caractère vide.
___
>>> NOTA  
Si une date peut être vide, il faut ajouter `null = True` ; pour autoriser autre chose qu'une date dans le champ.