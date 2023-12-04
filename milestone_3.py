import random

word_list = ['mango','orange','apple','plum','grape']
print(word_list)


word = random.choice(word_list)
print(word)
guess = input('please enter a sigle letter  ')
if len(guess) == 1 and type(guess) == str:
    print('Good guess')
else:
    print('Oops! That is not a valid input')