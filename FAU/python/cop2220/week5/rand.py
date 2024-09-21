def main():
    b = int(input("num: "))
    prime(b)


def prime(b):
    for n in range (1,b+1):
        if (b%n ==0):
            print(n)

main()
