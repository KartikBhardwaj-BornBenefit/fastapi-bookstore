# A smart to do list with categories, deadlines and auto sorting def to_do_list(*tasks)
from datetime import datetime
def to_do_list(tasks,timestamps):
  for task in tasks:
    print(sorted(f"task:{task}"))

  for timestamp in timestamps :
     print(sorted(f"timestamp:{timestamp}"))

tasks =['do 12 hours of coding']
timestamps = ['6:00am']
while True:
  tasks.append(input('enter a task:  '))
  timestamps.append(datetime.now())
  to_do_list(tasks,timestamps)
  print('if you want to remove a task enter 1\n \t if its alll for today enter 2\n')
  your_input = input('enter your choice:  ')
  if your_input == '1' :
    tasks.pop(input('enter the task you want to remove: '))
  elif  your_input == '2' :
    print('thanks , best of luck for your tasks and have a nice day')
    break
  else:
    continue
  

