import random

def guessing_game():
    secret_number = random.randint(1, 100)

    guess = 0

    while guess != secret_number:
        try:
            guess = int(input("Guess the number (between 1 and 100): "))

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            elif guess == secret_number:
                print(f"Congratulations! You guessed the correct number {secret_number}.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()
