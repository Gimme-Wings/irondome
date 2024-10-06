#trad list making
text = "hello world"
my_list = []
for letter in text:
    my_list.append(letter)
print(my_list)

#new way
my_list2 = [letter for letter in text]
print(my_list2)

my_list3 = [letter*2 for letter in text]
print(my_list3)

square = []
for n in range(1,21):
    square.append(n**2)
print(square)

square1 = [num**2 for num in range(1,21)]
print(square1)
