def get_name():
    '''get 3 names and add them to a list'''
    name_list = []
    for count in (range (3)):
        name = ""
        while len(name) <= 0 :
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

    if age[0] == age[1] and age[0] == age[2]:
        print("no single one of them is the youngest, they are all equally young")
        counter = 1
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
    '''same as youngest() but using max instead of min'''
    oldest_age_index = age.index(max(age))
    oldest_age = age[oldest_age_index]
    oldest_name = name[oldest_age_index]
    counter = 0

    if age[0] == age[1] and age[0] == age[2]:
        print("no single one of them is the oldest, they are all equally old")
        counter = 1
    else:
        print(f"{oldest_name} is the oldest, being {oldest_age} years old", end = '')

        for m in range(3):
            if m == oldest_age_index:
                continue
            if age[m] == oldest_age:
                counter = counter +1
                print(f" and {name[m]} is as old as {oldest_name} at {oldest_age} years old")
    if counter == 0:
        print()
    print("=" * 80)

def category(name,age):
    '''find age category using if elif statements'''
    for n in range(3):
        if age[n]>=1 and age[n] <= 12:
            print(f"{name[n]} is a child")
        elif age[n] >= 13 and age[n] <=19:
            print(f"{name[n]} is a teen")
        elif age[n] >=20 and age[n] <=64:
            print(f"{name[n]} is an adult")
        elif age[n] >=65:
            print(f"{name[n]} is a senior")

def main():
    name_list = get_name()
    age_list = get_age()
    youngest(name_list,age_list)
    oldest(name_list,age_list)
    category(name_list,age_list)

main()

print(80*"-")

def get_lab_grades():
    lab_list = []
    x = -1
    while x< 0:
        x = int(input("how many labs will you be inputting"))
    for count in (range(x)):
        grade = -1
        while grade < 0:
            grade = float(input(f"input grade {count+1}: "))
        lab_list.append(grade)

    return lab_list

def get_hw_grades():
    hw_list = []
    x = -1
    while x< 0:
        x = int(input("how many homeworks will you be inputting"))
    for count in (range(x)):
        grade = -1
        while grade < 0:
            grade = float(input(f"input grade {count+1}: "))
        hw_list.append(grade)
    return hw_list

def get_quiz_grades():
    quiz_list = []
    x = -1
    while x< 0:
        x = int(input("how many quizzes will you be inputting"))
    for count in (range(x)):
        grade = -1
        while grade < 0:
            grade = float(input(f"input grade {count+1}: "))
        quiz_list.append(grade)
    return quiz_list

def get_exam_grades():
    exam_list = []
    x = -1
    while x< 0:
        x = int(input("how many exams will you be inputting"))
    for count in (range(x)):
        grade = -1
        while grade < 0:
            grade = float(input(f"input grade {count+1}: "))
        exam_list.append(grade)
    return exam_list

def weight_list():
    weight = [0.1,0.3,0.1,0.5]
    return weight

def compute_grade(lab,hw,quiz,exam,weight):
    final_grade = 0
    assignments = [lab,hw,quiz,exam]
    for count,grade in enumerate(assignments):
        add = 0
        for i in grade:
            #add become equal to all the grades in a assignment category
            add = add + i
        avg = average(grade,add)#m is assignment_grade in a specific category
        final_grade = final_grade + (avg * weight[count])
    print(f"{final_grade:.2f}% is your final grade")

def average(assignment,add):
    length = len(assignment)
    if length == 0:
        return 0
    else:
        average = add/length
    return average

def main():
    lab = get_lab_grades()
    hw = get_hw_grades()
    quiz = get_quiz_grades()
    exam = get_exam_grades()
    weight = weight_list()
    compute_grade(lab,hw,quiz,exam,weight)
main()
