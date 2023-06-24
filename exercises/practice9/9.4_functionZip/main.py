# La fonction Zip est très puissante et polyvalente utilisée pour combiner plusieurs itérables en un (en rassemblant les élément de chaque itérables dans une tuple).

pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]

pets_and_owners = zip(pet_owners, pets)

print(list(pets_and_owners))
# [('Paul', 'Fluffy'), ('Andrea', 'Bubbles'), ('Marta', 'Captain Catsworth')]