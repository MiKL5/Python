# **Les conditions "`any`" et "`all`"**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
```py
any(False, False, True, False)
all(False, False, True, False)
```
Généralement on y met des ccompréhensions de liste.
```py
all([f.endswith(".jpg") for f in files])

notes = [12, 14, 20, 10, 8]
any([x > 18 for x in notes])
```