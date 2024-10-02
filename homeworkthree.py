def get_name():
    '''get 3 names and add them to a list'''
    #create an empty list
    name_list = []
    #start a loop to get 3 names
    for count in (range (3)):
        name = ""
        #if length of name is 0 or less ask again for a name
        while len(name) <= 0 :
            name = input(f"input name {count+1}: ")
        #capitalize the name
        name = name.title()
        #append the name to the list
        name_list.append(name)
    #return the list to main
    return name_list
def get_age():
    ''' take input of 3 ages and ask again if they are less than or equal to 0'''
    #create an empty list
    age_list = []
    #start a loop of length 3 to find ages
    for count in (range(3)):
        age = -1
        #force the while loop to start to find ages
        while age <= 0:
            age = int(input(f"input age {count+1}: "))
        #append it to age_list
        age_list.append(age)
        #return to the main function
    return age_list
def youngest(name,age):
    '''find youngest age, which name that age belongs to,
    print who is the youngest, and check if any others are the same age'''
    #check index of youngest age using min
    youngest_age_index = age.index(min(age))
    #use that index to find the youngest age as a number
    youngest_age = age[youngest_age_index]
    #find the name of youngest person
    youngest_name = name[youngest_age_index]
    counter = 0
    #if all are equal age print all equally young and move on past the else statement
    if age[0] == age[1] and age[0] == age[2]:
        print("no single one of them is the youngest, they are all equally young")
        counter = 1
    else:
        #find either 1 or 2 of the youngest people if applicable
        print(f"{youngest_name} is the youngest being {youngest_age} years old", end = '')
        for l in range(3):
            #if l is the same as the index of youngest person go back and iterate the next item
            if l == youngest_age_index:
                continue
                #if found to be equal enter and print they are as young as the first person that was found
            if age[l] == youngest_age:
                counter = counter + 1
                print(f" and {name[l]} is as young as {youngest_name} at {youngest_age} years old")
    #if only person person found to be youngest print a line to avoid printing on the same line as  print("="*80)
    if counter == 0:
        print()
    print("="*80)

def oldest(name,age):
    '''same as youngest() but using max instead of min'''
    #check index of oldest age
    oldest_age_index = age.index(max(age))
    #check age of oldest ages
    oldest_age = age[oldest_age_index]
    #find the name of oldest age
    oldest_name = name[oldest_age_index]
    counter = 0
    #if age all equal enter loop and dont go to the else loop
    if age[0] == age[1] and age[0] == age[2]:
        print("no single one of them is the oldest, they are all equally old")
        counter = 1
    #if ages are not equal then find oldest person and if neccesary append a second person as being as old as the first
    else:
        print(f"{oldest_name} is the oldest, being {oldest_age} years old", end = '')

        for m in range(3):
            if m == oldest_age_index:
                continue
            if age[m] == oldest_age:
                counter = counter +1
                print(f" and {name[m]} is as old as {oldest_name} at {oldest_age} years old")
    #if only one person is oldest, then the print("=" *80) will print on the same line as the first print line

    if counter == 0:
        print()
    #separate out the parts of the exercise
    print("=" * 80)

def category(name,age):
    '''find age category using if elif statements'''
    #check what category the person being passed into the function fits into
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

print("-" *80)

def get_lab_grades():
    '''Get and return lab grades in a list using a while and for loop'''
    #create a list called lab_list
    lab_list = []
    x = -1
    #force the while loop to start and ask how many labs will be input
    while x< 0:
        x = int(input("how many labs will you be inputting"))
    #start a loop of length x, which is how many labs will be input
    for count in (range(x)):
        grade = -1
        #get grade one at a time
        while grade < 0:
            grade = float(input(f"input grade {count+1}: "))
       #add it to the list
        lab_list.append(grade)
       #return this list to main_function
    return lab_list

def get_hw_grades():
    '''Get and return HW grades in a list using a for and while loop'''
    #the line by line is the same as get_lab_grades()
    #please refer to get_lab_grades() for comments
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
     #the line by line is the same as get_lab_grades()
    #please refer to get_lab_grades() for comments
    '''Get and return quiz grades in a list using a while and for loop'''
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
     #the line by line is the same as get_lab_grades()
    #please refer to get_lab_grades() for comments
    '''Get and return exam grades in a list using a while and for loop'''
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
    '''Return weight of assignment category in a list'''
    #create a list that was given in the assignment and return it
    weight = [0.1,0.3,0.1,0.5]
    return weight

def compute_grade(lab,hw,quiz,exam,weight):
    '''Take grades, get the average then weight them and print final grade'''
    #create final grade to store the final grade
    final_grade = 0
    #create a list of all the lists that have been received
    assignments = [lab,hw,quiz,exam]
    #start a loop the length of 4 and enumerate which iteration the program is on
    for count,grade in enumerate(assignments):
        add = 0
        #for each value in the list being itearated take it and add it
        for i in grade:
            #add become equal to all the grades in a assignment category
            add = add + i
        #call on average() to get the avrage of a category
        avg = average(grade,add)#grade is assignment in a specific category
        #add avg on each pass of the loop to add to final grade
        final_grade = final_grade + (avg * weight[count])
    #print the final_grade
    print(f"{final_grade:.2f}% is your final grade")

def average(assignment,add):
    '''calculate average of a grading category'''
    #calculate the length of the assignment being passed
    length = len(assignment)
    #if the length is 0 then return 0 so the final grade is calculated correctly
    if length == 0:
        return 0
    #if not 0 calculate the average using the sum of a category and divide it by the length
    else:
        average = add/length
    #return the category average
    return average

def main():
    lab = get_lab_grades()
    hw = get_hw_grades()
    quiz = get_quiz_grades()
    exam = get_exam_grades()
    weight = weight_list()
    compute_grade(lab,hw,quiz,exam,weight)
main()
