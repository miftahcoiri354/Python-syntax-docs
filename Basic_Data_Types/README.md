# **HackerRank-Python**

### **1. Say "Hello, World!" with Python**
```python
print'Hello, World!'
```
```
Hello, World!
```
### **2. Python If-Else**
**Task** Given an integer, n perform the following conditional actions:
- if **n** is odd, print *Weird*
- if **n** is even and in the inclusive range of 2 to 5, print *Not Weird*
- if **n** is even and in the inclusive range of 6 to 20, print *Weird*
- if **n** is even and greater than 20, print *Not Weird*
  
**Input Format**
A single line containing a positive integer *n*.
**Constraints**
- 1 <= n <= 100

**Output Format**
Print Weird if the number is `Weird`. Otherwise, print `Not Weird` 
**Answer:** 
```python
if __name__ == '__main__':
    n = int(raw_input().strip())
    if (n % 2) == 0:
        if 2 <= n <= 5 or n > 20:
            print("Not Weird")
        elif 5 <= n <= 20:
            print("Weird")
    elif (n % 2) != 0:
        print("Weird")
```
```
input : 3
output: Weird
```
### **3. Arithmetic Operators**
**Task** The provided code stup reads two integers from STDIN, *a* and *b*, add code to print three lines, where:
1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers(first-second).
3. The third line contains the product of the two numbers.

**Example**
- *a == b*
- *b == 5*

print:
```
8
-2
15
```
**Input Format**
The first line contains the first integer **a**.
The second line contains the second integer **b**.
**Constraints**
- 1 <= a <= 10^10 
- 1 <= b <= 10^10
  
**Output Format**
Print the three lines as explained above
```python
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a+b)
    print(a-b)
    print(a*b)
```
### **4. Python Division**
**Task** The provided code stub reads two integers, *a* and *b* from STDIN
Add logic to print two lines. The first line should contain the result of integer division, *a//b*. The second line should contain the result of float division *a/b*. No rounding or formating is necessary.
**Example**
- a = 3
- b = 5
    - The result of the integer division **3//5=0**
    - The result of the float division is **3/5=0.6**

**Input Format**
The first line contains the first integer, **a**.
The second line contains the second integer, **b**.
**Output Format**
Print the two lines as described above.
```python
from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

    print(a//b)
    print(a/b)
```
```
Input   : 4
          3
Output  : 1
          1.33333
```
### **5. Loops**
**Task** The provided code stub read and integer, **n** from STDIN. For all non-integers *i<n* print *i^2*.
**Example**
- n = 3
The list of non-negative integers that are less than n = 3 is [0,1,2] print the square of each number on a separate line.
```
0
1
4
```

**Input Format**
The first and only line contains the integer, *n*.
**Constraints**
- 1<= n <= 20

**Output Format**
Print **n** lines, one corrsponding to each **i**.
```python
if __name__ == '__main__':
    n = int(raw_input())
    
    for i in range(n):
        print(i*i)
```
```
input   : 5
output  : 0
          1
          4
          9
          16
```

### **6. Write a Function**
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:
- The year can be evenly divided by 4, is a leap year, unless:
    - The year can be evenly divided by 100, it is NOT a leap year, unless:
        - The year is also evenly divisible by 400. Then it is a leap year.
  
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. 
**Task**
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
**Input**
Read **year** the year in test
**Constaints**
- 1900 <= year <=10^5

**Output Format**
The function must return a Boolean Value (True/False). Output is handled by the provided code stub.
```python
def is_leap(year):
    leap = False
    
    # Write your logic here

    x = [1800, 1900, 2100, 2200, 2300, 2500]
    
    # Write your logic here
    if (year % 4) == 0:
      leap = True
      if year in x:
        leap = False
    else:
        leap = False
    return leap

year = int(raw_input())
```

```
input   : 1900
output  : False
```
### **7. List Comprehension**
Ler's learn about list comprehensions! You're given three integers, **x**, **y**, **z** representing the dimensions of a cuboid along with an integer **n**. Print a list of all possible coordinates given by **(i,j,k)** on a 3D grid where the sum of **i+j+k** is not equal to n. Here **0<=i<=x;0<=j=y;0<=k<=z**. Please use list comprehensions rather than multiple loops, as a learning excercise.
**Example**
- x = 1
- y = 1
- z = 2
- n = 3
All permutations of **[i,j,k]** are:
```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
```
print an array of the elements that don't sum to *n=3*.

