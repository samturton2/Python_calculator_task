# import functions in
from functions import Functions

# define a child class that holds a calculators functions and carries them out
class Calculator(Functions):
    def __init__(self):
        super().__init__()

    # create display function
    def calc_display(self):
        print("""
        --------------------------------
        ********** CALCULATOR **********
        --------------------------------
        
        The functions available are:
            - add, subtract, multiply, divide
            - divisible
            - triangle area
            - inch/cm converter
        Type exit/stop/quit to exit calculator
        """)

    #define a function that takes a string of numbers and assigns them as floats
    def float_getter(self, num_string):
        num1 = num_string.split(" ")[0]
        num2 = num_string.split(" ")[1]
        #check if the numbers are numbers or units
        try:
            return float(num1), float(num2)
        except:
            try:
                return float(num1), num2
            except:
                return num1, num2


    # create while loop function
    def calc_on(self):
        while True:
            # ask user for function
            func = input("enter the function you want to carry out\n=>")

            # if statements checking the function chosen, asking for 2 numbers and outputting answer
            if func[:2].lower() == 'ad':
                numbers = input("enter: num1 num2\n=>")
                num1, num2 = self.float_getter(numbers)
                print(f"answer: {self.add(num1, num2)}") #Returns add function

            elif func[:2].lower() == 'su':
                numbers = input("enter: num1 num2\n=>")
                num1, num2 = self.float_getter(numbers)
                print(f"answer: {self.subtract(num1, num2)}") #Returns subtract function

            elif func[:2].lower() == 'mu':
                numbers = input("enter: num1 num2\n=>")
                num1, num2 = self.float_getter(numbers)
                print(f"answer: {self.multiply(num1, num2)}") #Returns multiply function

            elif func[:5].lower() == 'divid':
                numbers = input("enter: num1 num2\n=>")
                num1, num2 = self.float_getter(numbers)
                print(f"answer: {self.divide(num1, num2)}") #Returns divide function

            elif func[:5].lower() == 'divis':
                numbers = input("enter: num1 num2\n=>")
                num1, num2 = self.float_getter(numbers)
                print(f"answer: {self.divisible(num1, num2)}") #Returns divisible function

            elif func[:2].lower() == 'tr':
                numbers = input("enter: base height\n=>")
                base, height = self.float_getter(numbers)
                print(f"answer: {self.triangle_area(base, height)}") #Returns triangle area

            elif func[:2].lower() == 'in':
                numbers = input("enter: num unit\n=>")
                num, unit = self.float_getter(numbers)
                print(f"answer: {self.inch_cm_convert(num, unit)}") #Returns inch cm converter

            elif func[:2].lower() == "ex" or func[:2].lower() == 'qu' or func.lower() == "stop":
                break  #exits calculator loop

            else:
                print("I don't recognise that function sorry")

print("6.5".isdigit())