# **Les structures conditionnelles**<a href="../../../"><img align="right" src="../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
```py
## **Les blocs d'instructions**
À quoi servent-ils et quand sont-ils utilisés ?  
Ils sont dans la pluspart des langages de programmations.  
Il apportent l'appartenance à une ou plusieurs lignes de code.  
Les `:` à la fin indique qu'un bloc d'instruction suit.  
L'indentation (est moins permisive, alège le code) indique que cette ligne est dépendante de l'autre.  
Ce blocs peuvent êtres imbriqués les uns aux autres.

⚠️ Avec Python, il faut être attentif à l'indentation.
```py
age = int(input("how old are you? "))
if   age >= 18:
    print("You're over 18.")
elif age <  18:
    print("Wait until you're 18.")
```
```py
age = int(input("how old are you? "))
if age >= 18:
    print("You're over 18.")
else:
    print("Wait until you're 18.")
```
