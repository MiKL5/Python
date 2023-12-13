# Ecrire l'exception dans un fichier `log.txt`

def log_exception(exception, fn, **kwargs):
    values = ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
    with open("log.txt", "a") as log_file:
        log_file.write(f"Exception : {exception}, Fonction : {fn}, Valeurs : {values}\n")


def itemgetter(collection, identifier):
    try:
        return collection[identifier]
    except (IndexError, KeyError, TypeError) as ex:
        log_exception(ex, "itemgetter", collection=collection, identifier=identifier)
        raise