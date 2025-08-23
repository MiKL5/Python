# **Les attributs de tableau**<a href="../../"><img align="right" src="../../../assets/numpy_2020.svg" alt="Numpy" height="64px"></a>
Attribut|Description
:-:|---
T|Retourne une vue transposée du tableau.
base|L'objet de base si le tableau partage sa mémoire avec un autre tableau.
ctypes|Une interface pour interagir avec du code C.
data|Le buffer contenant les données brutes du tableau.
device|L'appareil sur lequel réside le tableau (par exemple| CPU ou GPU).
dtype|Le type de données des éléments dans le tableau.
flags|Informations sur la mémoire et les caractéristiques du tableau.
flat|Un itérateur sur le tableau aplati.
imag|La partie imaginaire des éléments du tableau| si il s'agit d'un type complexe.
itemsize|La taille en octets de chaque élément du tableau.
mT|Similaire à T| utilisé pour la transposition de matrices 2D.
nbytes|La taille totale du tableau en octets (produit de size et itemsize).
ndim|Le nombre de dimensions (ou axe) du tableau.
real|La partie réelle des éléments du tableau| s'il est de type complexe.
shape|Les dimensions du tableau sous forme de tuple.
reshape|Méthode pour redimensionner le tableau sans changer ses données, sous réserve que le nombre total d'éléments reste le même
size|Le nombre total d'éléments dans le tableau.
resize|Fonction redimensionnant le tableau, répétant les éléments si nécessaire pour remplir la nouvelle forme.
strides|Le nombre d'octets à sauter pour passer à l'élément suivant dans chaque dimension.