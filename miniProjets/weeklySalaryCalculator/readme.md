
# Calculateur de salaire hebdomadaire <img align="right" src="../src/images/Python-logo-notext.svg" alt="Python" title="Phthon" widht="auto" height="64px">



***Ce programme fonctionne en ligne de commande***
```
Pour fonnctionner, il à besoin :
- du Nom de la personne ;
- du taux horaire ;
- du nombre d'heure travaillé.

Une capture vous donne un aperçu.
```

![Capture](../src/screenshots/calculateurDeSalaireHebdomadaire.png)

```python
# 1. L’utilisateur doit recevoir trois invites lui demandant de fournir différentes informations sur un employé. Une invite doit demander le nom de l’employé, une autre doit demander son salaire horaire, et la dernière doit demander combien d’heures l’employé a travaillé cette semaine.
# 2. Le nom de l’employé doit être traité pour s’assurer qu’il est dans un format particulier. Tous les noms d’employés doivent être dépourvus de tout espace blanc superflu et doivent être en majuscules. Cela signifie que chaque mot a sa première lettre en majuscule et que toutes les autres lettres sont en minuscules. Par exemple, si l’employeur a accidentellement activé le verrouillage des majuscules et qu’il écrit "rEGINA gEORGE", le nom sera quand même correctement enregistré sous la forme « Regina George ».
# 3. La rémunération totale de l’employé pour la semaine doit être calculée en multipliant les heures travaillées par son salaire horaire.
# 4. Rappelez-vous que toute entrée utilisateur que nous recevons sera une chaîne de caractères. Bien que nous puissions multiplier des chaînes de caractères, cela ne donnera pas tout à fait ce que vous voulez dans ce cas. Il est également utile de garder à l’esprit que le salaire de l’employé, ou le nombre d’heures travaillées, peut ne pas être un nombre entier.
# 5. Après avoir traité le nom de l’employé et calculé son salaire pour la semaine, le programme doit afficher ces informations sous la forme d’une chaîne unique. Par exemple, une sortie comme celle-ci serait appropriée :
# Regina George a gagné 800 € cette semaine.

# info retrieval
name = input("What is the name of the employee? ").title().strip()
wage = float(input("what is his hourly wage? "))
hourly = float(input("how long did his work this week? "))

# name display
print(f"Hello { name }.")

# hourly wage calculation
print(f"Your weekly wage is € { hourly * wage }.")

# name + weekly wage
print(f"{ name } received { round((hourly * wage), 2 ) } this week.")
earnings = float(wage) * float(hourly)
print(f"{ name } received { earnings:.2f } this week.")
```