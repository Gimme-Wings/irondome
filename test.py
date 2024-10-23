def append_and_double(numbers):
    numbers.append(5)#add 5 into the end of the list as an int
    numbers = [digit*2 for digit in numbers]#use a list comprehension to double each element
    print(numbers)#print the list
def list_input():
    numbers = []# create a list
    split_number_input = input("input numbers divided by a space on one line then press enter: ").split() #get input and split it 
    for number in split_number_input:#for every number in the list
        numbers.append(int(number))#append the number as an int
    return numbers#return the list to main
def main():
    numbers = list_input() # call on list_input to get input of all the numbers on one line
    #get numbers as a list
    append_and_double(numbers)#give numbers to append_and double as input
main()