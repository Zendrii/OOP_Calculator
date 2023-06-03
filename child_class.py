class Objects:
    def objct(self):
        # import functions from parent class
        from calculator_class import Calculator

        # create objects to use
        calc = Calculator()
        return calc

    def oprtn(self):
        # ask user for operation to be used
        operation = input('\nEnter operation: [ + | - | * | / ] ')
        return operation

    def npts(self):
        # ask user for numbers to be used
        num1 = input('\nEnter 1st number: ')
        num2 = input('\nEnter 2nd number: ')
        return num1, num2

# add/create a new class that inherits the functions from parent class
class Conditions(Objects):
    def chckr(self):
        try:
            obj = super().objct()
            oper = super().oprtn()
            inp = super().npts()

            

            # calculate inputs using funtions from class
            if oper == '+':
                sum = calc.addition(num1, num2)
                # output result
                print('\n', sum)
            elif operation == '-':
                dffrnc = calc.subtraction(num1, num2)
                # output result
                print('\n', dffrnc)
            elif operation == '*':
                prdct = calc.multiplication(num1, num2)
                # output result
                print('\n', prdct)
            elif operation == '/':
                qtnt = calc.division(num1, num2)
                # output result
                print('\n', qtnt)

        # check for errors
        except ValueError:
            print('\nOnly Numbers allowed!')
        except TypeError:
            print('\nAn Error has Occured.')