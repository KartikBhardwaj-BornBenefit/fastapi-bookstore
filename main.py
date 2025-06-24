def main_function(cells):
  for i, row in enumerate(cells):
    formatted_row = []
    for n in range(len(row)):
      formatted_row.append(f"{row[n]:^15}")
    print(f"ROW{i}: {' || '.join(formatted_row)}")


my_class = [['student' , 'eng_marks' , 'math_marks', 'sci_marks', 'comp_marks'],['kartik',90,9,8,91],
  ['john',88,99,100,90]
 ,['bob',89,76,78,99,]
 ,['tarini',10,91,92,9]]
for i, row in enumerate(my_class):
  formatted_row = []
  formatted_row.append(f"{row[0]:^12}")      
  formatted_row.append(f"{row[1]:^10}")        
  formatted_row.append(f"{row[2]:^10}")      
  formatted_row.append(f"{row[3]:^10}")      
  formatted_row.append(f"{row[4]:^10}")      

  print(f"ROW{i}: {' || '.join(formatted_row)}")

while True:
  print('enter 1 to add new student' )
  print('enter 2  to exit')
  x= int(input('enter your choice :  '))
  if x==1 :
    print('please enter the details of new student ')
    print(50*"*")
    name = input("enter the name of student :  ")
    eng_marks = int(input('enter marks of english subject:  '))
    math_marks = int(input('enter marks of math subject:  '))
    sci_marks = int(input('enter marks of science subject:  '))
    comp_marks = int(input('enter marks of computer subject:  '))
    my_class.append([name,eng_marks,math_marks,sci_marks,comp_marks])
    print("\nUpdated table:")
   

  elif x==2 :
    main_function(my_class)
    break


  else :
    print('invalid choice')





