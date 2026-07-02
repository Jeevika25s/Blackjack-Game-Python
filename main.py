from chips import Chips
from functions import player_wins, dealer_wins, player_busts, dealer_busts, push

chips = Chips()

chips.bet = 20

print("Starting Chips:", chips.total)

player_wins(None, chips)

print("After Win:", chips.total)

dealer_wins(None, chips)

print("After Loss:", chips.total)

push(None)