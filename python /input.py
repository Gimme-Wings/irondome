def greet (input):
    if "hello" in input:
        return ("whats going on ")#or print it
    else:
        return ("IDK")
#store is storing the value return through greet/input it can be accesed later
store = greet("hello") #this is the input thats referenced above
if store == ('whats going on '):
    name = input("whats your name? ")
    name= name.title
#can use stored value to add to it
print("hey " + store + name)
