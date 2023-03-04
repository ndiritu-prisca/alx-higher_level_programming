# 0x09. Python - Everything is object

## TASKS

### 0
What function would you use to print the type of an object?
Write the name of the function in the file, without ().

### 1
How do you get the variable identifier (which is the memory address in the
CPython implementation)?
Write the name of the function in the file, without ().

## Do a and b point to the same object? Answer with `Yes` or `No`

### 2
- `>>> a = 89`
- `>>> b = 100`

### 3
- `>>> a = 89`
- `>>> b = 89`

### 4
- `>>> a = 89`
- `>>> b = a`

### 5
- `>>> a = 89`
- `>>> b = a + 1`

## What do these 3 lines print?

### 6
- `>>> s1 = "Best School"`
- `>>> s2 = s1`
- `>>> print(s1 == s2)`

### 7
- `>>> s1 = "Best"`
- `>>> s2 = s1`
- `>>> print(s1 is s2)`

### 8
- `>>> s1 = "Best School"`
- `>>> s2 = "Best School"`
- `>>> print(s1 == s2)`

### 9
- `>>> s1 = "Best School"`
- `>>> s2 = "Best School"`
- `>>> print(s1 is s2)`

### 10
- `>>> l1 = [1, 2, 3]`
- `>>> l2 = [1, 2, 3]`
- `>>> print(l1 == l2)`

### 11
- `>>> l1 = [1, 2, 3]`
- `>>> l2 = [1, 2, 3]`
- `>>> print(l1 is l2)`

### 12
- `>>> l1 = [1, 2, 3]`
- `>>> l2 = l1`
- `>>> print(l1 == l2)`

### 13
- `>>> l1 = [1, 2, 3]`
- `>>> l2 = l1`
- `>>> print(l1 is l2)`

## What does this script print?

### 14
- `l1 = [1, 2, 3]`
- `l2 = l1`
- `l1.append(4)`
- `print(l2)`

### 15
- `l1 = [1, 2, 3]`
- `l2 = l1`
- `l1 = l1 + [4]`
- `print(l2)`

### 16
- `def increment(n):`
-   `n += 1`

- `a = 1`
- `increment(a)`
- `print(a)`

### 17
- `def increment(n):`
-    `n.append(4)`

- `l = [1, 2, 3]`
- `increment(l)`
- `print(l)`

### 18
- `def assign_value(n, v):`
-   `n = v`

- `l1 = [1, 2, 3]`
- `l2 = [4, 5, 6]`
- `assign_value(l1, l2)`
- `print(l1)`

### 19
Write a function `def copy_list(l):` that returns a **copy** of a list.
- The input list can contain any type of objects
- Your file should be maximum 3-line long (no documentation needed)
- You are not allowed to import any module

## Is `a` a tuple? Answer with `Yes` or `No`.

### 20
`a = ()`

### 21
`a = (1, 2)`

### 22
`a = (1)`

### 23
`a = (1, )`

## What does this script print?

### 24
- `a = (1)`
- `b = (1)`
- `a is b`

### 25
- `a = (1, 2)`
- `b = (1, 2)`
- `a is b`

### 26
- `a = ()`
- `b = ()`
- `a is b`

## Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

### 27
- `>>> id(a)`
- `139926795932424`
- `>>> a`
- `[1, 2, 3, 4]`
- `>>> a = a + [5]`
- `>>> id(a)`

### 28
- `>>> a`
- `[1, 2, 3]`
- `>>> id (a)`
- `139926795932424`
- `>>> a += [4]`
- `>>> id(a)`

### 29
Write a function `magic_string()` that returns a string “BestSchool” n
times the number of the iteration:
- Your file should be maximum 4-line long (no documentation needed)
- You are not allowed to import any module

### 30
Write a class `LockedClass` with no class or object attribute, that prevents
the user from dynamically creating new instance attributes, except if the new
instance attribute is called `first_name`.
- You are not allowed to import any module

## Assuming we are using a CPython implementation of Python3 with default options/configuration:

### 31
How many int objects are created by the execution of the first and second line of
the script?
- `a = 1`
- `b = 1`

### 32
- `a = 1024`
- `b = 1024`
- `del a`
- `del b`
- `c = 1024`
- How many int objects are created by the execution of the first line of the script? (`104-line1.txt`)
- How many int objects are created by the execution of the second line of the script (`104-line2.txt`)
- After the execution of line 3, is the int object pointed by `a` deleted? Answer with `Yes` or `No` (`104-line3.txt`)
- After the execution of line 4, is the int object pointed by `b` deleted? Answer with `Yes` or `No` (`104-line4.txt`)
- How many int objects are created by the execution of the last line of the script (`104-line5.txt`)

### 33
`print("I")`
`print("Love")`
`print("Python")`
- Before the execution of line 2 `(print("Love")`), how many int objects have
been created and are still in memory? (`105-line1.txt`)

### 34
- `a = "SCHL"`
- `b = "SCHL"`
- `del a`
- `del b`
- `c = "SCHL"`
- How many string objects are created by the execution of the first line of the script? (`106-line1.txt`)
- How many string objects are created by the execution of the second line of the script (`106-line2.txt`)
- After the execution of line 3, is the string object pointed by `a` deleted? Answer with `Yes` or `No` (`106-line3.txt`)
- After the execution of line 4, is the string object pointed by `b` deleted? Answer with `Yes` or `No` (`106-line4.txt`)
- How many string objects are created by the execution of the last line of the script (`106-line5.txt`)
