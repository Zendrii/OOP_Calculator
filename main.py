from child_class import Calculation

clclt = Calculation()
clclt

# Ask if the user wants to try again or not
choice = input('\nDo you want to try again? y/n  ')

# if yes, restart the program
if choice == 'y':
    clclt
# If no, the program will exit
elif choice == 'n':
    print('\nThank you!')

    print('\n', '\033[92m='*150)