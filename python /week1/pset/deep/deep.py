
deep  = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

deep = deep.lower().lstrip().rstrip()

match deep:
    case "42" | "forty two" | "forty-two":# these are or statements
        print("Yes")
    case _:
        print("No")
