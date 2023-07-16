# 2) Étudiez ce qui se passe lorsqu’il y a une instruction return dans la clause try et dans la clause finally d’une instruction try.


def func():
    try:
        return "Retour depuis la clause try !"
    finally:
        return "Retour depuis la clause finally !"
print(func()) # "Retour de la clause finally !"
# Logique car finally s'exécute toujours et oublie le return de la déclaration try pendant qu'elle exécute le sien.