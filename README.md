# ♠️ Blackjack Game (Python)

A simple **console-based Blackjack (21) game** built using **Python**.  
This project simulates the classic casino card game where the player competes against the computer (dealer).

---

## 🎮 Game Overview

Blackjack is a card game where the goal is to get a hand value as close to **21** as possible without exceeding it.

- Number cards are worth their face value  
- Face cards (J, Q, K) are worth **10**
- Ace can be **11 or 1** (automatically adjusted to prevent bust)

---

## ✨ Features

- ASCII art logo for a fun start 🎴  
- Random card distribution  
- Automatic Ace value adjustment (11 → 1 when needed)  
- Computer plays according to Blackjack rules (hits until score ≥ 17)  
- Win, lose, draw, and Blackjack conditions handled  
- Replay option after every game  

---

## 🛠️ Technologies Used

- **Python 3**
- Built-in `random` module
- Console / Terminal based UI

---


---

## ▶️ How to Run the Game

1. Clone this repository:
```bash
git clone https://github.com/your-username/blackjack-game.git
```
2. Navigate to the project folder:

```bash
cd blackjack-game
```

3. Run the game:

```bash
python blackjack.py
```

## 🧠 Game Rules

- You start with **two cards**
- The computer starts with **one visible card**
- Choose:
  - `'y'` → Hit (get another card)
  - `'n'` → Pass (computer plays)
- If your score goes above **21** → You lose
- If the computer goes above **21** → You win

---

## 🏆 Winning Conditions

- Blackjack (21 with two cards)
- Higher score than computer without busting
- Computer busts

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!  
Feedback and suggestions are always welcome 😊

---

## 👩‍💻 Author

**Unnati Agarwal**  
Aspiring AI & ML Engineer | Python Developer

