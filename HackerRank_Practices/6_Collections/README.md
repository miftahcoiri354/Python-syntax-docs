# **HackerRank-Python**
-----
## **Itertools**

### **1. DefaultDict Tutorial**
The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
**For example:**
```
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
```
This prints:
```
('python', ['awesome', 'language'])
('something-else', ['not relevant'])
```
In this challenge, you will be given **2** integers, **n** and **m**. There are **n** words, which might repeat, in word group **A**. There are **m** words belonging to word group **B**. For each **m** words, check whether the word has appeared in group  or not. Print the indices of each occurrence of **m** in group **A**. If it does not appear, print **-1**.

**Constraints**
- **1<=n<=10000**
- **1<=m<=100**
- **1<=length of each word in the input <= 100**
  
**Input Format**
The first line contains integers, **n** and **m** separated by a space.
The next **n** lines contains the words belonging to group **A**.
The next **m** lines contains the words belonging to group **B**.

**Output Format**
Output **m** lines.
The **ith** line should contain the **1**-indexed positions of the occurrences of the **ith** word separated by spaces.

**Sample Input**
````
5 2
a
a
b
a
b
a
b
````
**Sample Output**
```
1 2 4
3 5
```
**Explanation**
'**a**' appeared **3** times in positions **1**, **2** and **3**.
'**b**' appeared **2** times in positions **3** and **5**.
In the sample problem, if '**c**' also appeared in word group **B**, you would print **-1**.

```py
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(lambda: -1)
for i in range(1, n+1): word = input(); d[word] = d[word] + ' ' + str(i) if word in d else str(i)
for _ in range(m): print(d[input()])
```
### **2. Collections.namedtuple()**
Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

**Example**
**Code 01**
```
>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11
```
**Code 02**
```
>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y
```
**Task**
Dr. John Wesley has a spreadsheet containing a list of student's **ID's**, **marks**, **class** and **name**.

Your task is to help Dr. Wesley calculate the average marks of the students.

**Average=Sum of all Marks/Total Students**

**Note:**
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

**Input Format**
The first line contains an integer **N**, the total number of students.
The second line contains the names of the columns in any order.
The next **N** lines contains the **marks**, **IDs**, **name** and **class**, under their respective column names.

**Constraints**
- **0<N<=100**

**Output Format**
Print the average marks of the list corrected to 2 decimal places.

**Sample Input**
**TESTCASE 01**
```
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
```
**TESTCASE 02**
```
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
```
**Sample Output**
**TESTCASE 01**
```
78.00
```
**TESTCASE 02**
```
81.00
```
**Explanation**
**TESTCASE 01**
Average = **(97+50+91+72+80)/5**
Can you solve this challenge in 4 lines of code or less?
**NOTE:** There is no penalty for solutions that are correct but have more than 4 lines.
```py
import collections, statistics
print('%.2f' % statistics.mean(next((int(student(*row).MARKS) for row in (input().split() for i in range(size))) for size, student in [[int(input()), collections.namedtuple('Student', input())]])))
```

### **3. Collections.OrderedDict()**
An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

**Example**
**Code**
```
>>> from collections import OrderedDict
>>> 
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>> 
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>> 
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>> 
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
```
**Task**
You are the manager of a supermarket.
You have a list of **N** items together with their prices that consumers bought on a particular day.
Your task is to print each *item_name* and *net_price* in order of its first occurrence.

*item_name* = Name of the item.
*net_price* = Quantity of the item sold multiplied by the price of each item.

**Input Format**
The first line contains the number of items, **N**.
The next **N** lines contains the item's name and price, separated by a space.

**Constraints**
- **0<N<=100**

**Output Format**
Print the item_name and net_price in order of its first occurrence.

**Sample Input**
```
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
```
**Sample Output**
```
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
```
**Explanation**
BANANA FRIES: Quantity bought: **1**, Price: **12**
Net Price: **12**
POTATO CHIPS: Quantity bought: **2**, Price: **30**
Net Price: **60**
APPLE JUICE: Quantity bought: **2**, Price: **10** 
Net Price: **20**
CANDY: Quantity bought: **4**, Price: **5** 
Net Price: **20**

```py
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)
```

### **4. Word Order**
You are given **n** words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

**Note:** Each input line ends with a "**\n**" character.

