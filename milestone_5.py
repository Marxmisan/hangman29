import random
#import re

class Hangman:

   
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_']*len(self.word)
        self.list_of_guesses = []
        self.num_lives = num_lives
        self.word_list = word_list
        self.num_letters = (self.unique_count(self.word))
        print(f'{self.word}')


    def unique_count(self,word):
      k=list()
      self.word = word
      for x in self.word:
        if x not in k:
          k.append(x)
      return len(k)
    
    def check_guess(self, guess):
        self.guess = guess
        if self.guess in self.word:
          print(f"Good guess! {self.guess} is in the word")
          for xx in range(len(self.word)):
           if self.guess == self.word[xx]:
              self.word_guessed[xx]=self.guess
          self.num_letters =self.num_letters -1
        else:
           self.num_lives = self.num_lives -1
           print(f'sorry, {self.guess} is not in the word')
           print(f'you have {self.num_lives} lives left')
     
    
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
  
#hangman1 = Hangman(word_list=['orange','mango','apple'])
#hangman1.ask_for_input()


def play_game(word_list):
    num_lives = 5

    xx = 1
    print(f'{xx}')
    while xx < 6:
        game = Hangman(word_list, num_lives)
        game.ask_for_input()
        if game.num_lives == 0:
         print(f'{game.num_lives}')
         print('you lost')
         xx = xx + 6
         print(f'{xx}, new')
         
        elif game.num_letters > 0:
             xx = 2
         
        else:
           game.num_letters == 0 and game.num_lives > 0
           print('Congratulations. You won the game!')


word_list=['orange','mango','apple']
play_game(word_list)