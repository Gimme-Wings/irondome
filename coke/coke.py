cost = int(50)


while cost > 0:
    while True: #induce a forvever loop
        n = int(input("Insert coin: "))
        if (n != 25) and (n!= 10) and (n!=5):
            continue
        else:
            print(f"Amount Due: {n}")
            break

