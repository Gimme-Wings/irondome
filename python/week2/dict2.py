#using multiple dict
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "ron", "house": "gryffindor", "patronus": "jack russel terrier"},
    {"name": "Draco", "house": "slytherin", "patronus": None}
]

for i in students:
    print(i["name"], i["house"], i[sep=", ")

