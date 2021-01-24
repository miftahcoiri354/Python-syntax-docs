def takeSecond(elem):
    return elem[1]
def takeFirst(elem):
    return elem[0]

name_list = []
score_list = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    name_list.append(name)
    score_list.append(score)

student_list = []
for i in range(len(name_list)):
    python_students = [name_list[i], score_list[i]]
    student_list.append(python_students) 

#student_list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]] 
#student_list = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]] 
student_list.sort(key=takeSecond)

scores = [score[1] for score in student_list]
unique_values = [x for x in set(scores)]
unique_values.sort()
unique_values = unique_values[0:2]

group_list = []
for value in unique_values:
  this_group = []
  this_group.append(value)
  for list in student_list:
    if list[1] == value:
      this_group.append(list[0])
      
  group_list.append(this_group)

group_list.sort(key=takeFirst)

x = group_list[1]
x.remove(x[0])
x.sort()
for y in x:
  print(y)