
import random
#import re

def unique_count(word):
  k=list()
  for x in word:
    if x not in k:
      k.append(x)
  return len(k)



class Hangman:

   
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_']*len(self.word)
        self.list_of_guesses = []
        self.num_lives = num_lives
        self.word_list = word_list
        self.num_letters = (unique_count(self.word))
        print(f'{self.word}')
    
    def check_guess(self, guess):
        self.guess = guess
        if self.guess in self.word:
         print(f"Good guess! {self.guess} is in the word")

    
    def ask_for_input(self):
        xx=1
        
        while xx < 6:
            self.guess = input('please enter a single letter  ')
            if not self.guess.isalpha() :
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif len(self.guess) > 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
             
                    
            elif self.guess in self.list_of_guesses:
               print("You already tried that letter!")
            else:
             self.check_guess(self.guess)  
             self.list_of_guesses.append(self.guess)
             print(f'{self.list_of_guesses}')
  
hangman1 = Hangman(word_list=['orange','mango','apple'])
hangman1.ask_for_input()
