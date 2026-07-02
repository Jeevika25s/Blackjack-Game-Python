from chips import Chips

player = Chips()

print("Starting Chips:", player.total)

player.bet = 25

player.win_bet()

print("After Winning:", player.total)

player.bet = 40

player.lose_bet()

print("After Losing:", player.total)