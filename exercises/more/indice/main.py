liste=("neuf", 20, False)
print(liste[ 0]) # neuf
print(liste[ 2]) # False
print(liste[-3]) # neuf

liste = [1, 2, [3, "Python", 4], 5, 6]
print([2][1])    # Python

langages = ["Java", "Python", "C++"]
langage = langages[1]

liste = ["Java", "Python", "C++"]
liste.remove("Python")
liste.append("Python")