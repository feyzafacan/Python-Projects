# CS Lecture 2

Created: April 6, 2023 9:31 AM
Class: CS
Type: Lecture
Materials: https://github.com/squillero/computer-sciences/tree/master/Python/units, https://github.com/squillero/computer-sciences/tree/master/Python/units
Reviewed: No

### Numbers and Strings

Variables : 

A variable is a named storage location in a computer program, that refers to a specific value.

```python
cans = 4 # define a value
cans = 7 # assignment changes the value
```

We should write the variable to the left side and the value should be on the right side.

```python
cansPerPack = 6 # int
canVolume = 12.0 # float
myName = "feyza" #string
```

We also can update the value like that:

cansPerPack = cansPerPack + 2

You must define your variable before using it.

```python
taxRate = "Non-taxable" # string
print(taxRate)
print(taxRate + 5)

# This code will get an error. you can not sum int and str.
# Both of them should be str to sum.
```

o Variable names must start with a letter or the underscore ( _ ) character
• Continue with letters (upper or lower case), digits, or the underscore
o You cannot use other symbols (? or %, ...) or spaces
o Separate words with ‘camelCase’ notation
• Use upper case letters to signify word boundaries
o Don’t use ‘reserved’ Python words (see Appendix C, pages A6 and A7)

![Untitled](Untitled.png)

```python
BOTTLE_VOLUME = 2.0  # means it is constant (all capital)
```

Arithmetics:

o Addition +
o Subtraction -
o Multiplication *
o Division /
o Exponent **

7 + 4.0 # Yields the floating value 11.0

7 / 4 yields 1.75

7 // 4 evaluates to 1

remainder = 7 % 4 = 3

![Untitled](Untitled%201.png)

abs(x)  absolute value of x

round(x ,n) rounded to a whole number or to n decimal places

max(…) min(…)

![Untitled](Untitled%202.png)

import math imports the module, and gives access to all functions

```python
balance = total + tax # balance: float
dollars = int(balance) # dollars: integer
```

![Untitled](Untitled%203.png)

Strings:

```python
print("This is a string.", 'So is this.')
length = len("World!") # length is 6
firstName = "Harry"
lastName = "Morgan"
name = firstName + " " + lastName # Harry Morgan
print("my name is:", name)
dashes = "-" * 10 #"------------"
```

o integer + integer → integer addition
o float + float, float + integer → float addition
o string + string → string concatenation
o list + list → list concatenation

o string + integer → error

![Untitled](Untitled%204.png)

▪ Strings are immutable in Python.
▪ You can’t change the value of a character. A TypeError occurs.

![Untitled](Untitled%205.png)

![Untitled](Untitled%206.png)

| FUNCTION | METHOD |
| --- | --- |
| Functions are general and can accept arguments of different types | Methods are specific to a type of object
All strings have a group of methods
All integers have a group of methods |
| Functions are called directly, with a list of parameters
func(param) | Methods are called with the dot-syntax
object.method() |
| Functions may return a result, that may be stored in a variable
result = func(param) | Methods may return a result, that may be stored in a variable
result = obj.method() |

![Untitled](Untitled%207.png)
