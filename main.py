#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo, welcome_msg
import random
secret_number = random.randint(1, 100)
print(welcome_msg)
print(logo)
print("     I'm thinking of a number between 1 and 100\n")

def start():
    difficulty = input("""            Choose a difficulty:
EASY: You will have 10 attempts to guess the number. Type 'easy' 
HARD: You will have 5 attempts to guess the number. Type 'hard'\n""").lower()
    if difficulty == "easy":
        return 10
    else:
        return 5


count = start()


while count != 0:
    guess = int(input("Make a guess: "))
    if guess == secret_number:
        print(f"""You've got it, you win 
The secret number was {secret_number}""")
        break
    elif guess > secret_number:
        count -= 1
        print("Too high. Guess again")
        print(f"You have {count} attempts left.")
    elif guess < secret_number:
        count -= 1
        print("Too low. Guess again")
        print(f"You have {count} attempts left.")
    else:
      print("Wrong input, ")

if count == 0:
    print(f"""You've ran our of guesses, you lose
The secret number was {secret_number}""")


