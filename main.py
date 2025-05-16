# program that reads two numbers and an arithmetic operatorand displays the computed result
num1 = float(input('enter the first number:  '))
num2 = float(input('enter the second number:  '))
print(' select the operator you want to apply on your given two numbers i.e +,-,*,/ ')
op = input('enter the o[perator:   ')
if op == '+':
  print("you chose addition", num1 + num2)
elif op == '-':
  print('you chose subtraction' , num1- num2)
elif op == '*':
  print('you chose multiplication', num1*num2)

elif op == '/':
  print('you chose division', num1/num2)
  if num2 == 0 :
    print('zero can\'t be the denominator')