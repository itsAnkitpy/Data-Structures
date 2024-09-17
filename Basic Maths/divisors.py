import math

# Given an integer N, return all divisors of N.

# A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible
# by another integer without any remainder, then that integer is considered a divisor of N. 

# Example 1:
#                 Input:N = 36
               
#                 Output:[1, 2, 3, 4, 6, 9, 12, 18, 36]
                
#                 Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.

N = 36

# Solution 1
# divisors = []

# for i in range(1, N+1):
#     if N % i == 0:
#         divisors += [i]
# print(divisors)

# Time Complexity: O(N) where N is the input number. The algorithm iterates through each number from 1 to n once to check if it is a divisor.

# Space Complexity : O(N) where N is the input number. The algorithm iterates through each number from 1 to n once to check if it is a divisor.

#------------------------------------------------------------------------------------------------------------------------------------------

# Solution 2
# divisors = []

# sqrtN = int(math.sqrt(N))

# for i in range(1, sqrtN+1):
#     if N % i == 0:
#         divisors += [i]

#         if i != N//i:
#             divisors += [N//i]

# print(divisors)

# Time Complexity: O(sqrt(N)) where N is the input number. The algorithm iterates through each number from 1 to the square root
#  of N once to check if it is a divisor.

# Space Complexity : O(2*sqrt(N))where N is the input number. This approach allocates memory for an array to hold all the 
# divisors. The size of this array could go to be 2*(sqrt(N)). 