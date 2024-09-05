def main():
    y = ask_height()
    x = ask_length()
    print_brick(x, y)

def ask_height():
    height = int(input("whats the height? "))
    return height


def ask_length():
    length = int(input("whats the length? "))
    return length

def print_brick(length, height):
    for _ in range[height]:
        print("#")
