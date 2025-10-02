import random

easy_words = ["cat", "dag", "pig", "pen", "soup", "cup"]
medium_words = ["apple", "india", "ball", "lemon", "maggi", "gift"]
hard_words = ["banana", "orange", "giraffe", "elephant", "umbrella", "computer"]

print("WElcome to the word Guessing game")
print("Choose a difficulty level: easy, medium or hard")

level = input("Enter difficulty lenvel: ").lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice : Defaulting to easy Level")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the Secret Word")

while True:
    guess = input("Enter your Guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congrulations! You've guessed the word {secret} in {attempts} attempts. ")
        break
    
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]

        else:
            hint += "_"
    print("Hint: ", hint)
print("Game Over")            
