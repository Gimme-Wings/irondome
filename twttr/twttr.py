text = input("Input: ")
length = len(text)
print("Output: ", end ='')
while length > 0:
        for i in text:
            if (i == "a") or( i == "A") or (i=="i") or (i=="I") or (i == "o") or (i == "O") or (i == "u") or (i == "U") or (i == "e") or (i == "E") :
                length = length -1
                continue
            else:
                print(f"{i}", end ='')
                length = length - 1

print()

