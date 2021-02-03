# **HackerRank-Python**
-----
## **Strings**

### **1. String Split and Join**
In Python, a string can be split on a delimiter.
**Example:**
```
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
```
joining a string is simple:
```
>>> a = "-".join(a)
>>> print a
this-is-a-string 
```
**Task**
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

**Input Format**
The first line contains a string consisting of space separated words.

**Output Format**
Print the formatted string as explained above.

**Sample Input**
```
this is a string
```
**Sample Output**
```
this-is-a-string
```
```python
def split_and_join(line):
    # write your code here
    return line.replace(' ', '-')
    #return '-'.join(line.split())

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
```

### **2. What is Your Name?**

You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
```
Hello firstname lastname! You just delved into python.
```
**Input Format**
The first line contains the first name, and the second line contains the last name.

**Constraints**
The length of the first and last name ≤ **10**.

**Output Format**
Print the output as mentioned above.

**Sample Input 0**
```
Ross
Taylor
```
**Sample Output 0**
```
Hello Ross Taylor! You just delved into python.
```
**Explanation 0**
The input read by the program is stored as a string data type. A string is a collection of characters.
```python
def print_full_name(a, b):
    print(f"Hello {a} {b}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
```

### **3. Mutations**

We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.

**Example**
```
>>> string = "abracadabra"
```
You can access an index by:
```
>>> print string[5]
a
```
What if you would like to assign a value?
```
>>> string[5] = 'k' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```
How would you approach this?
- One solution is to convert the string to a list and then change the value.

**Example**
```
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
````
- Another approach is to slice the string and join it back.

Example
```
>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra
```

**Task**
Read a given string, change the character at a given index and then print the modified string.

**Input Format**
The first line contains a string, .
The next line contains an integer , denoting the index location and a character  separated by a space.

**Output Format**
Using any of the methods explained above, replace the character at index  with character .

**Sample Input**
```
abracadabra
5 k
```
Sample Output
```
abrackdabra
```
```python
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
```

### **4. Find a String**
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

**NOTE**: String letters are case-sensitive.

**Input Format**
The first line of input contains the original string. The next line contains the substring.

**Constraints**
**1<=len(string)>=200**
Each character in the string is an ascii character.

**Output Format**
Output the integer number indicating the total number of occurrences of the substring in the original string.

**Sample Input**
```
ABCDCDC
CDC
```
**Sample Output**
```
2
```
**Concept**
Some string processing examples, such as these, might be useful.
There are a couple of new concepts:
In Python, the length of a string is found by the function len(s), where **s** is the string.
To traverse through the length of a string, use a for loop:
```
for i in range(0, len(s)):
    print (s[i])
```
A range function is used to loop over some length:
```
range (0, 5)
```
Here, the range loops over **0** to **4**. **5** is excluded.
```python
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
```

### **5. String Validators**

Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

*str.isalnum()*
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
```
>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False
```
*str.isalpha()*
This method checks if all the characters of a string are alphabetical (a-z and A-Z).
```
>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
```
*str.isdigit()*
This method checks if all the characters of a string are digits (0-9).
```
>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
```
*str.islower()*
This method checks if all the characters of a string are lowercase characters (a-z).
```
>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
```
*str.isupper()*
This method checks if all the characters of a string are uppercase characters (A-Z).
```
>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
```
**Task**
You are given a string **S**.
Your task is to find out if the string **S** contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

**Input Format**
A single line containing a string **S**.

**Constraints**
**0 < len(S) < 1000**

**Output Format**
- In the first line, print `True` if **S** has any **alphanumeric** characters. Otherwise, print `False`.
- In the second line, print `True` if **S** has any **alphabetical** characters. Otherwise, print `False`.
- In the third line, print `True` if **S** has any **digits**. Otherwise, print `False`.
- In the fourth line, print `True` if **S** has any **lowercase** characters. Otherwise, print `False`.
- In the fifth line, print `True` if **S** has any **uppercase** characters. Otherwise, print `False`.

**Sample Input**
```
qA2
```
**Sample Output**
```
True
True
True
True
True
```

```python
if __name__ == '__main__':
    s = raw_input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
```

### **6. Text Alignment**
In python, a string of text can be aligned left, right, and center.
**.ljust(width)**
This method returns a left aligned string of length width.
```
>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  
```
**.center(width)**
This method returns a centered string of length width.
```
>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----
```
**.rjust(width)**
This method returns a right alighned string of length width.
```
>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank
```
**Task**
You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

**Input Format**
A single line containing the thickness value for the logo.
```
5
```
**Constraints**
The thickness must be an odd number.
**0<thickess<50**

**Output Format**
Output the desired logo.
```
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
```
**Template**
```python
#Replace all ______ with rjust, ljust or center. 

