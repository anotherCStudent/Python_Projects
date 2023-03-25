# Draw_Seven_Main
# Stuarrt 12/31/2022
# This is the underlying code behind the draw seven program.

import os
import pickle
import random

def drawSevenCards(deck):
    viewDeck = input("Do you want to view your decklist? Please enter (y) or (n):")
    viewDeck.lower()
    if viewDeck == "y":
        print(deck)
    elif viewDeck == "n":
        pass
    else:
        pass

    while True:
        keepGoing = input("These are the seven cards you would draw. Type (q) to quit.")
        if keepGoing == "q":
            break
        
        drawSeven = random.sample(deck, 7)
        print("The cards you drew were\n", drawSeven)


def deckCreation():
    
    deckList = []
    cardCount = 0

    while True:
        cardInput = input("Please enter the name of your card, don't enter energys. Type (s) to Stop")
        cardInput.lower()
        if cardInput == "s":
            energys  = (60 - cardCount)
            deckList += [("energys=" + str(energys))] * energys
            break

        cardName = f"card{cardCount}"
        globals()[cardName] = cardInput

        deckList.append(cardName)

        cardCount += 1

    saveDeckAs = input("Do you want to save the deck? Type (y) or (n)")
    saveDeckAs.lower()
    if saveDeckAs == "y":
       deckName = input("Please enter a name for your deck")
       with open(f"{deckName}.pkl", "wb") as f:
            pickle.dump(deckList, f)
            print(f"Deck saved as {deckName}.pkl")
    elif saveDeckAs == "n":
        print("Deck not saved, continuing on...")
    else:
        print("Sorry, did you enter (y) or (n)")
    drawSevenCards(deckList)