text = input("Input: ")

for i in len(text):
    for j in text:
        if j == "a":
            continue
        else:
            print(f"output {j}")
        break
