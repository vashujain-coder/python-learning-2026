import random

def guessing_game():
    computer_choice = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess my number (between 1 and 100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < 1 or guess > 100:
            print("Invalid number. Try again.")

        elif guess < computer_choice - 10:
            print("Too low!")

        elif guess < computer_choice:
            print("Close, but still lower.")

        elif guess > computer_choice + 10:
            print("Too high!")

        elif guess > computer_choice:
            print("Close, but still higher.")

        else:
            if attempts == 1:
                print(f"You won! My number was {computer_choice}. You guessed it in {attempts} attempt.")
            else:
                print(f"You won! My number was {computer_choice}. You guessed it in {attempts} attempts.")
            break


def main():
    while True:
        choice = input("Do you want to play the guessing game? (yes/no): ").lower()

        if choice == "yes":
            guessing_game()

        elif choice == "no":
            print("Thanks for playing!")
            break

        else:
            print("Invalid input. Please type yes or no.")


main()
