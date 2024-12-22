import random

def guess_the_number():
    # Ask the user to think of a number
    print("Please think of a number between 1 and 100, and I'll try to guess it.")
    
    # Set the boundaries for the random guesses
    lower = 1
    upper = 100
    attempts = 0
    
    # Start guessing
    while True:
        # The computer randomly guesses a number in the current range
        guess = random.randint(lower, upper)
        attempts += 1
        print(f"My guess is: {guess}")
        
        # Ask the user for feedback
        feedback = input("Is my guess correct? (yes / too high / too low): ").lower()
        
        if feedback == "yes":
            print(f"Yay! I guessed your number {guess} in {attempts} attempts.")
            break
        elif feedback == "too high":
            upper = guess - 1
        elif feedback == "too low":
            lower = guess + 1
        else:
            print("Please respond with 'yes', 'too high', or 'too low'.")

# Call the function to start the game
guess_the_number()