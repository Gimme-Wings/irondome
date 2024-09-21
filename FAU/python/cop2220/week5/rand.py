def main():
    for i in range(1000):
        b = i
        is_prime(b)


def is_prime(b):
    fact = 0
    for n in range (1,b+1):
        if (b%n ==0):
            fact = fact + 1
    if fact == 2:
        print(f"{b} is prime")
    else:
        print(f"{b} is not prime")

main()
