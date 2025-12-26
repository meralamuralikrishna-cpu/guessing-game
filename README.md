Great choice — adding a **preview section** makes your GitHub README much more engaging. Since your project is a terminal‑based game, the best way to show it off is with either:

- A **GIF recording** of gameplay (using tools like [asciinema](https://asciinema.org/) or [terminalizer](https://github.com/faressoft/terminalizer)), or  
- A **screenshot** of the terminal while playing.

Here’s the updated README with a **Preview section** included:

```markdown
# 🎯 Python Number Guessing Game

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen)
![GitHub stars](https://img.shields.io/github/stars/your-username/guessing-game?style=social)
![GitHub forks](https://img.shields.io/github/forks/your-username/guessing-game?style=social)

A fun and interactive **number guessing game** built with Python.  
The computer randomly selects a number between **1 and 100**, and the player has **6 attempts** to guess it correctly.

---

## 📖 How It Works
- The program generates a random number between **1 and 100**.
- You have **6 attempts** to guess the number.
- After each guess:
  - If your guess is too low → You’ll be prompted to try a higher number.
  - If your guess is too high → You’ll be prompted to try a lower number.
- If you guess correctly → 🎉 You win!
- If you run out of attempts → The correct number is revealed.
- After each round, you can choose to **play again** or exit.

---

## 🛠️ Requirements
- Python 3.x

---

## ▶️ Run the Game
Clone the repository and run the script:

```bash
git clone https://github.com/your-username/guessing-game.git
cd guessing-game
python guessing_game.py
```

---

## 🎮 Example Gameplay
```
Attempt 1/6 - Guess a number between 1 and 100: 50
Too low! Try a number higher than 51.
You have 5 attempts left.

Attempt 2/6 - Guess a number between 1 and 100: 75
Too high! Try a number between 1 and 74.
You have 4 attempts left.

Attempt 3/6 - Guess a number between 1 and 100: 63
Correct! The number was 63!
```

---

## 👀 Preview
Here’s what the game looks like in action:

![Gameplay Preview](preview.gif)

*(Replace `preview.gif` with your actual GIF or screenshot file — commit it to your repo and link it here.)*

---

## 🔁 Replay Feature
At the end of each round, you’ll be asked:
```
Do you want to play again (y/n):
```
- Enter `y` → Start a new game.
- Enter `n` → Exit with a thank-you message.

---

