my_list1 = [1,2,3,4]
my_list2 = my_list1
#not how to copy, its just a reference to list1
print(my_list1)
my_list2 = my_list1.copy()
my_list1 = my_list1.append(100)
print(my_list2)
print(my_list1)
