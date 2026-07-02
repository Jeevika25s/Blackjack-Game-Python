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
def show_some(player, dealer):
    print("\n--------------------------------")
    print("Dealer's Hand:")
    print("<card hidden>")
    print(dealer.cards[1])

    print("\nPlayer's Hand:")
    for card in player.cards:
        print(card)

    print("Player's Value:", player.value)
    print("--------------------------------")


def show_all(player, dealer):
    print("\n--------------------------------")
    print("Dealer's Hand:")
    for card in dealer.cards:
        print(card)

    print("Dealer's Value:", dealer.value)

    print("\nPlayer's Hand:")
    for card in player.cards:
        print(card)

    print("Player's Value:", player.value)
    print("--------------------------------")
def player_busts(player, chips):
    print("\nPlayer Busts!")
    chips.lose_bet()


def player_wins(player, chips):
    print("\nPlayer Wins!")
    chips.win_bet()


def dealer_busts(player, chips):
    print("\nDealer Busts!")
    chips.win_bet()


def dealer_wins(player, chips):
    print("\nDealer Wins!")
    chips.lose_bet()


def push(player):
    print("\nIt's a Tie!")