text = input("Input: ")

while i in range(len(text)):
    for j in text:
        if j == "a":
            continue
        else:
            print(f"output {j}")
        break
