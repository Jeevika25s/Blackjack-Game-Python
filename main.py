from chips import Chips
from functions import take_bet

player = Chips()

print("Total Chips:", player.total)

take_bet(player)

print("Bet Placed:", player.bet)