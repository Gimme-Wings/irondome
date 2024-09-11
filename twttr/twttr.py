text = input("Input: ")
print(len(text))
for i in range(len(text)):
    for j in text:
        if j == "a":
            continue
        else:
            print(f"output {j}")
        break
