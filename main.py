
import random

# Get the range from the user
min_num = int(input("Enter the minimum number: "))
max_num = int(input("Enter the maximum number: "))

# Generate random number
secret_number = random.randint(min_num, max_num)
attempts = 0

print(f"\nI'm thinking of a number between {min_num} and {max_num}")

while True:
    # Get user's guess
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    # Check the guess
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"\nCongratulations! You found the number in {attempts} attempts!")
        break
