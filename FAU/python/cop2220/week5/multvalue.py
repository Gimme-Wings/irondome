def operation(a, b):
    addition = a + b
    multiplication = a * b
    sub = a - b
    div = a/b
    return addition, multiplication, sub, div

x = int(input())
w = int(input())
a,b,c,d = operation(x,w) #using mutliple variables
print(a,b,c,d)
