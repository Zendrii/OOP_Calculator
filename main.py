def main():
    print('\n', '\033[92m='*150)

    # import functions from class
    from calculator_class import Calculator

    # create objects to use
    calc = Calculator()

    # ask user for operation to be used
    operation = input('\nEnter operation: [ + | - | * | / ] ')

    # ask user for numbers to be used
    num1 = input('\nEnter 1st number: ')
    num2 = input('\nEnter 2nd number: ')

    try:
        # calculate inputs using funtions from class
        if operation == '+':
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
    
while True:
    main()

    # Ask if the user wants to try again or not
    choice = input('\nDo you want to try again? y/n  ')

    # If no, the program will exit
    if choice == 'n':
        print('\nThank you!')

        print('\n', '\033[92m='*150)

        break