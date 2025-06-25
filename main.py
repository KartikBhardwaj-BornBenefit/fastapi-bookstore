import pandas as pd

my_class = [['student' , 'eng_marks' , 'math_marks', 'sci_marks', 'comp_marks'],['kartik',90,9,8,91],
  ['john',88,99,100,90]
 ,['bob',89,76,78,99,]
 ,['tarini',10,91,92,9]]

headers = my_class[0]

students = []
for row in my_class[1:] :
  student_dict=dict(zip(headers,row))
  print(student_dict)
  students.append(student_dict)

print(students)
  