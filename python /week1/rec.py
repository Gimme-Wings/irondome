def main():
    difficulty = input("Difficult or Casual? ")
    if not(difficulty == "Difficult" or difficulty == "casual"): #not negates the ()
     print("Enter a valid difficulty")
     return
    players = input("Multiplayer or Single-player? ")
    if not(players == "Multiplayer" or players == "single-player"):
        print("Enter a valid number of players")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
            recommend("Poker")
    elif difficulty == "difficult" and players == "Single-player":
            recommend("Klondike")

    elif difficulty == "Casual" and players == "Multiplayer":
            recommend("Hearts")
    elif difficulty == "Casual" and players == "Single-player":
            recommend("Clock")




def recommend(game):
    print("You might like", game)


main()
