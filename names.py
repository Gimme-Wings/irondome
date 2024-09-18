name_one = "a"
name_two = "b"
name_three = "c"
age_one = 10
age_two = 14
age_three = 6
length = 3
name_list = [name_one, name_two, name_three]
age_list = [age_one, age_two, age_three]
for i in range(length):
    name = name_list[i]
    age = age_list[i]

    if age > 0 and age <=12:
        print(f"{name} is a child")
    elif age >=13 and age <=18:
        print(f"{name} is a teen")
