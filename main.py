from deck import Deck

deck = Deck()

print("Number of cards:", len(deck.all_cards))


deck.shuffle()

card = deck.deal_one()

print("\nCard dealt:")
print(card)

print("\nCards remaining:", len(deck.all_cards))