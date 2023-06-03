def main():
    from child_class import Calculation

    clclt = Calculation()
    
    clclt.clcltn()

while True:
    main()

    # Ask if the user wants to try again or not
    choice = input('\nDo you want to try again? y/n  ')

    # If no, the program will exit
    if choice == 'n':
        print('\nThank you!')

        print('\n', '\033[92m='*150)
        
        break