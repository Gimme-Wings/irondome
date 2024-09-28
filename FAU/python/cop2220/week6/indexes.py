numbers = []
for i in range(10):
    x = int(input())
    numbers.append(x)
print(f"{numbers} is the list")
#to find position of a certain number
def get_element (n,numbers):
    result = []
    indexes = []
#enumerate finds position of a thing when true
#it creates a tuple
    for idx, e in enumerate(numbers):
        if e == n:
            result.append(e)
            indexes.append(idx)
    return result, indexes

sub_list, indexed = get_element(2,numbers)
print(f"{sub_list} is what was received and how many times it saw 2")
print(f"{indexed} is position of 2")
