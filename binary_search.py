import random
import time

lower_limit = 1
upper_limit = int(1e5)
guess_me = random.randint(lower_limit, upper_limit)

def brute_find(num_to_guess):
    """Guess the number by trial and error, removing failed guessings from
    a list of numbers, so there are no repeated guessings."""
    numbers = [i for i in range(lower_limit, upper_limit + 1)]
    while True:
        guess = random.choice(numbers)
        if guess == num_to_guess:
            break
        else:
            numbers.remove(guess)


def binary_search(num_to_guess, lower=lower_limit, upper=upper_limit):
    """Guess a number using a binary search"""
    median = (lower + upper) // 2
    while True:
        if median == num_to_guess:
            break
        else:
            if median > num_to_guess:
                upper = median
                median = (lower + upper) // 2
            elif median < num_to_guess:
                lower = median
                median = (lower + upper) // 2


print(f'\nThe number to guess was {guess_me}. Guessing range was between '
      f'{lower_limit} and {upper_limit}.')
then = time.time()
brute_find(guess_me)
now = time.time()
lapse_brute = now - then
print(f'Brute force search took {lapse_brute:.2f} seconds to figure it out.')

then = time.time()
binary_search(guess_me)
now = time.time()
lapse_binary = now - then
print(f'Binary search search took {lapse_binary:.2e} seconds '
      'to figure it out.')

print(f'Binary search was {(lapse_brute / lapse_binary):.2e} times faster '
      f'than a brute force guessing.')
