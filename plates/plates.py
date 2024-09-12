def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    letters(s)

def letters(l):
    first_number = l.find('0' or '1')
    print(first_number)
main()
