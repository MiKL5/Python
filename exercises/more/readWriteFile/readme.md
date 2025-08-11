# **Lire et écrire un fichier**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
```py
p = Path.home() / "PahtLib" / "readme.txt"

p.touch()
# more readme.txt
p.write_text("Hello")
# more readme.txt
p.read_text()