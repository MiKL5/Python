# **Différene entre les méthodes et les fonctions**<a href="../../../"><img align="right" src="../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
## **La méthode**
Fonction appartenant à un objet. 
## **La fonction**
Fonction qui ne modifie pass la variable.
```py
liste = [5, 3, 9, 7, 1]
# function
sorted(liste)
print(liste)          # unchanged

print(sorted(liste))  # changed

liste = sorted(liste)
print(liste)          # changed
# method
liste.sort()
print(liste)          # changed
# these are errors , 'cause it overwrites the list
print(liste.sort())   # empoy
liste = liste.sort()  # empty
```