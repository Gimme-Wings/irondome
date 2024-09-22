while True:
    try: # the value is not copied into x because theres an error in int
        x = int(input("whats x? "))#could add break below this line, if nothing goes wrong
        #if error happens it jumps to except
    except ValueError:
        print("x is not an integer")
    else: #else is related to except not working
        break #need to stop the loop
print(f"x is {x}")
