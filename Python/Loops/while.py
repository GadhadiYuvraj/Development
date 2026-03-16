# Syntax

# while condition:
#   Code Block

# The while loop can execute a set of statements as long as a condition is true.

# i = 1

# while i <= 6 :
#     print(i)
#     i += 1

# infinite loop 

# while True:
#     print("Yuvraj")

# ----IMPORT TIME IN PROGRAM---- #

# import time

# while True:
#     time.sleep(2)
#     print("Yuvraj")

# ----FINITE LOOP---- #
# 1 + 2 + 3 + 4 + ... + n

# n = 100
# start = 1
# total = 0

# while(start <= n):
#     total += start
#     print("Current Sum:", total)
#     start += 1

# print("total : ", total)


# 5! =  5*4*3*2*1

num = 5
start = 1
fact = 1

while(start <= num):
    fact *= start
    start += 1

print("Factorial of", num,"! = ", fact )   