**Constraints:**
- **1<=n<=10^5**
The sum of the lengths of all the words do not exceed **10^6**
All the words are composed of lowercase English letters only.

**Input Format**
The first line contains the integer, **n**.
The next  lines each contain a word.

**Output Format**
Output **2** lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

**Sample Input**
```
4
bcdef
abcdefg
bcde
bcdef
```
**Sample Output**
```
3
2 1 1
```
**Explanation**
There are **3** distinct words. Here, "**bcdef**" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "**bcdef**", "**abcdefg**" and "**bcde**" which corresponds to the output.
```py
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
```
### **5. Collections.deque()**
A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same **O(1)** performance in either direction.

Click on the link to learn more about **deque() methods**.
Click on the link to learn more about various approaches to working with deques: **Deque Recipes**.

**Example**
**Code**
```
>>> from collections import deque
>>> d = deque()
>>> d.append(1)
>>> print d
deque([1])
>>> d.appendleft(2)
>>> print d
deque([2, 1])
>>> d.clear()
>>> print d
deque([])
>>> d.extend('1')
>>> print d
deque(['1'])
>>> d.extendleft('234')
>>> print d
deque(['4', '3', '2', '1'])
>>> d.count('1')
1
>>> d.pop()
'1'
>>> print d
deque(['4', '3', '2'])
>>> d.popleft()
'4'
>>> print d
deque(['3', '2'])
>>> d.extend('7896')
>>> print d
deque(['3', '2', '7', '8', '9', '6'])
>>> d.remove('2')
>>> print d
deque(['3', '7', '8', '9', '6'])
>>> d.reverse()
>>> print d
deque(['6', '9', '8', '7', '3'])
>>> d.rotate(3)
>>> print d
deque(['8', '7', '3', '6', '9'])
```
**Task**
Perform append, pop, popleft and appendleft methods on an empty deque **d**.

**Input Format**
The first line contains an integer **B**, the number of operations. The next **N** lines contains the space separated names of methods and their values.

**Constraints**
- **0<N<=100**

**Output Format**

Print the space separated elements of deque **d**.

**Sample Input**
```
6
append 1
append 2
append 3
appendleft 4
pop
popleft
```
**Sample Output**
```
1 2
```
```py
from collections import deque
d = deque()
for _ in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
print(*[item for item in d])
```
### **6. Company Logo**
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

- Print the three most common characters along with their occurrence count.
- Sort in descending order of occurrence count.
- If the occurrence count is the same, sort the characters in alphabetical order.

For example, according to the conditions described above, **GOOGLE**
 would have it's logo with the letters **G,O,E**.

**Input Format**
A single line of input containing the string **S**.

**Constraints**
- **3<len(S)<=10^4**

**Output Format**
Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

**Sample Input 0**
```
aabbbccde
```
**Sample Output 0**
```
b 3
a 2
c 2
```
**Explanation 0**
**aabbbccde**
Here, b occurs **3** times. It is printed first.
Both a and c occur **2** times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

**Note:** The string **S** has at least **3** distinct characters.

```py
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict): pass

[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
```
### **7. Piling Up!**
There is a horizontal row of **n** cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if **cubei** is on top of **cubej** then **sideLengthj > sideLengthi**.

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

**Input Format**
The first line contains a single integer **T**, the number of test cases.
For each test case, there are **2** lines.
The first line of each test case contains **n**, the number of cubes.
The second line contains **n** space separated integers, denoting the sideLengths of each cube in that order.

**Constraints**
- **1<=T<=5**
- **1<=n<=10^5**
- **1<=sideLength<2^31**

**Output Format**
For each test case, output a single line containing either "Yes" or "No" without the quotes.

**Sample Input**
```
2
6
4 3 2 1 3 4
3
1 3 2
```
**Sample Output**
```
Yes
No
```
**Explanation**
In the first test case, pick in this order: **left** - **4**, **right** - **4**, **left** - **3**, **right** - **3**, **left** - **3**, **right** - **1**.
In the second test case, no order gives an appropriate arrangement of vertical cubes. **3** will always come after either **1** or **2**.
```py
for t in range(int(input())):
    input()
    lst = list(map(int, input().split()))
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]: i += 1
    while i < l - 1 and lst[i] <= lst[i+1]: i += 1
    print ("Yes") if i == l - 1 else print("No")z
```
