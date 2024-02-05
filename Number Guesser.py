import random

def guess_the_number(start_range, end_range):
    secret_number = random.randint(int(start_range),int(end_range))
    
    print(f"Guess the number (between {start_range} and {end_range}):")

    while True:
        try:
            user_guess = int(input("Your guess: "))

            if user_guess < int(start_range) or user_guess > int(end_range):
                print(f"Please enter a number between {start_range} and {end_range}.")
            elif user_guess < secret_number:
                print("Too low! Try again")
            elif user_guess > secret_number:
                print("Too high! Try again")
            else:
                print(f"Congratulations! You guessed the correct number {secret_number}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number")

if __name__ == "__main__":
    start_range =input ("Enter start range:- ")
    end_range = input ("Enter end range:- ")

    guess_the_number(start_range, end_range)
