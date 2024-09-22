def main():
    x = get_int("whats x? ")
    print(f"x is {x}")

def get_int(prompt):#using prompt to know what to show not to confuse
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass #just keep on going in the loop
            #print("x is not an int")
        #else:
            #return x #this is equal to a break
main()
