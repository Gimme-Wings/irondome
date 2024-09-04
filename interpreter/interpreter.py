numbers = input("Expression: ")


x = float(numbers[0:" "])

y = (numbers[2])

z = float(numbers[4])

if "+" in y:
    print(x + z)
elif "-" in y:
    print(x - z)
elif "*" in y:
    print(x * z)
elif "/" in y:
    if z != 0:
        print(x / z)
    else:
        print("undefined")
