cost = 50
cost = int(cost)

while cost > 0:
    while True: #induce a forvever loop
        n = int(input("Insert coin: "))
        if (n != 25) or (n!= 10) or (n!=5):
            continue
        else:
            print(f"Amount Due: {n}")
            break

