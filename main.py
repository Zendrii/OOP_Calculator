# import functions from class
from calculator_class import Calculator

# create objects to use
calc = Calculator()

# ask user for operation to be used
add_list = ['+', 'add', 'Add', 'addition', 'Addition']
subtra_list = ['-', 'subtract', 'Subtract', 'subtraction', 'Subtraction']
multi_list = ['x', '*', 'multiply', 'Multiply', 'multiplication', 'Multiplication']
divi_list = ['/', 'divide', 'Divide', 'division', 'Division']

operation = input('Enter operation: ')

# ask user for numbers to be used
num1 = input('Enter 1st number: ')
num2 = input('Enter 2nd number: ')

# calculate inputs using funtions from class
try:
    if operation in add_list:
        sum = calc.addition(num1, num2)
        # output result
        print(sum)
    elif operation in subtra_list:
        dffrnc = calc.subtraction(num1, num2)
        # output result
        print(dffrnc)
    elif operation in multi_list:
        prdct = calc.multiplication(num1, num2)
        # output result
        print(prdct)
    elif operation in divi_list:
        qtnt = calc.division(num1, num2)
        # output result
        print(qtnt)

# check for errors
except ValueError:
    print('\nOnly Numbers allowed!')
except TypeError:
    print('\nAn Error has Occured.')