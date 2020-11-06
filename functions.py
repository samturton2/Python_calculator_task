# create parent class with all calculators functions
class Functions:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def divide(self, num1, num2):
        return num1 / num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divisible(self, num1, num2):
        return num1 % num2 == 0

    def triangle_area(self, height, width):
        return 0.5 * height * width

    def inch_cm_convert(self, num, unit):
        rate = 0.3937
        if unit == "cm":
            return num * rate
        elif unit == "inch":
            return num / rate
        else:
            return "I can't convert those units"