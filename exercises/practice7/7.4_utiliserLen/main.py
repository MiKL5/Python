# 4. Imprimer la longueur du mot saisi
word = input("Saisissez un mot : ").strip()
print(len(word))
# imprimer le nombre de mot.s
string_of_words = input("Saisisiez un mot ou un phrase : ")
character_count = len(string_of_words)
word_count = len(string_of_words.split())

print(f"{character_count} caractère.s")
print(f"{word_count} mot.s")