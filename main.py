from numpy import exceptions
import pandas as pd
def excel_automation():
  headers = orignal_data[0]

  students = []
  for row in orignal_data[1:] :
    student_dict = dict(zip(headers, row))
    total = student_dict['eng_marks'] + student_dict['math_marks'] + student_dict['sci_marks'] + student_dict['comp_marks']
    student_dict['percentage'] = round(total/4,2)
    students.append(student_dict)
  df = pd.DataFrame(students)
  df.to_excel("student_marksheet.xlsx", index= False, engine= 'openpyxl')
  print("Excel file 'student_marksheet.xlsx' created successfully.")



orignal_data = [['name', 'eng_marks', 'math_marks', 'sci_marks', 'comp_marks']]


while True:

  print('enter 1 for entering data in excel \n enter 2 for viewing the entered data')

  user_choice = int(input('enter your choice :  '))
  if user_choice == 1 :
    print('you can enter name and marks of a student here and we would automatically feed it in excel')
    name = input('enter name of student : ')
    marks = (input('enter marks of student of 4 subjects respectively : ')) 
    marks = marks.split(",")
    converted_marks = []
    for i in marks:
      try:
        mark = int(i)  
        converted_marks.append(mark)

      except ValueError:
        print('enter marks in valid format')


    converted_marks.append(name)
    new_list = converted_marks
    new_list.reverse()
    orignal_data.append(new_list)
    print(20*'*','DATA STORED SUCCESSFULLY',20*'*')


  else:
    print('entered data is :  ')
    print(orignal_data)
    print(' do you want to continue or exit and move to excel')
    user_choice_2 = input('enter your choices :  ')
    if user_choice_2 == 'continue':
      continue
    elif user_choice_2 == 'exit' :
      excel_automation()

      break