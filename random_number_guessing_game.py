import random

def guessing_game():
    random_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to my Number Guessing Game, where you guess Numbers!")
    print("Pick a number between 1 and 100, and I'll tell you if it's too high, too low, or just right! Let's see how many attempts it takes you to guess the number!")

    while True:
        try:
            user_guess = int(input("Enter your random guess:"))
            attempts += 1

            if user_guess < random_number:
                print("It is too low but you can always try again!")

            elif user_guess > random_number:
                print("Too high, you can do better come on!")
            
            else:
                print("Yay, you did it.")
                break

        except ValueError:
            print("Please enter a valid number between 1 and 100.")

guessing_game()
