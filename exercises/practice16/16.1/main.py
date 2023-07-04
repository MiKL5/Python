# 1) Utilisez la méthode sort pour classer la liste suivante dans l’ordre alphabétique des noms des élèves :
#
# students = [
#     {"name": "Hannah", "grade_average": 83},
#     {"name": "Charlie", "grade_average": 91},
#     {"name": "Peter", "grade_average": 85},
#     {"name": "Rachel", "grade_average": 79},
#     {"name": "Lauren", "grade_average": 92}
# ]
# Vous allez devoir passer une fonction comme clé ici, et c’est à vous de décider si vous utilisez une expression lambda, ou si vous définissez une fonction avec def.


students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]
students.sort(key=lambda student: student["name"])