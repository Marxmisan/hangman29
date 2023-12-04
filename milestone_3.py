import random

def create_word_list():
    word_list = ['mango','orange','apple','plum','grape']
    print(word_list)
    return word_list

def comp_choice_guess(word_list):
    word = random.choice(word_list)
    print(word)
    guess = input('please enter a sigle letter  ')
    if len(guess) == 1 and type(guess) == str:
      print('Good guess')
    else:
      print('Oops! That is not a valid input')

word_list = create_word_list()
comp_choice_guess(word_list)






