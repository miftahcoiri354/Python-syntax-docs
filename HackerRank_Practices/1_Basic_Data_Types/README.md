
# **HackerRank-Python**
-----
## **Basic Data Types**

### **1. List Comprehension**
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
    x, y, z, n = [int(input()) for _ in range(4)]
    array_list = [[xx,yy,zz] for xx in range(x+1) for yy in range(y+1) for zz in range(z+1)]
    array_list_final = [array for array in array_list if array[0]+array[1]+array[2] != n]  
    print(array_list_final)
```
```
input   : 1
          1
          1
          2
output  :  [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

### **2. Nested Lists**
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
#student_list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]] 
#student_list = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]] 
student_list = [[input(), float(input())] for _ in range(int(input()))]
unique_score = [score for score in set([list[1] for list in student_list])]
unique_score.sort()
lowest_scores = unique_score[1:2]
    
group_list = [list[0] for score in lowest_scores for list in student_list if list[1] == score]
group_list.sort()
for x in group_list:
    print(x)
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

### **3. Finding the Percentages**
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

### **4. Lists**
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

### **5. Tuples**
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
