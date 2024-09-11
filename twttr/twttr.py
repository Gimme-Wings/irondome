text = input("Input: ")
length = len(text)
while length > 0:
    for i in text:
        if i == "a":
            continue
        else:
            print(f"{i}", end ='')
            length = length - 1
        break
