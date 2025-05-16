# program to calculate and print roots of quadratic equation ax^2 + bx + c = 0
print('welcome, let\'s calculate the roots of quadratic equation ax^2 + bx + c =0\nremember a must not be equal to 0')
print('please enter the values of a,b and c respectively')
a = float(input('enter the value of a:   '  ))
if a==0:
  print('thanks for your time but we can\'t go any further')
  break

b = float(input('enter the value of b:    '))
c = float(input('enter the value of c:    '))
print("calculating the roots of the equation")
print('**********************************************************************************************')
print('the value of first root is ', (-b + (b**2 - 4*a*c)**(1/2))/(2*a) )
print('the value of second root is ', (-b - (b**2 - 4*a*c)**(1/2))/(2*a) )