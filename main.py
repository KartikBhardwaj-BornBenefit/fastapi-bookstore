my_class = [['student' , 'eng_marks' , 'math_marks', 'sci_marks', 'comp_marks'],['kartik',90,9,8,91],
            ['john',88,99,100,90]
           ,['bob',89,76,78,99,]
           ,['tarini',10,91,92,9]]
for i, row in enumerate(my_class):
    formatted_row = []
    formatted_row.append(f"{row[0]:<12}")      # Student names, left-aligned
    formatted_row.append(f"{row[1]:>10}")      # English marks, right-aligned  
    formatted_row.append(f"{row[2]:>10}")      # Math marks, right-aligned
    formatted_row.append(f"{row[3]:>10}")      # Science marks, right-aligned
    formatted_row.append(f"{row[4]:>10}")      # Computer marks, right-aligned
    
    print(f"ROW{i}: {' | '.join(formatted_row)}")


 