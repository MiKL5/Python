import itertools

employees = itertools.cycle(["Pierre", "Fiona", "Kevin"])
days = itertools.cycle(["Lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"])

for day_number in range(1, 31):
    print(f"Jour {day_number} ({next(days)}): {next(employees)} ferme le magasin.")