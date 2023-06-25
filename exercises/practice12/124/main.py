# 4) Créez une fonction pour tester si un mot est un palindrome. Un palindrome est une chaîne de caractères identiques, qu’elle soit lue à l’endroit ou à l’envers. Par exemple, « c’était une voiture ou un chat que j’ai vu » est un palindrome.

# Dans le projet du septième jour, nous avons vu plusieurs façons d’inverser une séquence, et vous pouvez utiliser cette méthode pour vérifier si une chaîne de caractères est identique à l’envers et dans son ordre original. Vous pouvez également utiliser une approche par découpage (slicing). Une fois que vous avez déterminé si un mot est un palindrome ou non, vous devez imprimer le résultat à l’utilisateur.

# Veillez à nettoyer l’argument fourni à la fonction. Nous devons supprimer les espaces des deux extrémités de la chaîne de caractères et convertir le tout en respectant la case, au cas où nous aurions affaire à un nom, comme "Hannah".

# Avec `reversed`

def is_palindrome(word):
    word = word.strip().lower()
    reversed_word = reversed(word)
    if list(word) == list(reversed_word):
        print(True)
    else:
        print(False)
is_palindrome("Hannah")  # True
is_palindrome("Fred")    # False

# Avec `join`

def is_palindrome(word):
    word = word.strip().lower()
    reversed_word = reversed(word)
    if word == "".join(reversed_word):
        print(True)
    else:
        print(False)
is_palindrome("Hannah")  # True
is_palindrome("Fred")    # False

# utilisation de slice (tranche), solution élégante

def is_palindrome(word):
    word = word.strip().lower()
    if word == word[::-1]:
        print(True)
    else:
        print(False)
is_palindrome("Hannah")  # True
is_palindrome("Fred")    # False