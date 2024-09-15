number = int(input(""))
if number %3 ==0:
    if number %5 ==0:
        print("div by 3 and 5")
    else:
        print("div by 3 and not 5")
else:
    print("not divisible by 3")
