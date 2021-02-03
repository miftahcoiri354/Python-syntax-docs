# **HackerRank-Python**
-----
## **Python Function**

### **1. Validating Email Addresses with a Filter**
You are given an integer **N** followed by **N** email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.


Valid email addresses must follow these rules:
- It must have the username@websitename.extension format type.
- The username can only contain letters, digits, dashes and underscores.
- The website name can only have letters and digits.
- The maximum length of the extension is .

**Concept**
A filter takes a function returning True or False and applies it to a sequence, returning a list of only those members of the sequence where the function returned True. A Lambda function can be used with filters.

Let's say you have to make a list of the squares of integers from **0** to **9** (both included).
```
>> l = list(range(10))
>> l = list(map(lambda x:x*x, l))
```
Now, you only require those elements that are greater than **0** but less than **80**.
```
>> l = list(filter(lambda x: x > 10 and x < 80, l))
```
Easy, isn't it?

**Input Format**
The first line of input is the integer **N**, the number of email addresses.
**N** lines follow, each containing a string.

**Constraints**
Each line is a non-empty string.

**Output Format**
Output a list containing the valid email addresses in lexicographical order. If the list is empty, just output an empty list, [].

**Sample Input**
```
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
```
**Sample Output**
```
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
```
```py
import re

def fun(s):
  pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$")
  return pattern.match(s)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
```
### **2. Reduce Function**
Given a list of rational numbers,find their product.

**Concept**
The *reduce()* function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say [1,2,3] and you have to find its sum.
```
>>> reduce(lambda x, y : x + y,[1,2,3])
6
```
You can also define an initial value. If it is specified, the function will assume initial value as the value given, and then reduce. It is equivalent to adding the initial value at the beginning of the list. For example:
```
>>> reduce(lambda x, y : x + y, [1,2,3], -3)
3

>>> from fractions import gcd
>>> reduce(gcd, [2,4,8], 3)
1
```
**Input Format**
First line contains **n**, the number of rational numbers.
The **ith** of next **n** lines contain two integers each, the numerator(**Ni**) and denominator(**Di**) of the **ith** rational number in the list.

**Constraints**
- **1<=n<=100**
- **1<=Ni,Di<=10^9**
  
**Output Format**
Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than **1**.

**Sample Input 0**
```
3
1 2
3 4
10 6
```
**Sample Output 0**
```
5 8
```
**Explanation 0**

Required product is **1/2 * 3/4 * 10/6 = 5/8**
```py
from fractions import Fraction
from functools import reduce

import operator
def product(fracs):
    t =  reduce(operator.mul , fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = [Fraction(*map(int, input().split())) for _ in range(int(input()))]
    result = product(fracs)
    print(*result)
```

