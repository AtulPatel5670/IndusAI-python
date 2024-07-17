import random
def guess_the_number():
    print("Welcome to the Guess the Number Game!!!")
    lower_bound = 1
    upper_bound = 100
    random_number = random.randint(lower_bound, upper_bound)
    guess = None
    attempts = 0
    print(f"I have selected a number between {lower_bound} and {upper_bound}. Try to guess it!")

    while guess != random_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        guess_the_number()
    else:
        print("Thank you for playing!!")

# Start the game
guess_the_number()
