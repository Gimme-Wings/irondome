def hello (to="world"):
    print("Hello", to) #if nothing is enetered then it assumes to is world otherwise its name

hello()
name = input("whats your name? ")
name= name.title()
hello(name)
