import pandas as pd

print('you can enter name and marks of a student here and we would automatically feed it in excel')
name = [input('enter name of student : ')]
marks = (input('enter marks of student of 4 subjects respectively : ')) 
marks = marks.split(",")
converted_marks = []
for i in marks:
  try:
    mark = int(i)  # Try to convert string to integer
    converted_marks.append(mark)
    print(f"Converted: {mark}")
  except ValueError:
    print('enter marks in valid format')
 

