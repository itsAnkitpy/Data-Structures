import math

# Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 
# and itself and the total number of divisors is 2. 

n = 11

# is_prime = True

# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print("It is a prime number")
# else:
#     print("Not Prime")

# Time Complexity: O(N) where N is the input number as we iterate from 1 to N performing constant-time operation for each 
# iteration.

# Space Complexity : O(1) as the space used by the algorithm does not increase with the size of the input.

#------------------------------------------------------------------------------------------------------------------------------------------


# Solution 2
# count = 0
# sqrtN = int(math.sqrt(n))

# for i in range(1, sqrtN+1):
#     if n % i == 0:
#         count += 1

#         if n // i != i:
#             count += 1

# if count == 2:
#     print("Prime")
# else:
#     print("Not Prime")

# Time Complexity: O(sqrt(N))where N is the input number. The loop iterates up to the square root of n performing constant
#  time operations at each step.

# Space Complexity : O(1) as the space complexity remains constant and independent of the input size. Only a fixed amount 
# of memory is required to store the integer variables. 