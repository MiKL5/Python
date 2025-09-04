# **Les objets muables et immuables**<a href="../../../"><img align="right" src="../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
Les méthodes peuvent directement sur les objets s'il sont muables.
## **Muables**
L'état ou le contenu peut être changé.

Type | Description simple | Exemple
---|---|---|
`list` | Liste ordonnée modifiable | `[1, 2, 3]`
`dict` | Dictionnaire (clé-valeur) | `{'a': 1, 'b': 2}`
`set` | Ensemble non ordonné sans doublon | `{1, 2, 3}`
`bytearray` | Séquence d’octets modifiable | `bytearray(b'abc') |
`collections.deque` | File doublement chaînée optimisée | `deque([1,2,3])`
`array.array` | Tableau typé (librairie `array`) | `array('i', [1,2,3])`
`memoryview` (sur `bytearray`) | Vue mémoire modifiable si source muable | `memoryview(bytearray(b'abc'))`
 Objets personnalisés | Objets de classes définies par l’utilisateur, sauf si `__slots__` ou `__setattr__` les rendent immuables | `class A: pass`

> ⚠️ Si un 'tuple' contient un objet muable, il est modifiable.
## **Immuable**
Type        | Description simple               | Exemple
------------|----------------------------------|---
`int`       | Entier                           | `42`
`float`     | Flottant                         | `3.14`
`complex`   | Nombre complexe                  | `2 + 3j`
`str`       | Chaîne de caractères             | `'hello'`
`tuple`     | Séquence immuable                | `(1, 2, 3)`
`frozenset` | Ensemble non modifiable          | `frozenset([1,2,3])`
`bytes`     | Séquence d’octets non modifiable | `b'abc'`
`range`     | Séquence numérique paresseuse    | `range(10)`
