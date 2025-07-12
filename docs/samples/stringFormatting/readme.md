# **Le formatage des chaînes de caractères**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
## **La concaténation et les `f-string`**
```py
age       = 19
sentence  = "I've {age} yo."

age       = 19
sentence  = f"I've {age} yo."

firstname = "Kevin"
age       = 19
sentence  = f"I've {age} yo. His name is {firstname}."
```
## **La méthodee format()**
```py
age      = 16
sentence = "I've {} yo.".format(age)

age      = 16
sentence = "I've {a} yo.".format(a.age)

age      = 16
sentence = "I've {a} yo , {}.".format(a.age) # erreur

age      = 16
sentence = "I've {0} yo , {0} I'm teenager.".format(a.age)

firstname = "Kevin"
age       = 16
sentence  = "He's {} yo , {} his name is.".format(age , firstname)

firstname = "Kevin"
age       = 16
sentence  = "He's {1} yo , {0} his name is.".format(firstname , age)
```
Bien qu'ancienne, la méthode `format()`.  
Elle permet de définir la chaîne de caractères quelque part dans le script pour l'utilser plus tard.  
La méthode `format()` va chercher ce qui est défini dans un autre fichier contrairement à la "f-string".