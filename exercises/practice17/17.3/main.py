# 3) Imprimez le dictionnaire suivant à l’aide de la méthode format et de l’unpacking **.
#
# country = {
#     "name": "Germany",
#     "population": "83 million",
#     "capital": "Berlin",
#     "currency": "Euro"
#  }


country = {
    "name": "Italie",
    "population": "60 million",
    "capital": "Rome",
    "currency": "Euro"
}
country_template = """Pays       : {name}
Population : {population}
Capitale   : {capital}
Monnaie    : {currency}"""
print(country_template.format(**country))