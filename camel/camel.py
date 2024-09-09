
name = input("camel case: ")
print("snake case: ", end = "")
for c in name:

    if c.islower():
        print(c, end = "")
    elif c.isupper():
        c = c.lower()
        print("_", end = "")
        print(c, end = "")
print()

