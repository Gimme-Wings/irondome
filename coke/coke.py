cost = int(50)


while cost > 0:
    while True: #induce a forvever loop
        print(f"Amount Due: {cost}")
        n = int(input("Insert coin: "))
        if (n != 25) and (n!= 10) and (n!=5):
            continue
        else:
            if (cost-n)<0:
                print(f"Change Owed: {n-cost}")
            if( cost-n)>0:
                cost = cost - n
                print(f"Amount Due: {cost}")
            break

