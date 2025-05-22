color = ['blue', 'green' , 'red' ]
color.append('yellow')
print(color)
t1 = ['a', 'b','c']
t2 =['d', 'e']
t3 = ['f']
t1.extend(t2)
print(t1)
t1.insert(2,'i')
print(t1)
print(t1 + t2)