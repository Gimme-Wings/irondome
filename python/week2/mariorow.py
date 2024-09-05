def main():
   x = width()
   print_row(x)

def print_row(width):
    print("?" * width)

def width():
    x = int(input("how long is the row? "))
    return x

main()

