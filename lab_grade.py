def get_lab_grades():
    lab_grade = []
    lab_grade_list = ''
    lab_list = []
    space_index = [0]
    while len(lab_grade_list)<1:
        lab_grade_list = input("input lab grades separated by a space")
        lab_grade_list = lab_grade_list.lstrip().rstrip()

    for i,e in enumerate(lab_grade_list):
        if e == " ":
            space_index.append(i)
    for i in space_index:
        if i == 0:
            pass
        else:
            x = lab_grade_list[i-1:i]
            lab_grade.append(x)
        #use space index to get the numbers separately and then put them in a list
    print(lab_grade_list)
    print(len(space_index))
    print(space_index)
    print(lab_grade)
    return lab_grade_list
def main():
    get_lab_grades()
main()

