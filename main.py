
def cel_fan(x):
    return (x * 9/5) + 32

def km_miles(y):
    return y * 0.621371

def inr_usd(z):
    return z * 0.012

def reusable_function():
    print('\t you need to choose the options wisely for what you want to achieve\n1. cel to far \n2. km to miles \n3. inr to usd \nand 4. to exit')

    num = int(input('enter the number: '))

    if num == 1:
        x = float(input('enter the celcius value: '))
        print(cel_fan(x))
    elif num == 2:
        y = float(input('enter the km value: '))
        print(km_miles(y))
    elif num == 3:
        z = float(input('enter the value of z: '))
        print(inr_usd(z))
    else:
        print('you chose to exit')
        return

    print('if you want to try again then just type A')
    TRY_AGAIN = input('enter the value at once: ')

    if TRY_AGAIN == "A":
        reusable_function()  # This creates the loop by calling the function again

# Start the program
reusable_function()
