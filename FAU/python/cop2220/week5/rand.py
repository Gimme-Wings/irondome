def main():
    b = int(input("num"))
    prime(b)


def prime(b):
    for n in range (1,b+1):
        print(n, n % 1)

main()
