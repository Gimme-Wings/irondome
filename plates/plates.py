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
        for i in number_list:
            first_number = l.find(number_list)
            length = length -1
    if first_number <= 2:
        return False
    else:
        return True


    if first_number > 2:
        return True
    else:
        return False
main()
