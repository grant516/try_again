import random

class Word:

    def __init__(self):
        word = "hello"
        guess_word = []
        show_guess = ""
        wrong_guesses = 0

    def update_word(self):
        """This class chooses a word for the game and then makes the the tiles."""
        val = random.randint(1,3)
        if val == 1:
            self.word = "chicken"
        elif val == 2:
            self.word = "flag"
        elif val == 3:
            self.word = "pikachu"

        self.wrong_guesses = len(self.word)

        #use the code below to also update when the player chooses a correct guess
        for x in range(0, len(self.word)):
            self.guessed_word.append("_ ")
            self.show_guess = self.show_guess + self.guessed_word[x]
        

    def guessed_letter(self, letter):

        wrong =0
        
        for x in range(0, len(self.word)):
            if letter == self.word[x]:
                self.guessed_word[x] = letter
                self.show_guess = ""
                self.show_guess = self.show_guess + self.guessed_word[x]
            else:
                wrong += 1

            if(wrong == len(self.word)):
                self.wrong_guesses = self.wrong_guesses -1


    def keep_playing(self):
        
        if(self.wrong_guesses == 0):
            return(False)
        else:
            return(True)