# functions.py

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Enter your bet: "))

            if chips.bet > chips.total:
                print(f"You don't have enough chips! You have {chips.total} chips.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")