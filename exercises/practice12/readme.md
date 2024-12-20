# Les fonctions  <a href="../../"><img align="right" assets="../../assets/images/Python-logo-notext.svg" alt="Python" title="Phthon" widht="auto" height="64px"></a>

Elles permettent de réduire la longueure du code et les répétitions pour les opérations a effectuer plusieurs fois.  
Le code est donc plus lisible est plus facile à comprendre.  
Aussi, il n'est pas nécessaire de connaître le fonctionnemnt du code sous-jacent d'une fonction, il suffit juste de savoir utiliser la fonction et ce que la fonction fera avec les valeurs fournies. Les détails d'implémentations peuvent souvent être igonrés en toute sécurité.  

## Définir

Le mot-clé `def` est l'abreviation de 'define' indique que ce qui suit est une définition de fonction.
```py
def get_even_numbers():
    for number in range(1, 11):
        print(number * 2)


get_even_numbers()
```
Note de style : afin de voir rapidement où se termine la fonction il est d'usage de la suivre de deux lignes vides.

## Paramètres et arguments

Certaines fonctions accèptes des valeurs, d'autres une invite.  
Pour accepter des valeurs dans nos fonctions, il faut l'indiquer à Python.  
Une seule valeur = un seul paramètre.  
Un paramètre est une variable qui permet d'accéder aux arguments que l'utilisateur transmet. Ils servent de noms pour les valeurs des arguments.
Certains arguments peuvent êtres rendus facultatifs.

Les paramètres, comme les variables, ne sont que des noms le confort des développeurs, afin de facilement raisonner sur les types de valeurs auxquelles nous avons affaire.
Lorsque nous avons plusieurs paramè
L’ordre dans lequel sont les arguments à une fonction peut être très important, et si nous ne faisons pas attention, nous pouvons nous retrouver avec des bogues.tres, par défaut, Python va attribuer des valeurs d’argument à ces paramètres dans l’ordre.
En conséquence, l’ordre dans lequel sont fournis les arguments à une fonction peut être très important, et si nous ne faisons pas attention, nous pouvons nous retrouver avec des bogues.