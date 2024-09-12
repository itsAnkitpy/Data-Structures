import os
os.system('clear')

# Pattern 1

# A 
# B C 
# D E F 
# G H I J 
# K L M N O 

# n = 5
# ascii = 65


# for i in range(n):
#     for j in range(i+1):
#         alphabet = chr(ascii)
#         print(alphabet, end=" ")
#         ascii += 1
#     print()


# ---------------------------------------------------------------------------------------------------------------------

# Pattern 2

# P
# Py
# Pyt
# Pyth
# Pytho
# Python

# str = "Python"
# x = ""

# for i in str:
#     x += i
#     print(x)

    # OR

# for i in range(len(str)):
#     x += str[i]
#     print(x)


# ---------------------------------------------------------------------------------------------------------------------

# Pattern 3

# A 
# A B 
# A B C 
# A B C D 
# A B C D E 

# n = 5
# for i in range(1,n+1):
#     for j in range(65, 65+i):
#         print(chr(j), end=" ")
#     print()


# --------------------------------------------------------------------------------------------------------------------- 

# Pattern 4

# A B C D E 
# A B C D 
# A B C 
# A B 
# A 

# n = 5
# for i in range(n, 0, -1):
#     for j in range(65, 65+i):
#         print(chr(j), end=" ")
#     print()


# ---------------------------------------------------------------------------------------------------------------------

# Pattern 5

# A 
# B B 
# C C C 
# D D D D 
# E E E E E 

# n = 5
# ascii = 65
# for i in range(n):
#     for j in range(i+1):
#         print(chr(ascii), end=" ")
#     ascii += 1

#     print()


# ---------------------------------------------------------------------------------------------------------------------

# Pattern 6

# A 
# B B 
# A A A 
# B B B B 
# A A A A A 

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         if (i%2 == 0):
#             print("A", end=" ")
#         else:
#             print("B", end=" ")
#     print()


# ---------------------------------------------------------------------------------------------------------------------

# Pattern 7

# A B C D E 
#   A B C D 
#     A B C 
#       A B 
#         A 

# n = 5
# for i in range(n):
#     str = 65
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i,n):
#         print(chr(str) , end=" ")
#         str += 1
#     print()

# ---------------------------------------------------------------------------------------------------------------------

# Pattern 8

#     A 
#    B C 
#   D E F 
#  G H I J 
# K L M N O 

# n = 5
# ascii = 65
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(i):
#         print(chr(ascii), end=" ")
#         ascii += 1
#     print()


# ---------------------------------------------------------------------------------------------------------------------

# Pattern 9

#         A 
#       A B C 
#     A B C D E 
#   A B C D E F G 
# A B C D E F G H I 

# n = 5
# for i in range(n):
#     p = 65
#     for j in range(i,n-1):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print(chr(p), end=" ")
#         p += 1
#     for j in range(i):
#         print(chr(p),end=" ")
#         p += 1
#     print()


# ---------------------------------------------------------------------------------------------------------------------

# Pattern 10

#         A 
#       A B A 
#     A B C B A 
#   A B C D C B A 
# A B C D E D C B A 

# n = 5
# for i in range(n):
#     p = 65
#     for j in range(i,n-1):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print(chr(p), end=" ")
#         p += 1
#     p -=2
#     for j in range(i):
#         print(chr(p),end=" ")
#         p -= 1
#     print()

# ---------------------------------------------------------------------------------------------------------------------

# Pattern 11

# C 
# C O 
# C O D 
# C O D E 
# C O D E R 

# s = "CODER"
# for i in range(len(s)):
#     for j in range(i+1):
#         print(s[j],end=" ")
#     print()

# ---------------------------------------------------------------------------------------------------------------------

# Pattern 12

# R 
# R E 
# R E D 
# R E D O 
# R E D O C 

# s = "CODER"
# n = len(s)
# for i in range(n):
#     p = n-1
#     for j in range(i+1):
#         print(s[p],end=" ")
#         p -= 1
#     print()

# ---------------------------------------------------------------------------------------------------------------------

# Pattern 13

# R E D O C 
#   R E D O 
#     R E D 
#       R E 
#         R 

# s = "CODER"
# n = len(s)
# k = n-1
# for i in range(n):
#     p = k
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i,n):
#         print(s[p],end=" ")
#         p -= 1
#     print()
