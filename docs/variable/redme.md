# **Variable** <a href="../"><img align="right" src="../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
La variable est le nom associé à l'objet, facilitant son accès.
```py
chiffre = 5 # python créer un int
chiffre_2 = chiffre # chiffre_2 = 5 pas nombre
chiffre = 1 # il est attaché à 1
# Le "Garbae collector" se débarasse du 5
``` 
La fonction `id()` permet de savoir combien de place un objet utilise en mémoire.
```py
id(nombre)
4514223664
```
Si je le refait
```py
id(500)
4514223600 # 1 nouvel objet créer l'espace différent en mémoire
```
Et si
```py
a = 500
b = a
id(a)
4514223568
id(b)
4514223568 # même objet ; même id
b = 1000
ad(b)
4514224688 # nouvel oobjet
```
## **Affectations simples, parallèles et multiples**
### **Affection simple**
```py
nom = objet
```
### **Affectation parallèles**
```py
a , b = 5 , 8 # regroupe 2 varable en 1 ligne
```
Elle est très utilisée ; permettant l'inversion
```py
a , b = b , a
```
La limite à l'affectation parallèle est la lisibilité
```py
a , b , c , d , e , f = 1 , 2 , 3 , 4 , 5 , 6 # L'affectation simple est mieux
```
### **L'affectation multiple**
```py
a = b = b = c = 5 # Car les variables ont la même valeur
a = b = b = 5 = c # Ne fonctionne pas ; manque de bon sens
```
> **_NOTA_**
_L'une des convention avec Python est de privilégier la simplicité à la complexité._