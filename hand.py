# hand.py

from card import values

class Hand:

    def __init__(self):
        self.cards = []      # List to store cards
        self.value = 0        # Total hand value
        self.aces = 0         # Count the number of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1