# **HackerRank-Python**
-----
## **Numpy**

### **1. Shape and Reshape**
**shape**
The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.

**(a). Using shape to get array dimensions**
```py
import numpy

my__1D_array = numpy.array([1, 2, 3, 4, 5])
print my_1D_array.shape     #(5,) -> 1 row and 5 columns

my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns 
```
**(b). Using shape to change array dimensions**
```py
import numpy

change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print change_array      

#Output
[[1 2]
[3 4]
[5 6]]
```
**reshape**
The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.
```py
import numpy

my_array = numpy.array([1,2,3,4,5,6])
print numpy.reshape(my_array,(3,2))

#Output
[[1 2]
[3 4]
[5 6]]
```
**Task**
You are given a space separated list of nine integers. Your task is to convert this list into a **3**X**3** NumPy array.

**Input Format**
A single line of input containing **9** space separated integers.

**Output Format**
Print the **3**X**3** NumPy array.

**Sample Input**
```
1 2 3 4 5 6 7 8 9
```
**Sample Output**
```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```
```py
import numpy as np
print(np.array(input().split(),int).reshape(3,3))
```

### **2. Transpose and Flatten**
**Transpose**
We can generate the transposition of an array using the tool `numpy.transpose`.
It will not affect the original array, but it will create a new array.
```py
import numpy
my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print numpy.transpose(my_array)
#Output
[[1 4]
 [2 5]
 [3 6]]
```
**Flatten**
The tool flatten creates a copy of the input array flattened to one dimension.
```py
import numpy
my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print my_array.flatten()
#Output
[1 2 3 4 5 6]
```
**Task**
You are given a X integer array matrix with space separated elements ( = rows and  = columns).
Your task is to print the transpose and flatten results.

**Input Format**
The first line contains the space separated values of **N** and **M**.
The next **N** lines contains the space separated elements of **M** columns.

**Output Format**
First, print the transpose array and then print the flatten.

**Sample Input**
```
2 2
1 2
3 4
```
**Sample Output**
```
[[1 3]
 [2 4]]
[1 2 3 4]
```
```py
import numpy

n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())
```
### **3. Convatenate**
**Concatenate**
Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:

```py
import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))    

#Output
[1 2 3 4 5 6 7 8 9]
```
If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.
```py
import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]] 
```   
**Task**
You are given two integer arrays of size **N**X**P** and **M**X**P** ( **N** & **M** are rows, and **P** is the column). Your task is to concatenate the arrays along axis **0**.

**Input Format**
The first line contains space separated integers **N**, **M** and **P**.
The next **N** lines contains the space separated elements of the **P** columns.
After that, the next **M** lines contains the space separated elements of the **P** columns.

**Output Format**
Print the concatenated array of size **(N+M)** X **P**.

**Sample Input**
```
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
```
**Sample Output**
```
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
```
```py
import numpy as np
a, b, c = map(int,input().split())
arrA = np.array([input().split() for _ in range(a)],int)
arrB = np.array([input().split() for _ in range(b)],int)
print(np.concatenate((arrA, arrB), axis = 0))
```
### **4. Zeros and Ones**
**zeros**
The zeros tool returns a new array with a given shape and type filled with 's.
```py
import numpy

print numpy.zeros((1,2))                    #Default type is float
#Output : [[ 0.  0.]] 

print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
#Output : [[0 0]]
```
**ones**
The ones tool returns a new array with a given shape and type filled with 's.
```py
import numpy

print numpy.ones((1,2))                    #Default type is float
#Output : [[ 1.  1.]] 

print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
#Output : [[1 1]]   
```
**Task**
You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools `numpy.zeros` and `numpy.ones`.

**Input Format**
A single line containing the space-separated integers.

**Constraints**
- **1<=each integer<=3**

**Output Format**
First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.

