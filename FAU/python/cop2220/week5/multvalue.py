def operation(a, b):
    addition = a + b
    multiplication = a * b
    sub = a - b
    div = a/b
    return addition, multiplication, sub, div

a,b,c,d = operation(11,2) #using mutliple variables
print(a,b,c,d)
