my_class = [['student' , 'eng_marks' , 'math_marks', 'sci_marks', 'comp_marks'],['kartik',90,9,8,91],
            ['john',88,99,100,90]
           ,['bob',89,76,78,99,]
           ,['tarini',10,91,92,9]]
for i, row in enumerate(my_class):
  for row in my_class:
    formatted_row =[]
    formatted_row.append(f"{row[0]:^10}")
  print(f"ROW{i}:{row}")
  print(formatted_row)


 