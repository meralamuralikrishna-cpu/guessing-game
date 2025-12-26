
# 🎯 Python Number Guessing Game

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

