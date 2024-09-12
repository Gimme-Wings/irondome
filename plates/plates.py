def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    letters(s)

def letters(l):
    numbers = list(l)
    if numbers in l[1:2]:
        return False
    else:
        return True

main()
