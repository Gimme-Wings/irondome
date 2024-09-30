def get_lab_grades():
    lab_list = []
    x = -1
    while x< 0:
        x = int(input("how many labs will you be inputting"))
    for count in (range(x)):
        grade = -1
        while grade <= 0:
            grade = int(input(f"input grade {count+1}: "))
        lab_list.append(grade)

    return lab_list
def get_hw_grades():
    hw_list = []
    x = -1
    while x< 0:
        x = int(input("how many homeworks will you be inputting"))
    for count in (range(x)):
        grade = -1
        while grade <= 0:
            grade = int(input(f"input grade {count+1}: "))
        hw_list.append(grade)
    return hw_list

def get_quiz_grades():
    quiz_list = []
    x = -1
    while x< 0:
        x = int(input("how many quizzes will you be inputting"))
    for count in (range(x)):
        grade = -1
        while grade <= 0:
            grade = int(input(f"input grade {count+1}: "))
        quiz_list.append(grade)
    return quiz_list

def get_exam_grades():
    exam_list = []
    x = -1
    while x< 0:
        x = int(input("how many exams will you be inputting"))
    for count in (range(x)):
        grade = -1
        while grade <= 0:
            grade = int(input(f"input grade {count+1}: "))
        exam_list.append(grade)
    return exam_list

def weight_list():
    weight = [0.1,0.3,0.1,0.5]
    return weight
def average(assignment,add):
    length_assignment = len(assignment)
    average = add/length_assignment
    return average
def compute_grade(lab,hw,quiz,exam,weight):
    weight_avg = 0
    assignments_grade =
    for count,m in enumerate(assignments_grade):
        add = 0
        for i in m:
            #add become equal to all the grades in a assignment category
            add = add + i
        avg = average(m,add)#m is assignment_grade in a specific category
        weight_avg = weight_avg + (avg * weight[count])
    print(f"{weight_avg:.2f} is the final grade based on the inputs received")
def main():
    lab = get_lab_grades()
    hw = get_hw_grades()
    quiz = get_quiz_grades()
    exam = get_exam_grades()
    weight = weight_list()
    print(lab,hw,quiz,exam,weight)
    compute_grade(lab,hw,quiz,exam,weight)
main()
