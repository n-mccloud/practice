import random

print("Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.")

while attempts < max_attempts:
    try:
        # Get the player's guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
            
        # Tell player how many attempts are left
        attempts_left = max_attempts - attempts
        if attempts_left > 0:
            print(f"You have {attempts_left} attempts left.")
            
    except ValueError:
        print("Please enter a valid number!")
        continue

if attempts >= max_attempts and guess != secret_number:
    print(f"Game Over! The number was {secret_number}.")
