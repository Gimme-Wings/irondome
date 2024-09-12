def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if 2 <= length <= 6:
        return letters(s)

def letters(l):
    for i in l:
        print(type(l))

main()
