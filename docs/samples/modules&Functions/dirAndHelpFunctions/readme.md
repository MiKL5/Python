# **Les fonctions '`dir`' et '`help`'**<a href="../../../../"><img align="right" src="../../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
Leurs but est de savoir ce que fait le module.
```py
import random
form pprint import pprint


print(dir(random))   # elles sont listées à la suite.

help(random)         # répond proprement, q pour quiter l'aide

help(random.randint) # explication claire

pprint(dir(random))  # un résultat par linge
```
Les fonctions avec des andorscores '_' sont privées, nous ne les utilisont pas.
