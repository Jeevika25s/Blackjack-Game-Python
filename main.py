from deck import Deck
from hand import Hand
from functions import show_some, show_all

deck = Deck()
deck.shuffle()

player = Hand()
dealer = Hand()

# Deal two cards to player
player.add_card(deck.deal_one())
player.add_card(deck.deal_one())

# Deal two cards to dealer
dealer.add_card(deck.deal_one())
dealer.add_card(deck.deal_one())

print("Showing Some Cards")
show_some(player, dealer)

print("\nShowing All Cards")
show_all(player, dealer)