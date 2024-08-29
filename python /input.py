def greet (input):
    if "Hello" or "hello" in input:
        return ("Whats going on, ")#or print it
    else:
        return 0

def main():
    ask =  input("if you want to start, type hello: ")
                              #store is storing the value return through greet/input it can be accesed later
    store = greet(ask) #this is the input thats referenced above
    if store == ('Whats going on, '):
        name = input("whats your name? ")
        name= name.title()
#can use stored value to add to it
    print("Hey, " + store + name + "?")


main()
