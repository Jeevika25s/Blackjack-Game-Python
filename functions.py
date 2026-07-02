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
            
# functions.py

playing = True

def hit(deck, hand):
    card = deck.deal_one()
    hand.add_card(card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        choice = input("Hit or Stand? Enter 'h' or 's': ").lower()

        if choice == 'h':
            hit(deck, hand)
            break

        elif choice == 's':
            print("Player stands. Dealer's turn.")
            playing = False
            break

        else:
            print("Invalid input. Please enter h or s.")