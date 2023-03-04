# 0x09. Python - Everything is object

## TASKS

### 0
What function would you use to print the type of an object?
Write the name of the function in the file, without ().

### 1
How do you get the variable identifier (which is the memory address in the
CPython implementation)?
Write the name of the function in the file, without ().

## Do a and b point to the same object? Answer with Yes or No

### 2
`>>> a = 89
>>> b = 100`

### 3
`>>> a = 89
>>> b = 89`

### 4
`>>> a = 89
>>> b = a`

### 5
`>>> a = 89
>>> b = a + 1`

## What do these 3 lines print?

### 6
`>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)`

### 7
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

### 8
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

### 9
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)

### 10
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)

### 11
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)

### 12
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)

### 13
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

## What does this script print?

### 14
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

### 15
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

### 16
def increment(n):
    n += 1

a = 1
increment(a)
print(a)

### 17
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

### 18
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

### 19
Write a function def copy_list(l): that returns a copy of a list.

The input list can contain any type of objects
Your file should be maximum 3-line long (no documentation needed)
You are not allowed to import any module
