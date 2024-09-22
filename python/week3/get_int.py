def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("whats x "))
        except ValueError:
            pass #just keep on going in the loop
            #print("x is not an int")
        #else:
            #return x #this is equal to a break
main()
