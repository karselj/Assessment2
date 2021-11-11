import random

class RandomNumbers:
    def __init__(self, amount, minRange, maxRange):
        self.amount = amount
        self.minRange = minRange
        self.maxRange = maxRange

    def generateRandom(self):
        """Preconditions: amount > 0
                          minRange < maxRange
           Postconditions: At least one number is printed to the screen
                           The number(s) printed to the screen are in the
                           range minRange to maxRange"""
        assert self.amount > 0
        assert self.minRange < self.maxRange
        for n in range(0, self.amount):
            num = random.randint(self.minRange, self.maxRange)
            print(num)
        # This is the final edit

secret = RandomNumbers(5, 1, 1000)
secret.generateRandom()
