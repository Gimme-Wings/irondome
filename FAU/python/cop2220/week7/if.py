list1 = [1,12,2,20,3,15,4]
list2 = [item for item in list1 if item < 10]

#for n in list1:
    #if n <10:
       # list2.append(n)
print(list2)

list3 = [n for n in range(0,20) if n%2 == 0]
print(list3)

list4 = [n for n in list1 if n<10]
print(list4)

