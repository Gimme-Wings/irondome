def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    letters(s)

def letters(l):
    first_number = l.find('0')
    print(first_number)
    if first_number > 2:
        return True
    else:
        return False
main()
