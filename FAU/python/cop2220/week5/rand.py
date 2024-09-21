def main():
    b = int(input())
    a=prime(b)
    if a >25:
        pass
    else:
        print(a)

def prime(b):
    if b % b == 1 and b % 1 == b:
        return b
