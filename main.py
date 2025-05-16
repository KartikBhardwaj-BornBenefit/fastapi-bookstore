
while True:
    print('Do you want to perform a calculation? (y/n)')
    a = input("Enter 'y' to proceed: ")

    if a.lower() != 'y':
        print("Goodbye!")
        break

    x = float(input('Enter the first number: '))
    y = float(input('Enter the second number: '))

    print('Enter the value z as:')
    print('1 for addition')
    print('2 for subtraction')
    print('3 for multiplication')
    print('4 for division')

    z = float(input('Enter your choice (1-4): '))

    if z == 1:
        print('You chose addition:', x + y)
    elif z == 2:
        print('You chose subtraction:', x - y)
    elif z == 3:
        print('You chose multiplication:', x * y)
    elif z == 4:
        if y == 0:
            print('Error: Cannot divide by zero')
        else:
            print('You chose division:', x / y)
    else:
        print('Invalid operation choice')
