def z_input():
    #take input as a string not to raise an error if the use accidently attaches the z to the front
    z_number = (input("please input your entire z number: "))
    #check if the first element is a letter using .isalpha
    if z_number[0].isalpha():
        #if it is a letter assign z_number just from the second element to the end
        z_number= z_number[1:]
        #return just the entire z number as an str
        return z_number
    else:
        #return the whole z number as a str
        return z_number
def sum_of_digits(z_number):
    sum = 0#initialise sum to 0 so it can added to
    for number in z_number:#add the entire z number as an int
        sum += int(number)
    print(sum, end = '')#print the sum and end = '' to print even or odd on the same line
    #if the sum leaves no remainder its even so print even
    if  sum %2 == 0:
        print(" is even")
    #if the sum leaves a remainder prints odd
    else:
        print(" is odd")
def main():
    z_number = z_input()#call on z_input to get the whole z number
    sum_of_digits(z_number)#input that into sum_of digits to get the sum
main()