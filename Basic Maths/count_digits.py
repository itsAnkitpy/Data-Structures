import math


# Given an integer N, return the number of digits in N. 

n = 12345

# Solution 1
# count = 0
# while n > 0:
#     count += 1
#     n = n // 10

# print(count)

# The time complexity is O(log10(n))
# Space complexity - O(1)

#--------------------------------------------------------------------------------------------------------------

# Solution 2
# count = int(math.log10(n)) + 1
# print(count)

# Time Complexity: O(1)as simple arithmetic operations in constant time are computed on integers.

# Space Complexity : O(1)as only a constant amount of additional memory for the count variable regardless of size of the input number. 

#---------------------------------------------------------------------------------------------------------------


# Solution 3
# count = 0
# for i in str(n):
#     count += 1
# print(count)

#---------------------------------------------------------------------------------------------------------------------

#Solution 4

# print(len(str(n)))