# **Modifier un liste**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
Pour ajouter une valeur, la méthode "``append``". Une méthode est analogue à une fonction. Elle est reliée directement par un point. Et entre parenthèse le contenu.
```py
liste.append(5)
```
Pour ajouter plusieurs valeurs dans un seul argument, "`extend`", donc il y a des crochets entre parenthèses.
```py
liste.extend([5, "chat", True])
```
Pour supprimer, c'est la méthode "`remove`". Si plusieurs sont identique, il n'enlève que la première ocurence.  
Il faut donc plusieurs lignes.
```py
liste.remove(5,5) # Il reste le second 5
```
