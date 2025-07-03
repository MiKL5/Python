# **Variable** <a href="../"><img align="right" src="../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
_Les nombres entre -5 et 256 sont particuliers , il se peut que les résultats obtenus soit différents d'un ordi à l'autre ; Python gère la mémoire avec le meilleure efficacité._
## **Singleton et "small integer caching"**
### **Le singleton**
Cet obhet est unique.  
Tel que `none`, ainsi que `True` et `False`, ou `id = (c)`.  
Ainsi que les nombres de `-5` à `256`. Pour optimiser, il sont en mémoire.
C'est la pareil pour toutes les chaînes de caractères inférieure à 20 caractères.
### **Le Small integer caching**
E.g. `500` car ça place en mémoire change.  
Comme tout ce qui est en dehors de `-5` et `256`.