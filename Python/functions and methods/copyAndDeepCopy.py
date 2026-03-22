# "Copy" in Python is NOT just one thing.
'''
There are 3 fundamentally different behaviors:
✔️ Assignment (no copy) : Assignment copies the reference, not the object
✔️ Shallow copy : Creates a new outer object, but inner elements are still references
✔️ Deep copy : Creates completely independent copy of object AND all nested objects

'''
# 👉 Python stores references, not values

''' 
When working with data, sometimes you want:
• same data → but independent
• changes in one → should NOT affect other

for e.g :
orginal_data = [1,2,3,4]
copy_data = orginal_data

Now if you modify copy_data:
copy_data.append("5")

👉 Suddenly original_data also changed 😬

so to prevent this we use "copy()" also know as Shallow Copy and "deepcopy()" know as Deep Copy.

| Feature              | Assignment | Shallow Copy | Deep Copy |
| -------------------- | ---------- | ------------ | --------- |
| New object           | ❌         | ✔️          | ✔️        |
| Inner objects copied | ❌         | ❌          | ✔️        |
| Safe for nested data | ❌         | ❌          | ✔️        |
| Performance          | Fast       | Medium       | Slower     |

'''

# Defination : Shallow Copy (First Level Solution)
'''
A shallow copy creates a new outer object, 
but keeps references of inner elements.
'''
#Syntax [list]

a = [6,7,8,9]
b = a.copy
# OR
b = list(a)
b = a[:]

# Syntax for Dictionary and Set

b = a.copy()

''' 
Tuple is immutable so .copy() does not support.
You cannot change it, so copying is usually unnecessary.
 '''

# now one more thing if tuple have inner list like : a = ([1,2], [3,4]) : tuple have list inside
# so now if you change innter list it will change  see below example

a = ([1,2,3,4], [5,6,7,8])
print(a) #([1, 2, 3, 4], [5, 6, 7, 8])
a[0][0] = 100

print(a) #([100, 2, 3, 4], [5, 6, 7, 8])

#now why this happend because tuple is immutabal but list is not


c = ([1,2], [3,4])
d = tuple(c)
d[0][0] = 100
print(d) # another way is use tuple() and it works as shallow copy and not deep copy 