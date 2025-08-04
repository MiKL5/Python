while True:
    mdp = input("Entrez un mot de passe (min 8 caractères) : ")
    mdp_trop_court = "entrez un mot de passe d'au moins 8 caractères alphanumériques."

    if len(mdp) == 0:
        print(mdp_trop_court.upper())
    elif len(mdp) < 8:
        print(mdp_trop_court.capitalize())
    elif mdp.isdigit():
        print("Votre mot de passe ne contient que des chiffres.")
    elif mdp.isalpha():
        print("Votre mot de passe ne contient que des lettres.")
    else:
        print("Inscription terminée.")
        break