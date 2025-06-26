import pandas as pd

orignal_data = []
print('enter 1 for entering data in excel \n enter 2 for viewing the entered data')
while True:
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
            print(f"Converted: {mark}")
          except ValueError:
            print('enter marks in valid format')


        converted_marks.append(name)
        new_list = converted_marks
        new_list.reverse()
        print(new_list)
        orignal_data = orignal_data + new_list


    else:
      print('entered data is :  ')
      print(orignal_data)



    
    