# Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. 
# Find the number(between 1 to N), that is not present in the given array.

arr = [1,2,4,5]
N = 5

# Solution 1 - Using brute force to see missing number from 1 to N
# for i in range(1,N+1):
#     if i not in arr:
#         break
# print(i)

#----------------------------------------------------------------------------------------------------------------------

# Solution 2 - Using hashmap and saving element frequencies

# hashmap = [0] * (N+1)
# for i in range(len(arr)):
#     hashmap[arr[i]] += 1
# print(hashmap)

# for i in range(1,N+1):
#     if hashmap[i] == 0:
#         break
# print(i)

#------------------------------------------------------------------------------------------------------------------------

# Solution 3 - Using summation and substraction

# total = N * (N+1) // 2
# print(total - sum(arr))

# ---------------------------------------------------------------------------------------------------------------------------

# Solution 4 - Using XOR

xor1 = 0
xor2 = 0

for i in range(N - 1):
    xor2 = xor2 ^ arr[i]  # XOR of array elements
    xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]
    
xor1 = xor1 ^ N  # XOR up to [1...N]

print(xor1 ^ xor2 )  