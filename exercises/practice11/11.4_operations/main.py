# Trouvez l’union, la différence symétrique et l’intersection des deux ensembles. Imprimez les résultats de chaque opération.


s = set()
s.update(range(1, 4))
randomValues = {"r", 1, ("Python", "C", "Rust")}
print(s.union(randomValues))
print(s.symmetric_difference(randomValues))
print(s.intersection(randomValues))

# Ce qui donne :
# {1, 2, 3, ('Python', 'C', 'Rust'), 'r'}
# {2, 3, 'r', ('Python', 'C', 'Rust')}
# {1}