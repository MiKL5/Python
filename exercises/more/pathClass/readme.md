# **La class path**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
L'objet '`Path`' est une classe permettant la création de chemin.  
<!-- Il n'y a pas de se questionner à propos du sens des slashs. -->
```py
Path.home() # user folder

Path.cwd() # curent working directory

# Création d'une objet depuis un chapine de caractères
p = Path("/users/mikl/Documents")

p

p.parent # /users/mikl/