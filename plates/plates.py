def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if 2<= length <=6:
        letters(s, length)
    else:
        return False

def letters(l, length):
    number_list = ("123456890")
    while length > 0:
        for numb in l:
            if numb == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 0):
                    first_number = l.find(numb)

            length = length -1

            if first_number >= '2':
                return False
            else:
                return True


main()
