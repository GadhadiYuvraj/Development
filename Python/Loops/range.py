# range goes left to right

#range (start, stop, step)
# In the stop value, you always give one number more than the last number you want, because the stop value is not included in the range.
# For example, if you want numbers up to 6, you must write 7.

# The step value tells Python how much to increase or decrease each time.
# For example, a step of 1 increases by 1, and -1 decreases by 1.
# print(list(range(1, 7, 1)))  #output : [1, 2, 3, 4, 5, 6]


# range(start, stop, step)
# start → where counting begins
# stop → stopping point (not included) so if you give number 11 then it will stop at 10
# step → how much the number increases or decreases each time

# ✅ Key idea:
# Positive step (+) → numbers increase
# Negative step (-) → numbers decrease

print(list(range(11))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1,11))) # starts from 1 and goes to 10 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(range(1,11,1))) 
# Start from 1 and stop before 11.
# The stop value (11) is not included, so it prints numbers from 1 to 10.
# Step 1 means the numbers increase by 1 each time.

print(list(range(1,11,2))) 
# Start from 1 and stop before 11.
# Step 2 means the numbers increase by 2 each time.
# So it prints: 1, 3, 5, 7, 9

print((list(range(1,11,3))))# Step 3 means the numbers increase by 2 each time.
# so output is [1, 4, 7, 10] 
# It starts from 1 → 1 + 3 = 4 → 4 + 3 = 7 → 7 + 3 = 10

# Now let's learn about right to left (reverse order) 

print(list(range(11, 0, -1)))

# Start from 11 and decrease by 1 each time because the step is -1.
# The stop value (0) is not included.
# So the output is: [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(list(range(11, 0, -2)))
#output is : [11, 9, 7, 5, 3, 1] 
# Step -2 means the number decreases by 2 each time.


# ✅ Key idea:
# Positive step (+) → numbers increase
# Negative step (-) → numbers decrease

# 11 → 11 - 2 = 9
# 9 → 9 - 2 = 7
# 7 → 7 - 2 = 5
# 5 → 5 - 2 = 3
# 3 → 3 - 2 = 1

