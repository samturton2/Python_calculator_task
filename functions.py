# create parent class with all calculators functions
class Functions:
    def add(self, num1, num2):
        try:
            return num1 + num2
        except:
            return 'error'

    def subtract(self, num1, num2):
        try:
            return num1 - num2
        except:
            return "error"

    def divide(self, num1, num2):
        try:
            if num2 == 0 and num1 > 0:
                return "∞"
            elif num2 == 0 and num1 < 0:
                return "-∞"
            elif num2 == 0:
                return "undefined"
            else:
                return num1 / num2
        except:
            return "error"

    def multiply(self, num1, num2):
        try:
            return num1 * num2
        except:
            return "error"

    def divisible(self, num1, num2):
        try:
            return num1 % num2 == 0
        except:
            return "error"

    def triangle_area(self, base, height):
        try:
            # makes sure to return a positive area
            return (((0.5 * height * base) ** 2) ** 0.5)
        except:
            return "error"

    def inch_cm_convert(self, num, unit):
        rate = 0.3937
        try:
            if unit == "cm":
                return f"{num * rate} inch"
            elif unit == "inch":
                return f"{num / rate} cm"
            else:
                return "I can't convert those units"
        except:
            return "error"

