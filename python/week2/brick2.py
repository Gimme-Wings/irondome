def main():
    x = int(input("size": ))
    print_square(x)

def print_square(size):

    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)

main()
