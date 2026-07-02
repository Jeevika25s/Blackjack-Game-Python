from deck import Deck
from hand import Hand

# Create and shuffle the deck
deck = Deck()
deck.shuffle()

# Create a player's hand
player_hand = Hand()

# Deal two cards
player_hand.add_card(deck.deal_one())
player_hand.add_card(deck.deal_one())

# Adjust Ace if needed
player_hand.adjust_for_ace()

print("Player's Cards:")
for card in player_hand.cards:
    print(card)

print("\nHand Value:", player_hand.value)