# Print 1 to N using Recursion

# Solution 1

# def print1toN(i,N):
#     if i!=N+1:
#         print(i)
#         print1toN(i+1,N)

# print1toN(1,5)


# Solution 2 - Using Backtracking

# def print1toN(N):
#     if N != 0:
#         print1toN(N-1)
#         print(N)

# print1toN(5)