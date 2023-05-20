def main():
    print('\n', '\033[92m='*150)

    # import functions from class
    from calculator_class import Calculator

    # create objects to use
    calc = Calculator()

    # other variables needed:
    add_list = ['+', 'add', 'Add', 'addition', 'Addition']
    subtra_list = ['-', 'subtract', 'Subtract', 'subtraction', 'Subtraction']
    multi_list = ['x', '*', 'multiply', 'Multiply', 'multiplication', 'Multiplication']
    divi_list = ['/', 'divide', 'Divide', 'division', 'Division']

    # ask user for operation to be used
    operation = input('\nEnter operation:(or press q to quit) ')

    # ask user for numbers to be used
    num1 = input('\nEnter 1st number: ')
    num2 = input('\nEnter 2nd number: ')

    try:
        # calculate inputs using funtions from class
        if operation in add_list:
            sum = calc.addition(num1, num2)
            # output result
            print('\n', sum)
        elif operation in subtra_list:
            dffrnc = calc.subtraction(num1, num2)
            # output result
            print('\n', dffrnc)
        elif operation in multi_list:
            prdct = calc.multiplication(num1, num2)
            # output result
            print('\n', prdct)
        elif operation in divi_list:
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