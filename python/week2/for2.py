def main():
    names = ["mario", "luigi", "daisy", "yoshi"]

    for i in range(len(names)): # i is being iterated
        print(i)

    for i in range(len(names)):
        print( write_letter(names[i], "princess"))

def write_letter(receiver, sender):
    return f""" Dear {receiver},
come to the party.
sincerely,
{sender}

"""


main()
