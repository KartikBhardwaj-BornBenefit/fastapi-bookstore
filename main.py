def calcsum(a,b,c) :
  s = a+b+c
  return s

def average(x,y,z) :
  sm = calcsum(x,y,z)
  return sm/3

num1 = int(input("number 1 :  "))
num2 = int(input("number 2 :  "))
num3 = int(input("number 3 :  "))
print('average is ', average(num1, num2, num3))
print('sum is ', calcsum(num1,num2, num3))

  
  
