def main():
    value = get_int()
    level = Valerr(value)
    gauge = too_big(level)
    get_perc(gauge)

def get_perc(a):
    if a >= .99:
        print("F")
    elif a == .75:
        print("75%")
    elif a == 2/3:
        print("67%")
    elif a == .5:
        print("50%")
    elif a == 1/3:
        print("33%")
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
        except (ValueError, ValueError):
            pass
        else:
            return x

def Valerr(value):
    while True:
        try:
            a = value[0]/value[1]
        except (ValueError, ZeroDivisionError):
            value = get_int()
        else:
            return float(a)
def too_big(b):
    while True:
        if b > 1:
            c = get_int()
            b = Valerr(c)
        else:
            return b

main()
