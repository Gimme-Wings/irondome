def main():
    difficulty = input("Difficult or Casual? ")
    if not(difficulty == "Difficult" or == "casual") #not negates the ()
     print("Enter a valid difficulty")
     return
    players = input("Multiplayer or Single-player? ")
    if not(players == "Multiplayer" or == "single-player")
        print("Enter a valid number of players")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondike")
        else:
            print("Enter a valid number of players")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single-player":
            recommend("Clock")
        else:
            print("Enter a valid number of players")



def recommend(game):
    print("You might like", game)


main()
