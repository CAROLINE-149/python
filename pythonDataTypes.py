"""
DATA TYPES
Text : str(string)
Numbers : int, float, complex
Boolean : bool - Is a data type that can have only two possible values(true, False).Are used in decision-making and comparisons.
Sequence : list, tuple, range
Mapping: dict(dictionary)
Set: set,frozenset
Binary: bytes, byterray,memoryview
None: NoneType

"""
"""
x= 5<3
print(type(x)) #bool

numbers = frozenset([1,2,3,4,5]) 
print(type(numbers)) #frozenset

x= 1j
print(type(x)) #complex- Are written with a j as the imaginary part

x=["apple","banana","orange"]
print(type(x)) #list

x={"apple","banana","orange"}
print(type(x)) #set

x=("apple","banana","orange")
print(type(x)) #tuple

x={"name": "John", "age": 36}
print(type(x)) #dict
"""
"""
PYTHON NUMBERS
-Int
-float
-complex

Random Number
-Python has a built-in module called random that can be used to make random numbers.
"""
#example random numbers
#import random
#print(random.randrange(23,70))

"""
PYTHON CASTING
-It means converting a value from one data type to another
"""

#PYTHON STRINGS
#Multi-line string
a= """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

"""
String are Arrays
Strings in python are arrays of unicode characters
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets are used to access elements of the string
"""
#example
x="Caroline Doe"
print(x[11])