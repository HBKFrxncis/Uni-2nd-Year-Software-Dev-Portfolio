import random 
# Random was imported to generate a random number

def guessing_game():
    # Everything is in encapuslated in this function 
    print("Welcome to the Guessing Game!")

    # The lower and upper bounds for the number to guess
    lower_bound = 1
    upper_bound = 100

    # To generate a random number between the lower and upper bounds
    secret_number = random.randint(lower_bound, upper_bound)

    # Initialise the number of attempts the player has made
    attempts = 0
    max_attempts = 10  # Maximum attempts player can have

    print(f"I have selected a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess it.")

    # Looped until the player has made enough attempts or guessed correctly
    while attempts < max_attempts:
        try:
            # To ask the player for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1  # increases 1 to the amount of attempts each time

            # Checks if the guess is within the valid range
            if guess < lower_bound or guess > upper_bound:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
                continue  # Skips to the next iteration if the input is invalid

            # Provides feedback on the player's guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit the loop if the guess is correct

        except ValueError:
            # Handles cases where the players input is not an integer
            print("Invalid input. Please enter a valid number.")

    # Check if the user has exhausted all attempts
    if attempts == max_attempts and guess != secret_number:
        print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")

# Start the game
if __name__ == "__main__":
    guessing_game()
