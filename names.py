name_one = "a"
name_two = "b"
name_three = "c"
age_one = 10
age_two = 12
age_three = 6

name_list = [name_one, name_two, name_three]
age_list = [age_one, age_two, age_three]
for name in name_list:
    for num in range(3):
        for age in age_list:
            if age >=0 and age <= 12:
                print(f"{name[num]} is a child")
