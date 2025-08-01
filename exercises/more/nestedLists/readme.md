# **Listes imbriquées**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
<!-- Les slices sont utilisables avec les listes imbriquées. -->
```py
liste = ["Python", ["Java", "C++"], ['C'], ["Ruby"]]
print(liste[1][0])

print(liste[0][0:2])

second_element = liste[1]
print(second_element[1])
```