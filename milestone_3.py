import random

def create_word_list():
    word_list = ['mango','orange','apple','plum','grape']
    # print(word_list)
    return word_list

def comp_choice_guess(word_list):
    word = random.choice(word_list)
    # print(word)
    guess = input('please enter a single letter  ')
    return guess

xx=1
while xx < 6:
   word_list = create_word_list()
   guess = comp_choice_guess(word_list)
   x = guess.isalpha()

   if len(guess)==1 and  x == True:
     break
   else:
       print("Invalid letter. Please, enter a single alphabetical character.")