**Input Format**
Four integers **x,y,z** and **n** each on a separate line.

**Constraints**
Print the list in lexicographic increasing order.
```python
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    array_list = [[xx,yy,zz] for xx in range(x+1) for yy in range(y+1) for zz in range(z+1)]
    array_list_final = []
    for array in array_list:
       sum = array[0] + array[1] + array[2]
       if sum != n:
           array_list_final.append(array)           
    
    print(array_list_final)
```
```
input   : 1
          1
          1
          2
output  :  [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

### **8. Nested Lists**
Given the names and grades for eah student in a class of **N** students, store them in a nested list and print the name(s) of any students having the second lowest grade. 
**Note:** If there are multiple students with the second lowest grade, order their names alphabetically and print each names on a new line.
**example:**
- **rexord = ["chi", 20.0]. ['beta', 50.0], ["alpha", 50.0]]**
  The ordered list of scores in [20.0, 50.0], so the second loswest score is 50.0, there are two students with that score ['beta', 'alpha']. Ordered alphabetically the names are printed as:
  ```
  alpha
  beta
  ```

**Input Format**
The first line constraints an integer, **N**, the number of students.
The **2N** subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

**Constraints**
- **2<= N <=5**
- THere will always be one or more students having the second lowest grade.

**Output Format**
Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

```python
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
```
```
input   : 5
          Harry
          37.21
          Berry
          37.21
          Tina
          37.2
          Akriti
          41
          Harsh
          39
output  : Berry
          Harry
```

### **9. Finding the Percentages**
**Task** provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
**Example**
Marks key:value pairs are
- 'aplha':[20,30,40]
- 'beta':[30,50,70]
- query_name=='beta'
  The **query_name** is 'beta'. beta's average score is **(3-+50+70)/3=50.0**.

**Input Format**
  The first line contains the integer **n**, the number of students records. the next **n** lines contain the names and marks obtained by a student, each value separated by a space. The final line contains **query_name**, the name of a student to query.

```
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```

**Constraints**
- 2 <= n <= 10
- 0 <= marks|i| <= 100
- length of marks arrays = 3

**Output Format**
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

```
56.00
```
```python
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    print('{0:.2f}'.format(sum(student_marks[query_name])/len(student_marks[query_name])))
```

### **10. Lists**
**Task** Consider a list (*list=[]*). You can perform the following commands:
1. **insert i e**: Insert integer e at position i.
2. **print**: Print the list.
3. **remove e**: Delete the first occurrence of integer *e*.
4. **append e**: insert integer *e* at the end of the list.
5. **sort**: Sort the list.
6. **pop**: pop the last element from the list.
7. **reverse**: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be og the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

**Example**
N = 4
append 1
append 2
insert 3 1
print 
```
[1,3,2]
```
**Input Format**
The first line contains an integer, **n**, denoting the number of commands. Each line **i** of the **n** subsequent lines contains one of the commands described above.
```
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
```
**Constraint**
- The elements added to the list must be integers

**Output Format**
For each command of type **print**, print the list on a new line.
```
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
```
```python
if __name__ == '__main__':
    N = int(raw_input())

    l = []
    for _ in range(N):
        s = raw_input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("l."+cmd)
        else:
            print l
```

### **11. Tuples**
**Task**
Given an integer, **n**, and **n** space-separated integers as input, create a tuple, **t**, of those **n** integers. Then compute and print the result of **hash(t)**.
**Note:** *hash()* is one of the functions in the *__builtins__* module, so it need not be imported.
**Input Format**
The first line contains an integer, **n**, denoting the number of elements in the tuple. 
The second line contains **n** space-separated integers describing the elements in tuple **t**.
```
2
1 2
```
**Output Format**
Print the result of **hash(t)**
```
3713081631934410656
```
```python
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    print hash(tuple(integer_list))
```