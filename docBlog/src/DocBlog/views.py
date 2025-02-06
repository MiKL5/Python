from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request): # le (paramètre permet de récupérer la requête
    # print("Bonjour !")
    #date = datetime.today()
    # print(date)
    # print(type(date) )
    # return HttpResponse("<h1>Bonjour et bienvenue !</h1><br><br><br><br><p>🚧 Construction... 🚧</p>")
    return render(request, "index.html", context={"prenom": "cher inconnu" , "date" : datetime.today() } ) # context permet de passer des paramètres dans le modèle telles que des clés et valeurs