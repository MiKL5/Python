while True:
    # Ask the first numver
    n1 = float(input("What's the first number? "))

    # Ask the second number
    n2 = float(input("What's the second? "))

    # Dislay result and perform addition 
    # print(f"The result of {n1} with {n2} is {float(n1) + float(n2)}")
    print(f"The result is {float(n1) + float(n2)}")

    # Ask if user wants to continue
    print("Would you like another addition? (yes/no)")
    reponse = input().strip().lower()
    if reponse not in ("oui" , "o" , "yes" , "y"):
        break