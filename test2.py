def name_manipulation():
    #take name as input, call it name
    name = input("please input your full name? ")
    #use upper() str method to capitalize the entire string
    #print the name.upper()
    print(name.upper())
    #split the name into 2 strings, first and last name
    first,last = name.split()
    #print the first name capitzalized, 
    #add a space and end= '' so the last name print on the same line
    print(first.capitalize() + " ",end='')
    #print the last name capitalized
    print(last.capitalize())
    #returns nothing
def main():
    #call on name_manipulation function
    name_manipulation()
#call on main
main()