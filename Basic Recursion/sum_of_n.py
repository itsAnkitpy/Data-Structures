# Given a number ‘N’, find out the sum of the first N natural numbers.

# Example 1:
# Input: N=5
# Output: 15
# Explanation: 1+2+3+4+5=15


# Solution 1 - Parameterized Recursion
# def sumOfN(N, sum):
#     if N < 1:
#         print(sum)
#         return
     
#     sumOfN(N-1, sum+N)


# sumOfN(5,0)


# Solution 2 - Functional Recursion - We are using function to return not directly print

# def sumOfN(N):
#     if N == 0:
#         return 0
    
#     return N + sumOfN(N-1)

# print(sumOfN(5))

