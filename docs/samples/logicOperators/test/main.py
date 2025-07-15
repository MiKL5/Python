# Ne modifie pas les lignes suivantes
import sys
note = int(sys.argv[-1])
commentaire = ""

# Change l'ordre des if / elif
if note == 20:
    commentaire = "C'est un sans faute !"
elif 18 <= note < 20:
    commentaire = "Excellent !!"
elif 15 <= note < 18:
    commentaire = "Bon travail !"
elif 11 <= note < 15:
    commentaire = "Peut mieux faire."
elif 7 <= note < 11:
    commentaire = "Il faut tout revoir..."
elif 3 <= note < 7:
    commentaire = "Tu n'as rien compris !"
elif note < 3:
    commentaire = "Sans commentaire..."

# Ne modifie pas la ligne ci-dessous
print(commentaire)