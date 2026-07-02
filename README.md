# 🃏 Blackjack Game in Python

A simple text-based **Blackjack Card Game** built using **Python** and **Object-Oriented Programming (OOP)**. This project simulates a real Blackjack game where the player competes against an automated dealer.

---

## 📌 Features

- 🎴 Complete 52-card deck
- 🔀 Shuffle the deck randomly
- 👤 One player vs automated dealer
- ➕ Hit or Stand option
- 💰 Betting system with chips
- ♠️ Automatic Ace value adjustment (1 or 11)
- 🏆 Win, Lose, Bust, and Tie (Push) conditions
- 🔁 Play multiple rounds
- 🧩 Built using Python classes (OOP)

---

## 📂 Project Structure

```
Blackjack-Game-Python/
│
├── card.py          # Card class
├── deck.py          # Deck class
├── hand.py          # Hand class
├── chips.py         # Betting system
├── functions.py     # Helper functions
├── main.py          # Main game
├── README.md
└── .gitignore
```

---

## 🛠 Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Git
- GitHub
- VS Code

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/Jeevika25s/Blackjack-Game-Python.git
```

2. Open the project folder

```bash
cd Blackjack-Game-Python
```

3. Run the game

```bash
python main.py
```

---

## 🎮 Game Rules

- The player starts with 100 chips.
- Enter a betting amount before each round.
- Both the player and dealer receive two cards.
- One of the dealer's cards remains hidden.
- Choose:
  - **H** → Hit (draw another card)
  - **S** → Stand (end your turn)
- If your total exceeds 21, you bust and lose.
- The dealer draws cards until reaching at least 17.
- The player with the highest value (without exceeding 21) wins.

---

## 📚 OOP Concepts Used

This project demonstrates the following Object-Oriented Programming concepts:

- Classes
- Objects
- Constructors (`__init__`)
- Instance Variables
- Methods
- Encapsulation

---

## 📸 Sample Output

```
Welcome to Blackjack!

You have 100 chips.

Enter your bet: 20

Dealer's Hand:
<card hidden>
King of Hearts

Player's Hand:
Eight of Clubs
Seven of Diamonds

Player's Value: 15

Hit or Stand? (h/s): h

Player Wins!

Player's Total Chips: 120
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Python classes and objects
- Working with multiple Python files
- Lists and dictionaries
- Loops and conditional statements
- Random module
- Git and GitHub workflow
- Building a complete console-based application

---

## 🚀 Future Improvements

- Add multiple players
- Add Double Down option
- Add Split option
- Add Blackjack detection
- Improve console UI
- Create a GUI version using Tkinter or PyQt

---

## 👩‍💻 Author

**Jeevika S**

GitHub: https://github.com/Jeevika25s

---