**Sample Input 0**
```
3 3 3
```
**Sample Output 0**
```
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
```
**Explanation 0**
Print the array built using `numpy.zeros` and `numpy.ones` tools and you get the result as shown.
```py
import numpy

nums = tuple(map(int, input().split()))
print (numpy.zeros(nums, dtype = numpy.int))
print (numpy.ones(nums, dtype = numpy.int))
```
### **5. Eye and Identity**
**identity**
The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as **1** and the rest as **0**. The default type of elements is float.
```py
import numpy
print numpy.identity(3) #3 is for  dimension 3 X 3

#Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
```
**eye**
The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter **k**. A positive **k** is for the upper diagonal, a negative **k** is for the lower, and a **0** **k**  (default) is for the main diagonal.
```py
import numpy
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
[[ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]

print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.
```
**Task**
Your task is to print an array of size **N**X**M** with its main diagonal elements as **1**'s and **0**'s everywhere else.

**Note**
In order to get alignment correct, please insert the line **numpy.set_printoptions(legacy='1.13')** below the numpy import.

**Input Format**
A single line containing the space separated values of **N** and **M**.
**N** denotes the rows.
**M** denotes the columns.

**Output Format**
Print the desired X array.

**Sample Input**
```
3 3
```
**Sample Output**
```
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
```
```py
import numpy

print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))
```
### **6. Array Mathematics**
Basic mathematical functions operate element-wise on arrays. They are available both as operator overloads and as functions in the NumPy module.
```py
import numpy

a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print a + b                     #[  6.   8.  10.  12.]
print numpy.add(a, b)           #[  6.   8.  10.  12.]

print a - b                     #[-4. -4. -4. -4.]
print numpy.subtract(a, b)      #[-4. -4. -4. -4.]

print a * b                     #[  5.  12.  21.  32.]
print numpy.multiply(a, b)      #[  5.  12.  21.  32.]

print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]

print a % b                     #[ 1.  2.  3.  4.]
print numpy.mod(a, b)           #[ 1.  2.  3.  4.]

print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
```
**Task**
You are given two integer arrays, **A** and **B** of dimensions **N**X**M**.
Your task is to perform the following operations:
1. Add (**A** + **B**)
2. Subtract (**A** - **B**)
3. Multiply (**A** * **B**)
4. Integer Division (**A** / **B**)
5. Mod (**A** % **B**)
6. Power (**A** ** **B**)

**Note**
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

**Input Format**
The first line contains two space separated integers, **N** and **M**.
The next **N** lines contains **M** space separated integers of array **A**.
The following **N** lines contains **M** space separated integers of array **B**.

**Output Format**
Print the result of each operation in the given order under **Task**.

**Sample Input**
```
1 4
1 2 3 4
5 6 7 8
```
**Sample Output**
```
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 
```
Use // for division in Python 3.
```py
import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')
```
### **7. Floor, Ceil, and Rint**
**floor**
The tool floor returns the floor of the input element-wise.
The floor of **x** is the largest integer **i** where **i<=x**.
```
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
```
**ceil**
The tool ceil returns the ceiling of the input element-wise.
The ceiling of **x** is the smallest integer **i** where **i<=x**.
```py
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
```
**rint**
The rint tool rounds to the nearest integer of input element-wise.
```py
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
```
**Task**
You are given a 1-D array, **A**. Your task is to print the **floor**, **ceil** and **rint** of all the elements of **A**.

**Note**
In order to get the correct output format, add the line **numpy.set_printoptions(legacy='1.13')** below the numpy import.

**Input Format**
A single line of input containing the space separated elements of array **A**.

**Output Format**
On the first line, print the **floor** of A.
On the second line, print the **ceil** of A.
On the third line, print the **rint** of A.

**Sample Input**
```
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
```
**Sample Output**
```
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
```
```py
import numpy

numpy.set_printoptions(sign=' ')

a = numpy.array(input().split(),float)

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
```
### **8. Sum and Prod**
**sum**
The sum tool returns the sum of array elements over a given axis.
```
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])
print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10
```
By default, the axis value is None. Therefore, it performs a sum over all the dimensions of the input array.

**prod**
The prod tool returns the product of array elements over a given axis.
```
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])
print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24
```
By default, the axis value is None. Therefore, it performs the product over all the dimensions of the input array.

**Task**
You are given a 2-D array with dimensions **N**X**M**.
Your task is to perform the **sum** tool over axis **0** and then find the **product** of that result.

**Input Format**
The first line of input contains space separated values of **N** and **M**.
The next **N** lines contains **M** space separated integers.

