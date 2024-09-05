numbers = input("Expression: ")


x = numbers.find(" ")
w = float(numbers[0:x])

y = (numbers[x+1])

z = float(numbers[x+3:])

if "+" in y:
    print(w + z)
elif "-" in y:
    print(w - z)
elif "*" in y:
    print(w * z)
elif "/" in y:
    if z != 0:
        print(w / z)
    else:
        print("undefined")
