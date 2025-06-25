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

  print(f"ROW {i}: {' || '.join(formatted_row)}")

while True:
  print('enter 1 to add new student' )
  print('enter 2  to exit, or to find percentage of a student')
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
    print('now i guess you need to find percentage of a student, just enter the name of student and relax.....',100*"*")
    print('or if you just want to exit enter exit \n or if you want avg, enter percentage')
    user_choice = input('enter your choice :   ')
    if user_choice == 'exit':
      break
    elif user_choice == 'percentage':
      print('please select name of the student you wanna find percentage of :   ')
      student_name = input('enter name of the student:   ')
      found = False
      for i, row in enumerate(my_class):
        for j, cell in enumerate(row):
          if str(cell) == student_name:
           found = True
           total = row[1] + row[2] + row[3] + row[4]
           percentage = (total /400)*100
           print('percentage of', student_name, 'is', percentage)
           
      if not found:
        print(f"'{student_name}' not found in the table")

  else :
    print('invalid choice')






