import random 
import re


def create_word_list():
    word_list = ['mango','orange','apple','plum','grape']
    # print(word_list)
    return word_list

def choice_word(word_list):
   word = random.choice(word_list)
   print(word)
   return word

def ask_for_input(word_list):
    guess = input('please enter a single letter  ')
    return guess

def check_guess():
   
   xx=1
   while xx < 6:
     word_list = create_word_list()
     word =choice_word(word_list)
     guess = ask_for_input(word_list)
     guess = guess.lower()
     x = guess.isalpha()

     if len(guess)==1 and  x == True:
       yy = re.search(guess,word)
       if type(yy)== re.Match:
          print( "Good guess!", guess, "is in the word")
       else:
         print("Sorry", guess, "is not in the word. Try again")

       break
     else:
         print("Invalid letter. Please, enter a single alphabetical character.")


check_guess()





