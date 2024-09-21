def main():
    b = int(input("num: "))
    prime(b)


def prime(b):
    fact = 0
    for n in range (1,b+1):
        if (b%n ==0):
            fact = fact + 1
    if fact == 2:
        print("prime")
    else:
        print("not prime")

main()
