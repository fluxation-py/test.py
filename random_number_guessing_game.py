import random

def guessing_game():
    random_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to my Number Guessing Game, where you guess Numbers!")
    print("Pick a number between 1 and 100, and I'll tell you if it's too high, too low, or just right! Let's see how many attempts it takes you to guess the number!")

    while True:
        try:
            user_guess = int(input("Enter your random guess:"))5
            attempts += 1

            if user_guess < random_number:
                print("Nice try, too low - guess again!")

            elif user_guess > random_number:
                print("Close, but too high - guess again!")
            
            else:
                print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts! 🎉")
                break

        except ValueError:
            print("Please enter a valid number between 1 and 100.")

guessing_game()
