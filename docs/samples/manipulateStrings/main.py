for i in range(100):
    print(str(i).zfill(6))

"bonjour".islower()
True

"Bonjour À Tous".istitle()
True

"000020".isdigit()
True

"20yo".isdigit()
False

"Bonjour le jour".count("jour")
2

"Bonjour le jour".count(" jour")
1

"Bonjour le jour".count("   jour    ")
0