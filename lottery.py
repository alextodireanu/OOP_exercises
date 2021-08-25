# Lottery: make a list or tuple containing a series of 10 numbers and five letters. randomly select 4 numbers or letters
# and print a message saying that any ticket matching these four numbers or letters wins a prize.

from random import choices

numbers_letters = (12, 32, 1, 15, 27, 25, 46, 33, 8, 5, 'u', 'p', 't', 'a')
winning_numbers_letters = choices(numbers_letters, k=4)
print(f"Any ticket that has the following numbers/letters wins $1000: {winning_numbers_letters}")
