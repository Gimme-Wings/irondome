#dictionaries are more 2d using lists
students = {
    "hermione": "gryf",
    "harry":"gryf",
    "ron":"gryf",
    "draco":"slyth",
}
#name = input("what name? ")
#print(students[name])    #can use words to index
# or

#for student in students:     #this iterates only the keys(names of kids)
   # print(student)
for i in students:
    print(i,students[i], sep=", ") #first prints the i which is the key and then it calls the dictionary by i position
