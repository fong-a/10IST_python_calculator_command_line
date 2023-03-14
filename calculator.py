def calculate(): #base menu
    operation = input("""
Please type in the math operation you would like to complete:
{+} for addition
{-} for subtraction
{*} for multiplication
{/} for division

Type [0] to quit.
-------------------------
Enter your requested operation: """)

    print("")

    if operation == '+': #addition function
        print("""
::::::::::::::::::::::::
        """)
        try:
            number_1 = int(input('Please enter the first number: '))
            number_2 = int(input('Please enter the second number: '))
            print("")
            print('{} + {} = '.format(number_1, number_2))
            print(number_1 + number_2)

            again() #asks the user if they would like to calculate another operation
        except:
            print("""
            
Error: Please enter an integer!
--------------""")

            again()

    elif operation == '-': #subtraction function
        print("""
::::::::::::::::::::::::
        """)
        try:
            number_1 = int(input('Please enter the first number: '))
            number_2 = int(input('Please enter the second number: '))
            print('{} - {} = '.format(number_1, number_2))
            print(number_1 - number_2)

            again() #asks the user if they would like to calculate another operation
        except:
            print("""

Error: Please enter an integer!
--------------""")

            again()

    elif operation == '*': #multiplication function
        print("""
::::::::::::::::::::::::
        """)

        try:
            number_1 = int(input('Please enter the first number: '))
            number_2 = int(input('Please enter the second number: '))
            print('{} * {} = '.format(number_1, number_2))
            print(number_1 * number_2)

            again() #asks the user if they would like to calculate another operation
        except:
            print("""

Error: Please enter an integer!
--------------""")

            again()

    elif operation == '/': #division function
        print("""
::::::::::::::::::::::::
        """)
        try:
            number_1 = int(input('Please enter the first number: '))
            number_2 = int(input('Please enter the second number: '))

            if number_2 != 0:
                print('{} / {} = '.format(number_1, number_2))
                print(number_1 / number_2)
            
                again() #asks the user if they would like to calculate another operation
            else: #if user throws in a 1/0, return an error so the calculator doesn't break
                print("""
Error: Cannot divide by 0!
--------------""")

                again() #asks the user if they would like to calculate another operation
        except:
            print("""

Error: Please enter an integer!
--------------""")

            again()
    
    elif operation == "0": #quit function
        print("""--------------
Terminating program. See you next time!
""")
        quit()

    else: #if user enters an invalid command, return menu and display error
        print('You have not typed a valid operator, please run the program again.')
        calculate()

    


#old code below that didn't work/weren't necessary:

####    elif operation == '**':
##       print('{} / {} = '.format(number_1, number_2))
##        print(number_1 ** number_2)



    # elif operation == 'subtraction':        #word version of operations
    #     print('{} - {} = '.format(number_1, number_2))
    #     print(number_1 - number_2)

    # elif operation == 'multiplication':
    #     print('{} * {} = '.format(number_1, number_2))
    #     print(number_1 * number_2)

    # elif operation == 'division':
    #     print('{} / {} = '.format(number_1, number_2))
    #     print(number_1 / number_2)
    # elif operation == 'addition':
    #     print('{} / {} = '.format(number_1, number_2))
    #     print(number_1 + number_2)
##    elif operation == 'squared':
##        print('{} / {} = '.format(number_1, number_2))
##        print(number_1 ** number_2)

    # again() to repeat function

def again(): #blanket again function
    calc_again = input('''
// Do you want to calculate again?
Type [Y] for Yes or [N] for No.

Enter: ''')

    if calc_again.upper() == 'Y':
        print("""

------------------------- """)
        calculate()
    elif calc_again.upper() == 'N':
        print("""
--------------
Terminating program. See you next time!
""")
    else:
        print("Invalid command.")
        again()


#first time starting up menu
print("""
=========================
:::::[ CALCULATOR ]::::::
=========================
// By Devon Kawaguchi""")
calculate()
