def get_guess():
    guess=int(input("guess: "))
    return guess

def main():
    guess= get_guess()
    if guess == 50: # if checking a number ask for int above
        print("correct")
    else:
        print("incorrect")

main()
