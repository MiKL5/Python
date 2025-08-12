# **Les dictionnaires**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
Les dictionnaires sont délimités par <kbd>{</kbd><kbd>}</kbd>.  
```py
dictionnaire = {"prenom" : "Paul", "profession" : "Ingénieur"}
```
Les dictionnaires sont imbricables les uns aux autres.
```py
dictionnaire = {
    0: {"prenom":     "Paul",
        "profession": "Ingénieur",
        "ville":      "Paris"},
    1: {"prenom":     "Julie",
        "profession": "Architecte",
        "ville":      "Marseille"},
    2: {"prenom":     "Pierre",
        "profession": "Plombier",
        "ville":      "Nantes"}
}
```
La clé permettant l'accés à la valeur, elle est unique dans le dictionnaire.