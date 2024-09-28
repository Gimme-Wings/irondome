my_list = [1,2,3]
#append
my_list.append(100)
numbers = []
for n in range(10):
    x = int(input())
    numbers.append(x)

w = numbers.index(100)
w = w+1#to get position in actual list

#check how many time a number is in a list
r = numbers.count(3)
#or
def get_number(n,my_list):
    result=[]
    for e in my_list:
        if e == n:
            result.append(e)
    return result
print(f"{get_number(2,numbers)} is get_number")
print(f"{my_list} is my list")
print(f"{numbers} is numbers")
print(f"{w} is position of 100")
print(f"{r} is the amount of times 3 appears")
