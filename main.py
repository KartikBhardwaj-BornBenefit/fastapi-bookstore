if a== 'y':
  x = float(input('enter the first number:    '))
  y = float(input('enter the second number:   '))

  print('enter the value z as 1 for addition,  2 for subtraction, 3 for multiplication, 4 for division ')

  z = float(input('enter the value of z as stated above:     '))

  if z ==1:
      print('you chose addition' , x+y)

  elif z ==2:
    print(' you chose division' , x-y)

  elif z ==3:
    print('you chose multiplication' , x*y)

  elif z ==4:
    print('you chose division' , x/y)
  else: 
    if y == 0:
      print('error')

  

print('do you want to continue with any other operation or any other numbers?')
print(' press y for yes and n for no')
a = input("Enter 'y' to proceed: ")  # Prompt the user to input a value
if a == 'y':
    print("You chose yes!")
else:
    print("You didn't choose yes.")