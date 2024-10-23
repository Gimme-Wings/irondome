def get_list():
    numbers = []# create a list of length 0
    while len(numbers)< 5:#force the loop to start because the length is initially 0
        split_number_input = input("input: ").split()#take input and split it
        for number in split_number_input:#iterate over each number in split_number
            if len(numbers)<5:#if the length is 0 like how we started, then append the first 5, because even if 6 are input
                #the length of numbers after 5 numbers will stop the if statement. after 5 if statements len(numbers) would be false 
                number = float(number)#take the current number and convert it into a float
                number = number //1#if its a decimal then take away anything after the decimal point
                numbers.append(int(number))#append the remaining whole number as an int into numbers
    return numbers#return the list of whole numbers
def binary(numbers):#get the list of whole numbers
    for num in numbers:
        print(f"Decimal: {num},",end = '')#print decimal and the current number being iterated, 
        #and use end = '' so the next print will be on the same line
        if num == 0:# if the num is 0 then just print the binary is also 0
            print(f" binary: {0}")
        else:#if its not 0 
            y = ''#create a variable called y
            while num >0:#while the current number is greater than 0 enter the loop
                rem = num%2#get the remainder after dividing by 2
                y = str(rem) + y#add that to the front of y
                num = num//2#floor divide the number so it becomes 0 and makes the while loop false 
                #so it moves to the next number in the list
            print(f" Binary: {y}")

def main():
    numbers = get_list()#get a list of whole numbers to pass into binary
    binary(numbers)#get the number without decimal and get the binary number
main()
