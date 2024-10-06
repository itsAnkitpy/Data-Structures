# Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. 
# Find the number(between 1 to N), that is not present in the given array.

arr = [1,2,4,5]
N = 5

# for i in range(1,N+1):
#     if i not in arr:
#         break
# print(i)

total = N * (N+1) // 2
print(total - sum(arr))