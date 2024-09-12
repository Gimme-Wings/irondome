def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    letters(s)

def letters(l):
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    first_number = l.find(numbers)
    print(first_number)
main()
