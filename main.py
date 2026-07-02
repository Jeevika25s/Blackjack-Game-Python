# main.py

from deck import Deck
from hand import Hand
from chips import Chips

from functions import (
    take_bet,
    hit_or_stand,
    show_some,
    show_all,
    player_busts,
    player_wins,
    dealer_busts,
    dealer_wins,
    push,
)

import functions

print("Welcome to Blackjack!")

while True:

    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()

    # Create player and dealer hands
    player_hand = Hand()
    dealer_hand = Hand()

    # Deal two cards each
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())

    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())

    # Create chips object
    if 'player_chips' not in locals():
        player_chips = Chips()

    # Take bet
    print(f"\nYou have {player_chips.total} chips.")
    take_bet(player_chips)

    # Reset playing flag
    functions.playing = True

    # Show initial cards
    show_some(player_hand, dealer_hand)

    # Player's turn
    while functions.playing:

        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, player_chips)
            break

    # Dealer's turn
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            dealer_hand.add_card(deck.deal_one())
            dealer_hand.adjust_for_ace()

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, player_chips)

        else:
            push(player_hand)

    print(f"\nPlayer's total chips: {player_chips.total}")

    play_again = input("\nPlay again? (y/n): ").lower()

    if play_again != 'y':
        print("\nThanks for playing!")
        break