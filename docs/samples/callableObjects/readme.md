# **Les objects '`callable`'**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
Ce sont des objets appelables.
```py
os.makedirs() # est callable
```
Tous ne le sont pas.èpy
```py
import pprint
print(collable(pprint)) # False
```
```py
from pprint import pprint
print(collable(pprint)) # true
```