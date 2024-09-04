numbers = input("Expression: ")


x = float(numbers[0])

y = (numbers[2])

z = float(numbers[4])

if "+" in y:
    print(x + y)
elif "-" in y:
    print(x - y)
elif "*" in y:
    print(x * y)
elif "/" in y:
    if y != 0:
        print(x / y)
    else:
        print("undefined")