thickness = int(raw_input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print (c*i).______(thickness-1)+c+(c*i).______(thickness-1)

#Top Pillars
for i in range(thickness+1):
    print (c*thickness).______(thickness*2)+(c*thickness).______(thickness*6)

#Middle Belt
for i in range((thickness+1)/2):
    print (c*thickness*5).______(thickness*6)    

#Bottom Pillars
for i in range(thickness+1):
    print (c*thickness).______(thickness*2)+(c*thickness).______(thickness*6)    

#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).______(thickness)+c+(c*(thickness-i-1)).______(thickness)).______(thickness*6)
```
**Answer**
```python
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

```

### **7. Text Wrap**
You are given a string **S** and width **w**.
Your task is to wrap the string into a paragraph of width **w**.
**Input Format**
The first line contains a string **S**.
The second line contains the widht **w**.

**Constraints**
- **0 < len(S) <1000**
- **0 < w < len(S)**

**Output Format**
Print the text wrapped paragraph

**Simple Input 0**
```
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
```
**Simple Output 0**
```
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
```
```python
import textwrap

def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
```

### **8. Desinger Door Mat**
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

- Mat size must be **N** X **M**. (**N** is an odd natural number, and **M** is **3** times **N**.)
- The design should have 'WELCOME' written in the center.
- The design pattern should only use |, . and - characters.
**Sample Designs**
```
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
```
**Input Format**
A single line containing the space separated values of **N** and **M**.
```
9 27
```
**Constraints**
- **5<N<101**
- **15<M<303**

**Output Format**
Output the design pattern.
```
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
``` 
```python
if __name__ == '__main__':
    n, m = map(int,raw_input().split())

    pattern = [('.|.'*(2*i + 1)).center(m, '-') for i   in range(n//2)]
    print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
```

### **9. String Formatting**
Given an integer, **n**, print the following values for each integer **i** from **1** to **n**:
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

The four values must be printed on a single line in the order specified above for each **i** from **1** to **n**. Each value should be space-padded to match the width of the binary value of **n**.

**Input Format**
A single integer denoting **n**.
```
17
```

**Constraints**
- **1<= n <= 99**
  
**Output Format**
Print **n** lines where each line **i** (in the range **1<=i<=n**) contains the respective decimal, octal, capitalized hexadecimal, and binary values of **i**. Each printed value must be formatted to the width of the binary value of **n**.
```
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001    
```
```python
def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))
    for i in xrange(1,number+1):
        print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
```

### **10. Alphabet Rangoli**
You are given an integer, **N**. Your task is to print an alphabet rangoli of size **N**. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:
```
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
```

The center of the rangoli has the first alphabet letter a, and the boundary has the **N^th** alphabet letter (in alphabetical order).

**Input Format**
Only one line of input containing **N**, the size of the rangoli.
```
5
```

**Constraints**
- **0 < N < 27**

**Output Format**
Print the alphabet rangoli in the format explained above.
```
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
```

```python
import string
alpha = string.ascii_lowercase

def print_rangoli(size):
    # your code goes here
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(L[:0:-1]+L))


if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
```

### **11. Capitalize!**
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
```python
alison heck ==> Alison Heck
```
Given a full name, your task is to capitalize the name appropriately.

**Input Format**
A single line of input containing the full name, **S**.
```
chris alan
```

**Constraints**
- **0 < len(S) < 1000**
- The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

**Output Format**
Print the capitalized string, **S**.
```
Chris Alan
```
```python
#!/bin/python
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    print(s)
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
```

### **12. The Minion Game**
Kevin and Stuart want to play the **'The Minion Game'**.

**Game Rules**
Both players are given the same string, **S**.
Both players have to make substrings using the letters of the string **S**.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

**Scoring**
A player gets +1 point for each occurrence of the substring in the string **S**.

**For Example:**
String **S** = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:
```
Image
```
Your task is to determine the winner of the game and their score.

**Input Format**

A single line of input containing the string **S**.
Note: The string  will contain only uppercase letters: **[A-Z]**.

**Constraints**
- **0 < len(S) <= 10^6**

**Output Format**
Print one line: the name of the winner and their score separated by a space. If the game is a draw, print Draw.

**Sample Input**
```
BANANA
```
**Sample Output**
```
Stuart 12
```
**Note :** Vowels are only defined as **AEIOU**. In this problem, **Y** is not considered a vowel.

```
def minion_game(string):
    # your code goes here
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
            
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
```

### **13. Merge the Tools!**

```python
def merge_the_tools(string, k):
    # your code goes here
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
```

