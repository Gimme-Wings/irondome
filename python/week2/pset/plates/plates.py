def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid", end ='')
    else:
        print("Invalid")


def is_valid(s):

    length = len(s)
    if 2 <= length <= 6:
        if letters(s):

            if punct(s):
                return let_aft(s,length)
            else:
                return False



def letters(l):
    number_list = ("012345689")
    spaces = 0
    flag = False
    # i is the first digit
    for i in l:
        for j in number_list:
            if i == j:
                flag = True
                break
            else:
                # spaces is where it is in the word
                spaces = spaces + 1

        if flag:
            break
    spaces = spaces // 10
    if (spaces < 1) or (j == '0'):
        return False
    else:
        return True

def punct(pu):
    number_list = (".,/';:")
    spaces = 0
    flag = False
    # i is the first digit
    for i in pu:
        for j in number_list:
            if i == j:
                flag = True
                break
            else:
                # spaces is where it is in the word
                spaces = spaces + 1

        if flag:
            break
    spaces = spaces // 7

    if flag:
        return False
    else:
        return True

def let_aft(k,length):

    diglet_list = []
    for i in k:
            if i.isdigit():
                diglet_list.append('dig')
            else:
                diglet_list.append('str')
    for m in range(length-1):
        if (diglet_list[m] == 'dig') and (diglet_list[m+1] == 'str'):
            return False
    else:
        return True




main()
