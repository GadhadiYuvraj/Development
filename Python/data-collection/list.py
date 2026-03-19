"""
In Python there are 

List is a build-in data type stores set of values
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to 
store collections of data, the other 3 are Tuple, Set, and Dictionary,
all with different qualities and usage.

| Property      | Meaning                      |
| ------------- | ---------------------------- |
| Ordered       | Index-based access           |
| Mutable       | Can modify after creation    |
| Heterogeneous | Different data types allowed |
| Dynamic       | Size can grow/shrink         |
| Indexed       | Starts from 0                |



List : Mutable, Ordered, Indexing, Slicing, duplicate values are allowed.


Lists are created using square brackets:

syntax:

list_name = []
list_name = list()

Example

list_name = [ele-1,ele-2,...,ele-n]
"""

# nums =[1,2,3,4,5]

# print(type(nums))

# print(len(nums))

# print(nums)

# Access elements of list

# Indexing(-/+)
# print(nums[0]) #1
# print(nums[-2]) #4


# Slicing in list in python 
# nums = [1,2,3,4,5]

# print(nums[1:4])
# print(nums[:3])
# print(nums[3:])

# print(nums[-1:-4:-1])


# chars = ['a','b','c','d','e','f','g']
# print(chars)

# # List is Mutable 

# chars[4] = 5  # "e" become 5 cause indexing starts from 0 and at 4th index 'e' was there and then value is changed to 5

# print(chars)

even = [0,2,4,6,8]
odd = [1,3,5,7,9]


# concat
# print(even + odd)

# #repilca

# print (even *2 ) # so now this will replicate even 2 time --> [0, 2, 4, 6, 8, 0, 2, 4, 6, 8]
# print (even *3 )


''' python variable don't store values, They Store refereneces (addresses)   '''