**Output Format**
Compute the sum along axis **0**. Then, print the product of that sum.

**Sample Input**
```
2 2
1 2
3 4
```
**Sample Output**
```
24
```
**Explanation**

The sum along axis **0** = [**46**]
The product of this sum = **24**
```py
import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))
```
### **9. Min and Max**
**min**
The tool min returns the minimum value along a given axis.
```py
import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])
print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0
```
By default, the axis value is `None`. Therefore, it finds the minimum over all the dimensions of the input array.

**max**
The tool max returns the maximum value along a given axis.
```py
import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7
```
By default, the axis value is `None`. Therefore, it finds the maximum over all the dimensions of the input array.

**Task**
You are given a 2-D array with dimensions **N**X**M**.
Your task is to perform the min function over axis  and then find the max of that.

**Input Format**
The first line of input contains the space separated values of **N** and **M**.
The next **B** lines contains **M** space separated integers.

**Output Format**
Compute the min along axis **1** and then print the max of that result.

**Sample Input**
```
4 2
2 5
3 7
1 3
4 0
```
**Sample Output**
```
3
```
**Explanation**
The min along axis **1** = **[2,3,1,0]**
The max of **[2,3,1,0]** = **3**
```py
import numpy as np

print(np.max(np.min(np.array([input().split() for _ in range(int(input().split()[0]))],int),axis=1)))
```
### **10. Mean, Var, and Std**
**mean**
The mean tool computes the arithmetic mean along the specified axis.
```
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
print numpy.mean(my_array, axis = None)     #Output : 2.5
print numpy.mean(my_array)                  #Output : 2.5
```
By default, the axis is None. Therefore, it computes the mean of the flattened array.

**var**
The var tool computes the arithmetic variance along the specified axis.
```py
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
print numpy.var(my_array, axis = None)      #Output : 1.25
print numpy.var(my_array)                   #Output : 1.25
```
By default, the axis is None. Therefore, it computes the variance of the flattened array.

**std**
The std tool computes the arithmetic standard deviation along the specified axis.
```py
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
print numpy.std(my_array, axis = None)      #Output : 1.11803398875
print numpy.std(my_array)                   #Output : 1.11803398875
```
By default, the axis is **None**. Therefore, it computes the standard deviation of the flattened array.

**Task**
You are given a 2-D array of size **N**X**M**.
Your task is to find:
1. The mean along axis **1**
2. The var along axis **0**
3. The std along axis **None**

**Input Format**
The first line contains the space separated values of **N** and **M**.
The next **N** lines contains **M** space separated integers.

**Output Format**
First, print the mean.
Second, print the var.
Third, print the std.

**Sample Input**
```
2 2
1 2
3 4
```
**Sample Output**
```
[ 1.5  3.5]
[ 1.  1.]
1.11803398875
```
```py
import numpy

nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []
for i in range(n):
    m = list(map(int, input().split()))
    arr.append(m)
arr = numpy.array(arr)

mean = numpy.mean(arr, axis = 1)
var = numpy.var(arr, axis = 0)
std = numpy.std(arr)

print(mean)
print(var)

rnd = numpy.around(std, 11)
print(rnd)
```
### **11. Dot and Cross**
**dot**
The dot tool returns the dot product of two arrays.
```py
import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11
```
**cross**
The cross tool returns the cross product of two arrays.
```py
import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2
```
**Task**
You are given two arrays **A** and **B**. Both have dimensions of **N**X**N**. 
Your task is to compute their matrix product.

**Input Format**
The first line contains the integer **N**.
The next **N** lines contains **N** space separated integers of array **A**.
The following **N** lines contains **N** space separated integers of array **B**.

**Output Format**
Print the matrix multiplication of **A** and **B**.

**Sample Input**
```
2
1 2
3 4
1 2
3 4
```
**Sample Output**
```
[[ 7 10]
 [15 22]]
```
```py
import numpy
n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))
```
### **12. Inner and Outer**

**inner**
The inner tool returns the inner product of two arrays.
```py
import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.inner(A, B)     #Output : 4
```
**outer**
The outer tool returns the outer product of two arrays.
```py
import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]
```
**Task**
You are given two arrays: **A** and **B**.
Your task is to compute their inner and outer product.

