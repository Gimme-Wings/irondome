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
    while spaces > 0:
        #i is the first digit
        for i in l:
            for j in number_list:
                if i == j:
                    break
                else:
                    #spaces is where it is in the word
                    spaces = spaces +1
                    spaces = spaces %10

        


main()
