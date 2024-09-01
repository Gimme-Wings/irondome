name  = input("whats your name? ")

#if name == "Harry" or name == "hermione" or name == "ron" :
#    print("G")

#elif name == "draco":
 #   print("s")
#else:
 #   print("who")


match name:
    case "harry" | "ron" | "hermione":# these are or statements
        print("G")
    case "Draco":
        print("S")
    case _:#for cases not mentioned before
        print("who")
