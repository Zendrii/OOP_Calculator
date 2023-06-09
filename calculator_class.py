# create class
class Calculator:
    def __init__(self):
        pass

    # create behaviors/statements
    def addition(self, num1, num2):
        return float(num1) + float(num2)
    
    def subtraction(self, num1, num2):
        return float(num1) - float(num2)
    
    def multiplication(self, num1, num2):
        return float(num1) * float(num2)
    
    def division(self, num1, num2):
        try:
            quotient = float(num1) / float(num2)
        except ZeroDivisionError:
            print('\nCannot Divide by zero!')
        else:
            return quotient