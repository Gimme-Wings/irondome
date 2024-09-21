def main():
    for i in range(100):
        b = i
        is_prime(b)
        #print(true(b))

def is_prime(b):
    fact = 0
    for n in range (1,b+1):
        if (b%n ==0):
            fact = fact + 1
    if fact == 2:
        print(f"{b} is prime")
    else:
        pass
        #print(f"{b} is not prime")
def true(num):
    factors = 0
    result = False
    for n in range(1, num+1):
        if num%n == 0:
            factors = factors +1
    if factors<=2:
        result = True
    return result

main()
