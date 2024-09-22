def main():
    value = get_int()
    ValueError(value)

def get_perc(a):
    if a == 1:
        print("100%")
    elif a == .75:
        print("75%")
    elif a == .5:
        print("50%")
    elif a == .25:
        print("25%")
    elif a <= .01:
        print("E")

def get_int():
    while True:
        perc = input("Fraction: ")
        x = perc.split("/")
        try:
            x = int(x[0]), int(x[1])
        except ValueError:
            pass
        else:
            return x

def ValueError(value):
    try:
        a = value[0]/value[1]
    except ValueError:
        get_int()
    else:
        get_perc(a)
main()
