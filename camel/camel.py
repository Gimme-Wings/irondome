
name = input("camel case: ")

for c in name:
    if c.islower:
        print(c, end = "")
    elif c.isupper:
        c = c.lower(c)
        print("_")
        print(c, end = "")
