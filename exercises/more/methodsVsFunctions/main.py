liste = [5, 3, 9, 7, 1]
# function
sorted(liste)
print(liste)          # unchanged

print(sorted(liste))  # changed

liste = sorted(liste)
print(liste)          # changed
# method
liste.sort()
print(liste)          # changed
# these are errors , 'cause it overwrites the list
print(liste.sort())   # empoy
liste = liste.sort()  # empty

film = "le seigneur des anneaux"
film.title()
print(film)