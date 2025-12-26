import random

def guessing_game():
    rand_num = random.randint(1, 100)
    for i in range(6):
        try:
            guess = int(input(f'Attempt {i+1}/6 - Guess a number between 1 and 100: '))
        except ValueError:
            print('Please enter a valid integer')
            continue

        if guess == rand_num:
            print(f' Correct! The number was {rand_num}!')
            break
        elif guess < rand_num:
            print(f' Too low! Try a number higher than {guess+1}.')
            print(f'You have {5-i} attempts left.')
        elif guess > rand_num:
            print(f' Too high! Try a number between 1 and {guess-1}.')
            print(f'You have {5-i} attempts left.')
    else:
        print(f' Out of attempts! The number was {rand_num}.')

# 🔁 Replay loop
while True:
    guessing_game()
    play_again = input('Do you want to play again (y/n): ').lower()
    if play_again != 'y':
        print('Thanks for playing!')
        break