# In Python, operators are symbols or keywords used to perform operations on variables and values (operands).
# They are fundamental to programming because they allow you to perform calculations, comparisons, logical decisions, and more.

# Operands → values
# Operators → symbols performing the operation.
# a + b --> so here "a" and "b" is Operends and "+" is Operator

# Types of Operators 
# 1️⃣ Arithmetic Operators (+, -, *, /, //, %, **): Perform mathematical calculations.
# 2️⃣ Assignment Operators (=, +=, -=, *=, /=): Used to assign values to variables, often with shorthand operations.
# 3️⃣ Comparison Operators (==, !=, >, <, >=, <=): Evaluate values to return boolean results.
# 4️⃣ Logical Operators (and, or, not): Used to combine conditional statements.
# 5️⃣ Identity Operators (is, is not): Check if variables refer to the same object.
# 6️⃣ Membership Operators (in, not in): Test for sequence membership.
# 7️⃣ Bitwise Operators (&, |, ^, ~, <<, >>): Manipulate individual bits of integers. 


# 1️⃣ Arithmetic Operators 
# in python arithmetic operator, Division with single slash "/" give float  value result
# while  Division with dubble slash "//" give interger value result
# Division with module "%" Give reminder as result 
# and last Exponentiation with double stars "**" raises a number to the power of another number
# while single star "*" is used for multiplicaiton 
# and pluse "+" is for addition and minus "-" is for subtraction 

num1 = 20
num2 = 4

print("Sum of Num_1 and num_2 is : ", num1 + num2) 
print("Sub of Num_1 and num_2 is : ", num1 - num2) 
print("Mul of Num_1 and num_2 is : ", num1 * num2) 
print("Div of Num_1 and num_2 is : ", num1 / num2) 
print("Floor Div of Num_1 and num_2 is : ", num1 // num2)
print("Reminder after div of Num_1 and num_2 is : ", num1 % num2)  
print("Power of num_1 to num_2 is:", num1 ** num2)

print("\n\n--------------------------\n\n")


# 2️⃣ Assignment Operators (=, +=, -=, *=, /=, **=, )
# Assignment operators are used to assign values to variables.
# They can also update the value of a variable using arithmetic operations.

# a = 5 : -->  "a" is variable -->  "=" is assingment operator --> "5" is assigned value
assing = 2
assing += 10  # :--> here "+="" is "Add and assign" assingment operator 
assing = assing + 10 #:->> this is same as above one but does not use assingment operator 
# and also it is the example of how the assingmet operator works

print (assing)



x = 10
print("Current assigned value of X :", x) #10

x +=  4 # 14
print("Add and assign:", x) #14

x -= 4
print("Add and assign:", x) #10

x /= 2
print("Divide(flote value) and assign:", x) #5.0

x *= 4
print("Multiply and assign:", x) #20

x //= 2
print("Floor divide and assign:", x) #10

x **= 2
print("Exponent and assign:", x) #100

x %= 3
print("Modulus and assign : ", x) #1.0

print("\n\n--------------------------\n\n")



# 3️⃣ Comparison Operators (==, !=, >, <, >=, <=)
# Comparison operators (also called relational operators) are used to compare two values or variables.
# The result of a comparison is always a Boolean value --> True or False










