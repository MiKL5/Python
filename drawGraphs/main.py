from chart import createChart
from dataStorage import readColumn



userMenu = """Veuillez choisir parmi les options suivantes :
- Saisissez 'c' ou 't' pour tracer un graphique.
- Saisissez 'q' pour quitter.
Quel est votre choix : """

chartingMenu = "Saisissez la colonne que vous souhaitez représenter : "

def handleChart():
    column = int(input(chartingMenu))
    x = readColumn(-1)
    y = map(float, readColumn(column))
    createChart(x, y)
while True:
    userSelection = input(userMenu)
    if userSelection == "q":
        break
    elif userSelection == "c" or "t":
        handleChart()
    else:
        print(f"Désolé, '{userSelection}' n'est pas une option valide.")


