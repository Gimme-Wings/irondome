def get_guess():
    guess=int(input("guess: "))#can do without int but the checking == below has to be "50"
    return guess

def main():
    guess= get_guess()
    if guess == 50: # if checking a number ask for int above
        print("correct")
    else:
        print("incorrect")

main()
