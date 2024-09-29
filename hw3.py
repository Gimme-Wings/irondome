

def get_name():
    '''get 3 names and add them to alist'''
    name_list = []
    for count,i in enumerate(range (3)):
        name = input(f"input name {count+1}: ")
        name = name.title()
        name_list.append(name)
    return name_list
def get_age():
    ''' take input of 3 ages and ask again if they are less than or equal to 0'''
    age_list = []

    for count in (range(3)):
        age = -1
        while age <= 0:
            age = int(input(f"input age {count+1}: "))
        age_list.append(age)

    return age_list
def youngest(name,age):
    '''find youngest age, which name that age belongs to,
    print who is the youngest, and check if any others are the same age'''
    youngest_age_index = age.index(min(age))
    youngest_age = age[youngest_age_index]
    youngest_name = name[youngest_age_index]
    counter = 0
   # print(f"{youngest_name} is the youngest being {youngest_age} years old")
    if age[0] == age[1] and age[0] == age[2]:
        print("no single one of them is the youngest, they are all equally young")

    else:
        print(f"{youngest_name} is the youngest being {youngest_age} years old", end = '')
        for l in range(3):
            if l == youngest_age_index:
                continue
            if age[l] == youngest_age:
                counter = counter + 1
                print(f" and {name[l]} is as young as {youngest_name} at {youngest_age} years old")
    if counter == 0:
        print()
    print("="*80)

def oldest(name,age):
    oldest_age_index = age.index(max(age))
    oldest_age = age[oldest_age_index]
    oldest_name = name[oldest_age_index]

    if age[0] == age[1] and age[0] == age[2]:
        print("no single one of them is the oldest, they are all equally old")
        print("="*80)
    else:
        print(f"{oldest_name} is the oldest, being {oldest_age} years old")

        for m in range(3):
            if m == oldest_age_index:
                continue
            if age[m] == oldest_age:
                print(f"{name[m]} is as old as {oldest_name} at {oldest_age} years old")
        print("=" * 80)
def main():
    name_list = get_name()
    print(name_list)
    age_list = get_age()
    print(age_list)
    youngest(name_list,age_list)
    oldest(name_list,age_list)

main()
