# **Les types nativfs**
Il existe 6 types natifs dont 3 sont des dérivés servant à organiser les 3 premiers.
* Les chaînes de caractères ;
* Les nombres ;
* Les booléens ;
* Les types séquentiels (liste, tuple) ;
* Les types d'ensemble (set, frozenset) ;
* Les types de correspondances (dictionnaire).
## Les chaînes de carractères
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
Voici une liste non exaustive utilisables dans les raw string :  
`\a` caractère d'appel (BEL) ;
`\b` caractère de retour arrière ;
`\f` saut de page ;
`\n` retour à la ligne ;
`\r` retour chariot ;
`\t` tabulation horizontale ;
`\v` tabulatio verticale.