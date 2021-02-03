# **HackerRank-Python**
-----
## **Built-Ins**

### **1. Input()**
This challenge is only forPython 2.

**input()**
In **Python 2**, the expression input() is equivalent to eval(raw _input(prompt)).

**Code**
```
>>> input()  
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'
```
**Task**
You are given a polynomial **P** of a single indeterminate (or variable), **x**.
You are also given the values of **x** and **k**. Your task is to verify if **P(x) == k**.

**Constraints**
All coefficients of polynomial **P** are integers.
**x** and **y** are also integers.

**Input Format**
The first line contains the space separated values of **x** and **k**.
The second line contains the polynomial **P**.

**Output Format**
Print `True` if **P(x)==k**. Otherwise, print False.

**Sample Input**
```
1 4
x**3 + x**2 + x + 1
```
**Sample Output**
```
True
```
**Explanation**
**P(1) = 1^3 + 1^2 + 1 + 1 = 4 = k**
Hence, the output is `True`.

```py
ui = input().split()
x = int(ui[0])
print(eval(input()) == int(ui[1]))
```

### **2. Python Evaluation**
The eval() expression is a very powerful built-in function of Python. It helps in evaluating an expression. The expression can be a Python statement, or a code object.

For example:
```
>>> eval("9 + 5")
14
>>> x = 2
>>> eval("x + 3")
5
```
Here, `eval()` can also be used to work with Python keywords or defined functions and variables. These would normally be stored as strings.

For example:
```
>>> type(eval("len"))
<type 'builtin_function_or_method'>
Without eval()

>>> type("len")
<type 'str'>
```
**Task**
You are given an expression in a line. Read that line as a string variable, such as var, and print the result using eval(var).

**NOTE:** Python2 users, please import `from __future__ import print_function`.

**Constraint**
Input string is less than 100 characters.

**Sample Input**
```
print(2 + 3)
```
**Sample Output**
```
5
```
```py
eval(input())
```

### **3. Athlete Sort**
You are given a spreadsheet that contains a list of **N** athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the **K**th attribute and print the final resulting table. Follow the example given below for better understanding.

image

Note that **K** is indexed from **0** to **M-1**, where **M** is the number of attributes.

**Note:** If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

**Input Format**
The first line contains **N** and **M** separated by a space.
The next **N** lines each contain **M** elements.
The last line contains **K**.

**Constraints**
- **1 <= N,M <= 1000**
- **0 <= K <= M**
- Each element **<= 1000** 

**Output Format**
Print the **N** lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

**Sample Input 0**
```
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
```
**Sample Output 0**
```
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
```
**Explanation 0**
The details are sorted based on the second attribute, since **K** is zero-indexed.
```py
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = [list(map(int, input().split())) for i in range(n)]
    k = int(input())
    nums.sort(key=lambda x: x[k])
    for line in nums: print(*line, sep=' ')
```

### **4. Any or All**
**any()**
This expression returns `True` if **any** element of the iterable is true.
If the iterable is empty, it will return `False`.

**Code**
```
>>> any([1>0,1==0,1<0])
True
>>> any([1<0,2<1,3<2])
False
```
**all()**
This expression returns `True` if **all** of the elements of the iterable are true. If the iterable is empty, it will return `True`.

**Code**
```
>>> all(['a'<'b','b'<'c'])
True
>>> all(['a'<'b','c'<'b'])
False
```
**Task**
You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

**Input Format**
The first line contains an integer **N**. **N** is the total number of integers in the list.
The second line contains the space separated list of **N** integers.

**Constraints**
- **0 < N < 100**

**Output Format**
Print True if all the conditions of the problem statement are satisfied. Otherwise, print `False`.

**Sample Input**
```
5
12 9 61 5 14 
```
**Sample Output**
True

**Explanation**
**Condition 1:** All the integers in the list are positive.
**Condition 2:** 5 is a palindromic integer.

Hence, the output is `True`.

Can you solve this challenge in `3 lines of code or less?`
There is `no penalty` for solutions that are correct but have more than 3 lines.
```py
N,n = int(input()),input().split()
print(all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n]))
```
### **5. ginortS**
You are given a string **S**.
**S** contains alphanumeric characters only.
**(IMAGE)** Your task is to sort the string **S** in the following manner:
- All sorted lowercase letters are ahead of uppercase letters.
- All sorted uppercase letters are ahead of digits.
- All sorted odd digits are ahead of sorted even digits.

**Input Format**
A single line of input contains the string **S**.

**Constraints**
- **0<len(S)<1000**

**Output Format**
Output the sorted string **S**.

**Sample Input**
```
Sorting1234
```
**Sample Output**
```
ginortS1324
```
```py
print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')
```