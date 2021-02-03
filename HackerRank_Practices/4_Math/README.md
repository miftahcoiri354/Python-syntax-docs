# **HackerRank-Python**
-----
## **Math**

### **1. Introduction to Sets**
**Input**
```
10
161 182 161 154 176 170 167 171 170 174
```
**Output**
```
169.375
```
```python
from __future__ import division

def average(array):
    # your code goes here
    return sum(set(array))/len([x for x in set(array)])

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
```

### **2. Find Angle MBC**
**ABC** is a right triangle, **90°** at **B**.
Therefore, **ABC = 90°**.

Point **M** is the midpoint of hypotenuse **AC**.

You are given the lengths **AB** and **BC**.
Your task is to find  **MBC**(angle **0°**, as shown in the figure) in degrees.

**Input Format**
The first line contains the length of side **AB**.
The second line contains the length of side **BC**.

**Constraints**
- **0<AB<=100**
- **0<BC<=100**
- Lengths **AB** and **BC** are natural numbers.
  
**Output Format**
Output **MBC** in degrees.

**Note:** Round the angle to the nearest integer.

**Examples:**
If angle is 56.5000001°, then output **57°**.
If angle is 56.5000000°, then output **57°**.
If angle is 56.4999999°, then output **56°**.
**Input**
```
10
10
```
**Output**
```
45°
```
```python
# -*- coding: utf-8 -*-
import math

AB = float(input())
BC = float(input())
print('%d°' % round(math.degrees(math.atan2(AB,BC)),0))
```

### **3. Mod Divmod**
One of the built-in functions of Python is divmod, which takes two arguments **a** and **b** and returns a tuple containing the quotient of **a/b** first and then the remainder **a**.

For example:
```
>>> print divmod(177,10)
(17, 7)
```
Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.

Task
Read in two integers, **a** and **b**, and print three lines.
The first line is the integer division **a//b** (While using Python2 remember to import division from **__future__**).
The second line is the result of the modulo operator: **a%b**.
The third line prints the divmod of **a** and **b**.

**Input Format**
The first line contains the first integer, **a**, and the second line contains the second integer, **b**.

**Output Format**
Print the result as described above.
**Input**
```
177
10
```
**Output**
```
17
7
(17, 7)
```
```python
print('{0}\n{1}\n({0}, {1})'.format(*divmod(int(input()), int(input()))))
```

### **4. Triangle Quest 2**
You are given a positive integer **N**. Your task is to print a palindromic triangle of size **N**.

For example, a palindromic triangle of size  is:
```
1
121
12321
1234321
123454321
```
You can't take more than two lines. The first line (a for-statement) is already written for you. You have to complete the code using exactly one print statement.

**Note:**
Using anything related to strings will give a score of **0**.
Using more than one for-statement will give a score of **0**.

**Input Format**
A single line of input containing the integer **N**.

**Constraints**
- 0 < N < 10

**Output Format**
Print the palindromic triangle of size  as explained above.
**Sample Input**
```
5
```
**Sample Output**
```
1
121
12321
1234321
123454321
```
```py
for x in range(1,int(input())+1):
    print(((10**x - 1)//9)**2)
```
### **5. Power-Mod Power**
So far, we have only heard of Python's powers. Now, we will witness them!

Powers or exponents in Python can be calculated using the built-in power function. Call the power function **a^b** as shown below:
```
>>> pow(a,b)
``` 
or
```
>>> a**b
```
It's also possible to calculate .
```
>>> pow(a,b,m) 
``` 
This is very helpful in computations where you have to print the resultant % mod.

**Note:** Here, **a** and **b** can be floats or negatives, but, if a third argument is present,  cannot be negative.

**Note:** Python has a math module that has its own pow(). It takes two arguments and returns a float. Frankly speaking, we will never use math.pow().

**Task**
You are given three integers: **a**, **b**, and **m**, respectively. Print two lines. The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).

Input Format
The first line contains **a**, the second line contains **b**, and the third line contains **m**.

**Constraints**
- **1<= a <= 10**
- **1<= b <=10**
- **2 <= m <= 1000**

**Input:**
```
3
4
5
```
**Output:**
```
81
1
```
```py
a,b,m = [int(input()) for _ in '123']
print(pow(a,b),pow(a,b,m),sep='\n')
```
### **6. Integers Come in All Sizes**
Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: **2^31-1** (c++ int) or **2^63-1** (C++ long long int).

As we know, the result of **a^b** grows really fast with increasing **b**.

Let's do some calculations on very large integers.

**Task**
Read four numbers, **a**, **b**, **c**, and **d**, and print the result of **a^b + c^d**.

**Input Format**
Integers **a**, **b**, **c**, and **d** are given on four separate lines, respectively.

**Constraints**
- **1<=a<=1000**
- **1<=b<=1000**
- **1<=c<=1000**
- **1<=d<=1000**

**Output Format**
Print the result of **a^b+c^d** on one line.

**Sample Input**
```
9
29
7
27
```
**Sample Output**
```
4710194409608608369201743232  
```
**Note:** This result is bigger than **2^63 - 1**. Hence, it won't fit in the long long int of C++ or a 64-bit integer.
```py
a,b,c,d = (int(input()) for _ in range(4))
print (pow(a,b)+pow(c,d))
```

### **7. Triangle Quest**
You are given a positive integer **N**. Print a numerical triangle of height **N-1** like the one below:
```
1
22
333
4444
55555
......
```
Can you do it using only **arithmetic operations, a single for loop and print statement?**

Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.

**Note:** Using anything related to strings will give a score of **0**.

**Input Format**
A single line containing integer, **N**.

**Constraints**
- **1<=N<=9**

**Output Format**
Print **N-1** lines as explained above.

**Sample Input**
```
5
```
**Sample Output**
```
1
22
333
4444
```
```py
for i in range(1,int(input())): print((10**(i)//9)*i)
```