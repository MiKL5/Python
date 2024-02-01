# 2) Créez une fonction qui accepte un nombre quelconque d’arguments de position et de mots-clés, et qui les imprime à l’utilisateur. Votre sortie doit indiquer quelles valeurs ont été fournies comme arguments de position et quelles valeurs ont été fournies comme arguments mots-clés.



def arg_printer(*args, **kwargs):
    args = [repr(arg) for arg in args]
    print(f"Les arguments de position sont : {', '.join(args)}")
    kwargs = [f"{key}={repr(value)}" for key, value in kwargs.items()]
    print(f"Les arguments de mots-clés sont : {', '.join(kwargs)}")

arg_printer(1, "blue", [1, 23, 3], height=184, key=lambda x: x ** 2)