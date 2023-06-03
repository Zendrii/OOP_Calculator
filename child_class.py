class Objects:
    # import functions from parent class
    from calculator_class import Calculator

    # create objects to use
    calc = Calculator()

    # ask user for operation to be used
    operation = input('\nEnter operation: [ + | - | * | / ] ')

    # ask user for numbers to be used
    num1 = input('\nEnter 1st number: ')
    num2 = input('\nEnter 2nd number: ')

# add/create a new class that inherits the functions from parent class
