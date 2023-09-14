# Randomizer class

# This class returns a randomized password using the string library and the random library
import random
import string


class Randomizer:
    def __init__(self, complexity):
        if complexity == 'low':
            self.__chars = string.ascii_letters + string.digits
        elif complexity == 'high':
            self.__chars = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self, length):
        return ''.join(random.choice(self.__chars) for i in range(length))
