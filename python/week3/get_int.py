def main():
    

def get_int():
    while True:
        try:
            x = int(input("whats x"))
        except ValueError:
            print("x is not an int")
        else:
            break
    return x
