# **Les opérateurs logiques**<a href="../../../"><img align="right" src="../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
`AND`, `OR` et `NOT`.

En utilisant `AND` le code est exécuté si tout est vrai.  
Avec `OR` au moins 1 doit être vrai.

L'opérateur le plus fort ; il est vérifier en premier.  
Nonobstant les parenthèses sont plus fortes que `AND`.  
`True` or `False` vaut `True`.

Et `NOT` retourne l'inverse de ce qu'il recoit.
```py
if not user == 'admin':
    print("access denied")
```