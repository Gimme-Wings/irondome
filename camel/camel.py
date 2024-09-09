
name = input("camel case: ")
print("snake case: ", end = "")
for c in name:

    if c.islower:
        print(c, end = "")
    elif c.isupper:
        c.lower()
        print("_")
        print(c, end = "")

