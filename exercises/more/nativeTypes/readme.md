# **Les types nativfs**<a href="../../../"><img align="right" src="../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
Il existe 6 types natifs dont 3 sont des dérivés servant à organiser les 3 premiers.
* Les chaînes de caractères ;
* Les nombres ;
* Les booléens ;
* Les types séquentiels (liste, tuple) ;
* Les types d'ensemble (set, frozenset) ;
* Les types de correspondances (dictionnaire).
## **Les chaînes de carractères**
Elles sont délimitées par des guillement simples (apostrophes) ou doubles.  
L'usage de guillement simples complique l'utilisation d'apostropher.  
L'antislash permet l'échapement (dire qu'il ne faut pas l'utiliser pour la fonction de base, ici la délimitation).

Les. chaînes de caractères multilignes snnt """délimitées de cette manière""", ou '''comme ceci'''.  
Avec les `'''` les apostrophes ne sont pas problèmatiques.

Pour les caractères spéciaux, il y a `\n` pour le retour à la ligne ou '\u2764' pour afficher un coeur. 2764 est le code du caractère unicode.

Les **raw sting** sont des chaînes de caractères bruts et symbolisés par `r`.  
```py
print(r'c:\dossier\')
```
Voici une liste non exaustive utilisable dans les raw string :  
* `\a` caractère d'appel (BEL) ;
* `\b` caractère de retour arrière ;
* `\f` saut de page ;
* `\n` retour à la ligne ;
* `\r` retour chariot ;
* `\t` tabulation horizontale ;
* `\v` tabulation verticale.
## **Les nombres**
Nature | Entiers | Décimaux (flottant)
---|---|---
Positif | ✅ | ✅
Négatif | ✅ | ✅
longueur | ✅ | ✅
Avec _ pour séparer les millers | 1_000 | 

Les nombres décimaux fonctionnent avec un `.` pas de `,`.  
10.0 n'est pas converti.
## **Les booléens**
Ils ont 2 valeurs 'true'=1 & 'false'=0. 
Ceux sont une sous classe des nombre entiers.
Les booléens sont associables aux nombres. `True+1=2` ou `False+5=5`. 
Chaque objet doit être `truthy` ou `falsy`.  
La fonction `bool()` le vérifie. Si elle est vide, c'est faux.  
Sont faux `0`, `0.0`, `[]`, `{}`. Les types séquenciels sont faux s'ils sont vides comme ici.