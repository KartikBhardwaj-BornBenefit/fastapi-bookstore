import pandas as pd

my_class = [['student' , 'eng_marks' , 'math_marks', 'sci_marks', 'comp_marks'],['kartik',90,9,8,91],
  ['john',88,99,100,90]
 ,['bob',89,76,78,99,]
 ,['tarini',10,91,92,9]]

headers = my_class[0]

students = []
for row in my_class[1:] :
  student_dict=dict(zip(headers,row))
  total = student_dict['eng_marks'] + student_dict['math_marks'] + student_dict['sci_marks'] + student_dict['comp_marks']
  student_dict['percentage'] = round(total/4,2)
  students.append(student_dict)
  df = pd.DataFrame(students)
  df.to_csv("student_marksheet.csv", index= False, )
  print("Excel file 'student_marksheet.xlsx' created successfully.")