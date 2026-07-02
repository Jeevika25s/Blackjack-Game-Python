from deck import Deck
from hand import Hand
from functions import hit

deck = Deck()
deck.shuffle()

player_hand = Hand()

# Give two cards
player_hand.add_card(deck.deal_one())
player_hand.add_card(deck.deal_one())

print("Player Cards:")
for card in player_hand.cards:
    print(card)

print("Value:", player_hand.value)

print("\nGiving one more card...\n")

hit(deck, player_hand)

print("Updated Cards:")
for card in player_hand.cards:
    print(card)

print("New Value:", player_hand.value)