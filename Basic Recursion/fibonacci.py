# Print Fibonacci Series up to Nth term

# Example 1:
# Input: N = 5
# Output: 0 1 1 2 3 5
# Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing) 

# Solution 1

# fibonacci = [0,1]
# N = 5
# for i in range(2, N+1):
#     c = fibonacci[i-1] + fibonacci[i-2]
#     fibonacci.append(c)

# print(fibonacci[N])

# Solution 2 - Using Recursion

# def fibonacci(N):
#     if N <=1:
#         return N
#     else:
#         return fibonacci(N-1) + fibonacci(N-2)

# N = 5
# print(fibonacci(N))