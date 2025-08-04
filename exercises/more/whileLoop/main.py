i = 0
while i < 10000:
    print("Hi!");i += 1
# Beauoup de ligne peuvent êtres en une avec le ";".

continuer = "o"
while continuer == "o":
    print("Ça continue...")
    continuer = input("Voulez-vous continuer ? o/n          ") # input met en pause donc les risque sont limités

import time

while True:
    print("Sauvegarde...")
    time.sleep(600)