**Input Format**
The first line contains the space separated elements of array **A**.
The second line contains the space separated elements of array **B**.

**Output Format**
First, print the inner product.
Second, print the outer product.

**Sample Input**
```
0 1
2 3
```
**Sample Output**
```
3
[[0 0]
 [2 3]]
```
```py
import numpy as np
A = np.array(input().split(), int)
B = np.array(input().split(), int)
print(np.inner(A,B), np.outer(A,B), sep='\n')
```
### **13. Polynomials**
**poly**
The poly tool returns the coefficients of a polynomial with the given sequence of roots.
```
print numpy.poly([-1, 1, 1, 10])        #Output : [  1 -11   9  11 -10]
```
**roots**
The roots tool returns the roots of a polynomial with the given coefficients.
```
print numpy.roots([1, 0, -1])           #Output : [-1.  1.]
```
**polyint**
The polyint tool returns an antiderivative (indefinite integral) of a polynomial.
```
print numpy.polyint([1, 1, 1])          #Output : [ 0.33333333  0.5         1.          0.        ]
```
**polyder**
The polyder tool returns the derivative of the specified order of a polynomial.
```
print numpy.polyder([1, 1, 1, 1])       #Output : [3 2 1]
```
**polyval**
The polyval tool evaluates the polynomial at specific value.
```
print numpy.polyval([1, -2, 0, 2], 4)   #Output : 34
```
**polyfit**
The polyfit tool fits a polynomial of a specified order to a set of data using a least-squares approach.
```
print numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)
#Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]
```
The functions polyadd, polysub, polymul, and polydiv also handle proper addition, subtraction, multiplication, and division of polynomial coefficients, respectively.

**Task**
You are given the coefficients of a polynomial **P**.
Your task is to find the value of **P** at point **x**.

**Input Format**
The first line contains the space separated value of the coefficients in **P**.
The second line contains the value of **x**.

**Output Format**
Print the desired value.

**Sample Input**
```
1.1 2 3
0
```
**Sample Output**
```
3.0
```
```py
import numpy

print(__import__('numpy').polyval(list(map(float,input().split())),float(input())))
```
### **14. Linear Algebra**
The NumPy module also comes with a number of built-in routines for linear algebra calculations. These can be found in the sub-module linalg.

**linalg.det**
The linalg.det tool computes the determinant of an array.
```py
print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0
```
**linalg.eig**
The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
```py
vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print vals                                      #Output : [ 3. -1.]
print vecs                                      #Output : [[ 0.70710678 -0.70710678]
                                                #          [ 0.70710678  0.70710678]]
```
**linalg.inv**
The linalg.inv tool computes the (multiplicative) inverse of a matrix.
```py
print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
                                                #          [ 0.66666667 -0.33333333]]
```
Other routines can be found here

**Task**
You are given a square matrix **A** with dimensions **N**X**N**. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

**Input Format**
The first line contains the integer **N**.
The next **N** lines contains the **N** space separated elements of array **A**.

**Output Format**
Print the determinant of **A**.

**Sample Input**
```
2
1.1 1.1
1.1 1.1
```
**Sample Output**
```
0.0
```
```py
import numpy

print(round(numpy.linalg.det(numpy.array([input().split() for _ in range(int(input()))],float)),2))
```

### **15. Array**
The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.
To use the NumPy module, we need to import it using:
```py
import numpy
```
**Arrays**
A NumPy array is a grid of values. They are similar to lists, except that every element of an array must be the same type.
```py
import numpy

a = numpy.array([1,2,3,4,5])
print a[1]          #2

b = numpy.array([1,2,3,4,5],float)
print b[1]          #2.0
```
In the above example, numpy.array() is used to convert a list into a NumPy array. The second argument (float) can be used to set the type of array elements.

**Task**
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.

**Input Format**
A single line of input containing space separated numbers.

**Output Format**
Print the reverse NumPy array with type float.

**Sample Input**
```
1 2 3 4 -8 -10
```
**Sample Output**
```
[-10.  -8.   4.   3.   2.   1.]
```
```py
import numpy

def arrays(arr):
   #revrser array first, convert to float array with numpy
   return(numpy.array(arr[::-1], float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
```