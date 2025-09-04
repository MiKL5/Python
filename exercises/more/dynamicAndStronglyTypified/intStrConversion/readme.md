# **Conversion d'`int` et `str`**<a href="../../../../"><img align="right" src="../../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
```py
a =  5
b = 10
b = int(b)
print(a + b) # 15
```
Sauf que
```py
    b =    "10"
  int(b) #  10 # Il est traiter en entier, mais ...
print(b) # "10"  il reste en chaîne de caractère
```
Il ne faut pas se fier qu'à l'apparence car idle laisse croire que c'est convertit.