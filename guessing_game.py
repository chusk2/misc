#!/usr/bin/env python3

# guess a number between 1 and 10

import random

random_num = random.randint(1,10) # random chosen number to be guessed

print('You have to guess a number between 1 and 10. Good luck!')
count = 1 # counts the number of attemps before guessed
guess_num = 0 # guess_num set to 0 in order to be asked at least one in next nested while 
while True:
    
# check the given number is between 1 and 10    
    while guess_num>10 or guess_num<1 :
            guess_num=int(input('Guess a number: '))
    try:
        if guess_num==random_num:
            print('Congrats!! It was %i' % (guess_num))
            print('It took you just %i attemps.' % (count))
            break
        else:
            print('Try again...\n')
            count += 1
    except TypeError:
        print('Enter a number, not text!')

