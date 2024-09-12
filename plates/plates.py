def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    letters(s)

def letters(l):
    first_number = l.find('0' or '1' or '2' or '3' or '4' or '5')
    print(first_number)
    if first_number > 2:
        return True
    else:
        return False
main()
