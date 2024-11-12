from random import choice
from logo import logo
import os
from colorama import Back, Style


class Wordle:
    def __init__(self, letters=5, logo=logo):
        self.logo = logo
        self.letters = letters
        self.game_words = self.get_all_words()
        self.winning_word = self.choose_game_word()
        self.guess = ""
        self.guesses = [[] for _ in range(6)] # [["tubes"],[],[],[],[],[]]
        # self.guesses = [
        #     ["t", "u", "b", "e", "s"],
        #     ['c', 'h', 'a', 'm', "p"]
        #     ]
        # print(self.guesses[0][1])
        self.tries = 0
        self.play_game()


    def get_all_words(self):
        file = open("words.txt")
        # print(list(file))
        words = [ word.rstrip() for word in file]
        # print(words)
        wordle_words = [ word for word in words if len(word) == self.letters]
        # print(wordle_words)
        return wordle_words


    def choose_game_word(self):
        return choice(self.game_words)


    def handle_guess(self):
        bad_guess = True    

        while bad_guess:

            user_guess = input(f"Guess a {self.letters} letter word: ").lower()

            if len(user_guess) != self.letters:
                print(f'Words must be {self.letters} long, try again!')
                continue

            elif user_guess in self.guesses:
                print(f'You already guessed {user_guess}, try again!')

            else:
                bad_guess = False
                self.guess = user_guess
                self.guesses[self.tries] = user_guess
                self.tries += 1


    def play_game(self):
        print(self.logo)
        print("Welcome to Wordle!")
        while self.tries < 6:
            self.handle_guess()
            # print(self.guess)
            self.update_display()
            if self.guess == self.winning_word:
                print(f"YOU WIN! {self.tries}/6 THE WORD WAS '{self.winning_word.upper()}'")
                # build in play again here
                return

        print(f"Sorry you are out of tries, the word was {self.winning_word}")


    def update_display(self):
        os.system("clear")
        for word in self.guesses:
            if len(word) > 0:
                display = []
                for index, letter in enumerate(word):
                    if letter == self.winning_word[index]:
                        display.extend([Back.GREEN, letter.upper(), Style.RESET_ALL, ' '])
                    
                    elif letter in self.winning_word and letter != self.winning_word[index]:
                         display.extend([Back.YELLOW, letter.upper(), Style.RESET_ALL, ' '])

                    else:
                         display.extend([Style.RESET_ALL, letter.upper(), Style.RESET_ALL, ' '])

                print(display)
                for index, word in enumerate(display):
                    if index == (len(display) - 1):
                        print(word)
                    else:
                        print(word, end='')

            else:
                display = ["_" for _ in range(self.letters)] # ["_","_","_","_","_",]
                print(' '.join(display)) #

game = Wordle()


