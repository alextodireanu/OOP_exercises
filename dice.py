# Dice: make a class Die with one attribute called sides which has a default value of 6. write a method called
# roll_die that prints a random number between 1 and the number of sides the die has.

from random import randint


class Die:
    """Representing a die"""
    def __init__(self):
        """Defining the attributes"""
        self.sides = 6

    def roll_die(self):
        """Method to roll the die"""
        print(randint(1, self.sides))


die = Die()
die.roll_die()
