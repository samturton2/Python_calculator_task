# import functions in
from functions import Functions

# define a child class that holds a calculators functions and carries them out
class Calculator(Functions):
    def __init__(self, ans = 0):
        super().__init__()
        self.ans = ans

    # create display function

    # create while loop function