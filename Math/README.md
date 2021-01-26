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
print '%d°' % round(math.degrees(math.atan2(AB,BC)),0)
```

### **3. Mod Divmod**
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
print('{0}\n{1}\n({0}, {1})'.format(*divmod(177, 10)))
```
