import random
"""
***Shuffling a Deck of Cards***

A standard deck of playing cards contains 52 cards. Each card has one of four suits
along with a value. The suits are normally spades, hearts, diamonds and clubs while
the values are 2 through 10, Jack, Queen, King and Ace.
Each playing card can be represented using two characters. The first character is
the value of the card, with the values 2 through 9 being represented directly. The
characters “T”, “J”, “Q”, “K” and “A” are used to represent the values 10, Jack,
Queen, King and Ace respectively. The second character is used to represent the suit
of the card. It is normally a lowercase letter: “s” for spades, “h” for hearts, “d” for
diamonds and “c” for clubs. The following table provides several examples of cards
and their two-character representations.

Card                             Abbreviation
Jack of spades           Js
Two of clubs             2c
Ten of diamonds          Td
Ace of hearts            Ah
Nine of spades           9s

Begin by writing a function named create_deck. It will use loops to create a
complete deck of cards by storing the two-character abbreviations for all 52 cards
into a list. Return the list of cards as the function’s only result. Your function will
not take any parameters.
Write a second function named shuffle that randomizes the order of the cards
in a list. One technique that can be used to shuffle the cards is to visit each element
in the list and swap it with another random element in the list. You must write your
own loop for shuffling the cards. You cannot make use of Python’s built-in shuffle
function.
Use both of the functions described in the previous paragraphs to create a main
program that displays a deck of cards before and after it has been shuffled. Ensure
that your main program only runs when your functions have not been imported into
another file. (edited)

***Dealing Hands of Cards***

In many card games each player is dealt a specific number of cards after the deck
has been shuffled. Write a function, deal, which takes the number of hands, the
number of cards per hand, and a deck of cards as its three parameters. Your function
should return a list containing all of the hands that were dealt. Each hand will be
represented as a list of cards.
When dealing the hands, your function should modify the deck of cards passed
to it as a parameter, removing each card from the deck as it is added to a player’s
hand. When cards are dealt, it is customary to give each player a card before any
player receives an additional card. Your function should follow this custom when
constructing the hands for the players.
Use your solution to Exercise 3 to help you construct a main program that
creates and shuffles a deck of cards, and then deals out four hands of five cards each.
Display all of the hands of cards, along with the cards remaining in the deck after
the hands have been dealt.
"""

def create_deck():
    numbers = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    suit = ["s","h","d","c"]
    pack = []
    counter = 0    
    while counter < 104:
        for nr in numbers:
            for st in suit:
                pairs = nr + st
                counter += len(pairs)                 
                pack.append(pairs)
    return pack                

def shuffle():
    pack = create_deck()
    shuffled_pack = []
    counter = 0
    while counter < 104:        
        shuffled_card = random.choice(pack)
        counter += len(shuffled_card)
        shuffled_pack.append(shuffled_card)
    return shuffled_pack
           
print(f"This is the deck :\n{create_deck()}")
print(f"This is the shuffled deck:\n{shuffle()}")
deck = shuffle()
deck_lenght = len(deck)
print(f"Deck lenght: {deck_lenght}")

# def deal(hand, cards, deck):
deck = shuffle()  
hand_1 = []
hand_2 = []
hand_3 = []
hand_4 = []
updated_deck = []
while len(hand_1) < 4:
    
    shuffled_card = random.choice(deck)
    hand_1.append(shuffled_card)
    deck.remove(shuffled_card)
    shuffled_card2 = random.choice(deck)
    hand_2.append(shuffled_card2)
    deck.remove(shuffled_card2)
    shuffled_card3 = random.choice(deck)
    hand_3.append(shuffled_card3)
    deck.remove(shuffled_card3)
    shuffled_card4 = random.choice(deck)
    hand_4.append(shuffled_card4)
    deck.remove(shuffled_card4)


print(f"First hand: {hand_1}\nSecond hand: {hand_2}\nThird hand: {hand_3}\nForth hand: {hand_4}")
print(f"Remaining cards: {deck}")
deck_lenght = len(deck)
print(f"Deck lenght: {deck_lenght}")



# if __name__ == "__main__":
#     main()