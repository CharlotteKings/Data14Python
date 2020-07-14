from Hangman_brain import Brain
class Game:

    def __init__(self):
        self.lives = 10
        self.brain = Brain()
        self.word = self.brain.get_word()
        self.game_board = self.brain.dash()
        self.guess_index = []
        self.display()
        self.guess_letter()
        self.play_again()

    def display(self):
        # print(self.word)
        hello = input("Hello! What's your name? \n")
        greeting = input(f"Would you like to play a game of hangman, {hello}? \n").upper()
        characters = len(self.game_board)
        while greeting != "Y" and greeting != "N":
            greeting = input("Please choose Y or N \n").upper()
        if greeting == "Y":
            print(f"Your word is {self.game_board} = {characters} characters")
        elif greeting == "N":
            quit()


    def guess_letter(self):
        while self.lives > 0:
            guess = input("Guess a letter! \n").upper()
            indicies = self.brain.letter_check(guess)
            self.update(guess, indicies)
            if guess in self.guess_index:
                print(f"You've already guessed that. Here are your previous guesses {self.guess_index}")
            else:
                self.guess_index.append(guess)
                if indicies == []:
                    if not guess.isalpha() or len(guess) > 1:
                        print("That's not a letter!")
                    else:
                        self.lives -= 1
                        print(f"That letter isn't in the word. {self.lives} lives left!")
                elif indicies != []:
                    print(self.game_board)
                if "_" not in self.game_board and self.lives > 0:
                    print("YOU WIN!!!")
                    self.play_again()
                elif self.lives == 0:
                    print(f"You lose. The correct word was {self.word}")
                    self.play_again()



    def update(self, guess, indicies):
        for i in indicies:
            self.game_board[i] = guess
        return self.game_board


    def play_again(self):
        play_again = input("Would you like to play again? Y(Yes) or N(No) \n").upper()
        while play_again != "Y" and play_again != "N":
            play_again = input("Please choose Y or N \n").upper()
        if play_again == "Y":
            Game()
        elif play_again == "N":
            quit()


new_guess = Game()
print(new_guess.word)



