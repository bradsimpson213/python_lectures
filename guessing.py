# GUESSING GAME

# things we will need to make this game
# 1. randomly choose the number - x
# 2. conditional
# 3. input - x
# 4. variables - guesses, user input, num -x
# 5. loop iterations - x
# 6. functions - x

from random import randint
# from random import randint, choice as picker, sample

# picker()

# def choice():
#     pass


def guess(start, stop):
    """helper function to handle guessese"""
    bad_guess = True

    while bad_guess:
        try: 
            user_guess = int(input(f"Guess a number between { start } and { stop }: "))

        except ValueError:
            print("We need to guess only numbers, no letters")
            continue

        else:
            if user_guess < start or user_guess > stop:
                print(f"Numbers should be between {start} and { stop }, not { user_guess}, try again!")
                continue

        bad_guess = False
        return user_guess



def guessing_game(start=1, stop=20):
    """plays the guessing game taking in start and 
    stop points for the guess range"""

    print("Welcome to the guessing game!")
    winning_num = randint(start,stop)
    # print(winning_num)
    guesses = 5


    while guesses > 0:
        
        # user_guess = int(input(f"Guess a number between { start } and { stop }: "))
  
        user_guess = guess(start, stop)

        print(user_guess)
        guesses -= 1
  
        if user_guess == winning_num:
            print(f"YOU GUESSED CORRECT! The number was { winning_num }, you used { 5 - guesses }")
            return 

        elif user_guess > winning_num:
            print(f"You guessed too high! Try again, you have { guesses} left...")

        else:
            print(f"You guessed too low! Try again, you have { guesses} left...")

    print(f"You have run out of guesses!, Sorry you lose, The winning number was { winning_num } ")


guessing_game(1, 20)
# guessing_game(1, 50)

# guessing_game(10, 50)
# guessing_game(stop=20, start=1)
# guessing_game()