# **PYTHON DOCUMENTATION**
----
### **Basic Syntax**
**If Else**
```py
if a > b: print("a is greater than b")
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")
```
**Function**
```py
def my_function(**kid): print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
```
**List**
- List Basic Operation: 
```
l.append(arg)       #add an element to the end of the list
l.clear()           #removes all items from the list
l.copy()            #return a copy of the list
l.count(arg)        #returns the count of number of items passed as an arguments
l.extend(arg)       #add all elements of a list to the another list
l.index(arg)        #returns the index of the first matched item/arg
l.pop(pos)          #removes item in pos and returns an element at the given 
l.index(pos,arg)    #returns the index of the first matched item
l.remove(arg)       #removes an first item/arg from the list
l.reverse()         #reverse the order of items in the list
l.sort()            #returns a copy of the list
```
- List Basic Function:
```
reduce(list)        #apply a particular function passed in its argument to all of the list elements stores the intermediate result and only returns the final summation value
sum(list)           #sum up the numbers in the list
ord(string)         #returns an integer representing the unicode code point of the given unicode character (only 1 char)
cmp(list1,list2)    #this function returns 1, if first list is 'greater' than second list
max(list)           #return maximum element of given list
min(list)           #return minimum element of given list
all(list)           #return true if all element in list are true of if list is empty     
any(list)           #return true if any element of the list is true. if list is empty, return false
len(list)           #returns length of the list or size of the list
enumerate(list)     #returns enumerate object of list
accumulate(list)    #apply a particular function passed in its argument to all of the list elements returns a list containing the intermediate results
filter(func, list)  #tests if each element of a list true or not
map(func, list)     #returns a list of the results after applying the given function to each item of a given iterable
lambda()            #This function can have any number of arguments but only one expression, which is evaluated and returned.
```
- How to use `cmp`
```py
list1 = [ 1, 2, 4, 3] 
list2 = [ 1, 2, 5, 8] 
list3 = [ 1, 2, 5, 8, 10] 
list4 = [ 1, 2, 4, 3] 
print("Comparison of list2 with list1 : ", cmp(list2, list1)) 
# Comparison of list2 with list1 :  1
print("Comparison of list2 with list3(larger size) : ", cmp(list2, list3))
# Comparison of list2 with list3(larger size) :  -1
print("Comparison of list4 with list1(equal) : ", cmp(list4, list1))
# Comparison of list4 with list1(equal) :  0
```
- How to use `enumerate`
```python
l1 = ["eat","sleep","repeat"]
print (list(enumerate(l1)))
#output: [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
for count,ele in enumerate(l1,100):
    print (count,ele)
# 100 eat
# 101 sleep
# 102 repeat
```
- How to use `map`, `filter`, `lambda` object
```python
ages = [13, 90, 17, 59, 21, 60, 5] 
print(list(filter(lambda age: age>18, ages)) ) #filter to return all true element
#output: [90, 59, 21, 60]
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
print(list(map(lambda x, y: x + y, numbers1, numbers2)))
#output: [5, 7, 9]
```
- Link References: [geeksforgeeks.org](https://www.geeksforgeeks.org/python-list/)

**Dictionary**
- Dictionary Basic Operations:
```
m.copy()            #returns a shallow copy of the dictionary
m.clear()           #removes all the key-value pairs from m
m.pop()             #removes and returns an element from a dictionary having the given key
m.popitem()           #removes the arbitrary key-value pair from the dictionary and returns it as tuple (hapus key-value sewenang-wenang)
m.get(k)            #returns the value associated with key k in map m
m.str()             #produces a printable string representation of a dictionary
m1.update(m2)       #adds dictionary dict2's key-values pairs to dict
m.setdefault(k)     #set dict[key]=default if key is not already in dict
m.keys()            #returns list of dictionary dict's keys
m.items()           #returns a list of dict's (key, value) tuple pairs
m.has_key(k)        #returns true if key in dictionary dict, false otherwise
m.fromkeys(set,val) #create a new dictionary with keys from set and values set to value
type(m)             #returns the type of the passed variable
cmp(m1,m2)          #compares elements of both dict
m.put(k,v)          #adds new key value pair to map m
m.containsKey(k)    #returns whether there's a key-value pair inmap m with key k
m.containsValue(v)  #returns whether there's a key-value pair in map m with value v
m.putAll(otherMap)  #adds all the key-value pairs of otherMap to m
m.keySet()          #returns the set of keys of m
m.values()          #returns the values of m in some collection (not a set, since they don't have to be unique)
m.entrySet()        #returns the set of key-value pairs in m
m.remove()          #removes the key-value pair with key k from map m
m.size()            #returns the number of key-value pairs in m
m.isEmpty()         #returns whether there are zero pairs in map m
```
- How to show `key` & `values` from dictionary
```python
my_dict = {'one': 1, 'two':2, 'three': 3}
a,b,c = my_dict 
#Output: 'one', 'two', 'three'
a,b,c = my_dict.values() 
#Output: 1, 2, 3
a,b,c = my_dict.items() 
#Output: ('one', 1), ('two', 2), ('three', 3)
keys = my_dict.keys()
#Output: dict_keys(['one', 'two', 'three'])
x = thisdict.get("two")
#Output: 2
my_dict.update({"year": 2020})
my_dict.pop("model")
my_dict.popitem()
```
- How to use `zip()`
```python
fruits = ["Apple", "Pear", "Peach", "Banana"]
prices = (0.35, 0.40, 0.40, 0.28)
fruit_dictionary = dict(zip(fruits, prices))
#Output: {'Apple': 0.35, 'Pear': 0.4, 'Peach': 0.4, 'Banana': 0.28}
```
- How to create `nested dictionary`
```py
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
```
- Link References: [geeksforgeeks.org](https://www.geeksforgeeks.org/python-dictionary/#:~:text=Dictionary%20in%20Python%20is%20an,to%20make%20it%20more%20optimized.)

**Tupple**
- Tupple Basic Operation:
```
t.count(arg)        # returns the number of times a specified value occurs in a tuple       
t.index(arg)        # searches the tuple for a specified value and returns the position of where it was found
```
```python
(name, age, studies) = ("Bob", 19, "CS")
(green, yellow, *red) = ("apple", "banana", "cherry", "strawberry", "raspberry")
print(red)
# Output: ['cherry', 'strawberry', 'raspberry']
(green, *tropic, red) = ("apple", "mango", "papaya", "pineapple", "cherry")
print(tropic)
# Output: ['mango', 'papaya', 'pineapple']
print(("a", "b" , "c") + (1, 2, 3))
# Output: ('a', 'b', 'c', 1, 2, 3)
print(("apple", "banana", "cherry") * 2)
# Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
```

**Sets**
- Sets Basic Operations:
```
s.add(e)            #add element e to the set s
s.update(e)         #add items from another set into the current set
s.remove(e)         #remove element e from the set s
s.discard(e)        #remove element e from the set s
s.pop()             #remove the last element from the set s
s.clear()           #remove all elements in set s
s.contains(e)       #returns whether e is a member of s
s.size()            #returns the number of elements in s
s.isEmpty()         #returns whether there are no elements in s
s.addAll(t)         #add all the elements of set t to set s
s.retainAll(t)      #removes all the elements from s that are not in t
s.union(t)          #returns a new set which contains all the elements of set s and all the elements of set t, and no others
s.intersect(t)      #return a new set which contains all and only those elements in both s and t
s.intersection_update(t)#keep the items that exist in bot set s and set t
s.minus(t)          #returns a new set which contains all and only those elements in s but not in t
s.symmetricMinus(t) #returns a new set which contains all and only those elements in either set s or set t but not both
```
- How to use `union`, `intersection`, `difference`, `symmetricminus`
```py
A = {0, 2, 4, 6, 8}; 
B = {1, 2, 3, 4, 5}; 

print("Union :", A | B) 
print("Intersection :", A & B)  
print("Difference :", A - B) 
print("Symmetric difference :", A ^ B) 
```
**Classes/Objects**
- How to create `parent class` == `Person`
```py
class MyClass: x = 5
print(MyClass.x)
# Output: 5
# The __init__() function is called automatically every time the class is being used to create a new object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self): print("Hello my name is " + self.name)

p1 = Person("John",36)
p1.age = 40
print(p1.name, p1.age)
# Output: John 40
p1.myfunc()
# Output: Hello my name is John
```
- How to create a `child class` == `Student` 
```py
# Parent Class
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc): print(abc.firstname, abc.lastname)

# Child Class
class Student(Person): pass
# OR # to keep inheritence of the parent class
class Student(Person):
  def __init__(self, fname, lname): 
    Person.__init__(self, fname, lname)
# OR # to make the child class inherit all the methods and properties from its parent
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self): print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen")
x.printname()
# Output: Mike Olsen
x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
#Output: 2019
x.welcome()
#Output: Welcome Mike Olsen to the class of 2019
```
**Iterators**
```py
mytuple = iter("apple", "banana", "cherry")
print(next(mytuple), next(mytuple), next(mytuple))
# Output: apple banana cherry

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myiter = iter(MyNumbers())
print(next(myiter), next(myiter), next(myiter), next(myiter), next(myiter))
# Output: 1 2 3 4 5
```
**Try Except**
```py
try: print(x)
except NameError: print("Variable x is not defined")
except: print("Something else went wrong")
#Output: Variable x is not defined
try: print("Hello")
except: print("Something went wrong")
else: print("Nothing went wrong")
#Output: Hello \n Nothing went wrong
if -1 < 0: raise Exception("Sorry, no numbers below zero")
#Output: Sorry, no numbers below zero
if not type("hello") is int: raise TypeError("Only integers are allowed")
#output: Only integers are allowed
```
### **Basic Dependencies**
**Datetime**
```py
import datetime

x = datetime.datetime(2020, 5, 17)
x = datetime.datetime.now() 
print(x.strftime("%A"), x.year)
#Output: Tuesday 2021
```
- `Datetime` legal format codes:
```
DIRECTIVE   EXAMPLE         DESCRIPTION
%a          Wed             Weekday, sort version
%A          Wednesday       Weekday, full version
%w          3               Weekday as a number 0-6, 0 is Sunday
%d          31              Day of month 01-31
%b          Dec             Month name, sort version
%B          December        Month name, full version
%m          12              Month as a number 01-12
%y          18              Year, sort version, without century
%Y          2018            Year, full version
%H          17              Hour 00-23
%I          05              Hour 00-12
%p          PM              AM/PM
%M          41              Minute 00-59
%S          08              Second 00-59
%f          548513          Microsecond 000000-99999
%z          +0100           UTC offset
%Z          CST             Timezone
%j          365             Day number of year 001-366
%U          52              Week number of year Sunday as the first day of week, 00-53
%W          52              Week number of year, Monday as the first day of week 00-53
%c          Mon Dec 31      Local version of date
            17:41:00 2018   
%x          12/31/18        Local version of date
%X          17:41:00        Local version of time
%%          %               A % character
%G          2018            ISO 8601 year
%u          1               ISO 8601 weekday (1-7)
%V          01              ISO 8601 weeknumber (01-53)   
```
**Math**

```py
import math 

min(5, 10, 25)              #returns highest value
max(5, 10, 25)              #returns lowest value
abs(-7.25)                    #returns the absolute (positive) value
pow(4,3)                    #returns the value of x to the power of y (x^y).
math.ceil(1.4)              #mehtod rounds a number upwards to its nearest integer
math.floor(1.4)             #method rounds a number downwards to its nearest integer
math.sqrt(64)              #returns the square root of a number
math.pi                     #return the value of phi(3.14...)
```
**JSON**
```py
import json
#Convert from JSON to Python
x =  '{ "name":"John", "age":30, "city":"New York" }'
y = json.load(x)
# COnvert from Python to JSON
x = { "name": "John", "age": 30, "city": "New York" }
y = json.dumps(x)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
#Output: {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))
```
**RegEx**
```py
import re

txt = "The rain in Spain"
print("Yes!") if re.search("^The.*Spain$", txt) else print("NO")
#Outut: Yes!
txt = "The rain in Spain"
print(re.split("\s", txt))
#Output: ['The', 'rain', 'in', 'Spain']
print(re.split("\s", txt, 1))
#Output: ['The', 'rain in Spain']
print(re.sub("\s", "9", txt))
#Output: The9rain9in9Spain
print(re.sub("\s", "9", txt, 2))
#Output: The9rain9in Spain
print(re.search(r"\bS\w+", txt).span())
#Output: (12, 17)
print(re.search(r"\bS\w+", txt).group())
#Output: Spain
```
**os**
- how to `delete` file
```py
import os

os.remove('demofile.txt')
#or
os.remove("demofile.txt") if os.path.exists("demofile.txt") else print("The file does not exist")
#or
os.rmdir("myfolder")
```
### **Built-in Dependencies**
**NumPy**
```
```
**Pandas**
```
```
**Matplotlib**
```
```
**Scipy**
```
```
**Machine Learning**
```
```
-----
# **HACKERRANK PRACTICE**
### **1. Basic Data Types**
**Input Data**
```python
a = input()
a = int(input())
a = int(raw_input())
a = int(raw_input("input any integer:"))
```

**Basic Calculation**
```python
pembagian = a/b
pembulatan = a//b
habis_dibagi = a%b
```

**List Comprehensions**
```python
x, y, z, n = [int(raw_input()) for _ in range(4)]
array_list = [[xx,yy,zz] for xx in range(x+1) for yy in range(y+1) for zz in range(z+1)]
array_list_final = [array for array in array_list if array[0]+array[1]+array[2] != n]  
```

**Nested List**
```python
student_list = [[input(), float(input())] for _ in range(int(input()))]
unique_score = [score for score in set([list[1] for list in student_list])]
unique_score.sort()
lowest_scores = unique_score[1:2]
    
group_list = [list[0] for score in lowest_scores for list in student_list if list[1] == score]
group_list.sort()
for x in group_list:
    print(x)
```

**list dictionary**
```python
students_data = [raw_input().split() for _ in range(int(raw_input()))]
name_list, scores_list = [line[0], line[1:] for line in students_data]
student_marks = {student_marks[name] = map(float, scores) for scores in scorelist for name in name_list}
```
```python
x = { row.SITE_NAME : row.LOOKUP_TABLE for row in cursor }
```

