# Draw 7
# Stuarrt 12/31/2022
# This program will have an area for the user to enter in the cards in thier
#   deck along with the ammount of energys they have, the program will draw
#   seven cards at random from the deck to help determine  future draws. 

import Draw_Seven_Main

def main():
    userQ1 = ""
    while userQ1 != "q":
        userQ1 = input("Do you have a previous deck to load? Type (y) for yes or (n) for no\n Type (q) to quit\n ")
        userQ1.lower()
        if userQ1 == "y":
            deckName = input("Please enter a deck name to load:")
            if os.path.exists(deckName):
                with open(deckName, "rb") as f:
                    deckList = pickle.load(f)
                    cardCount = len(deckList)
                    Draw_Seven_Main.drawSevenCards(deckList)
            else:
                print("Sorry did you enter your deck name right? I couldn't find ", deckName)
        elif userQ1 == "n":
            Draw_Seven_Main.deckCreation()
        else:
            print("Did you type (y), (n) or (q)? Try again.")

main()