#using multiple dict
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "ron", "house": "gryffindor", "patronus": "jack russel terrier"},
    {"name": "Draco", "house": "slytherin", "patronus": None}
]

for i in students:
    print(f"The patronus of {i["name"]} is a/an {i["patronus"]}",sep=", ")

