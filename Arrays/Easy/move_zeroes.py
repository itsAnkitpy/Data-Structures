# Move all Zeros to the end of the array
# Example 1:

# Input:
#  1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
# Output:
#  1 ,2 ,3 ,4 ,1 ,0 ,0 ,0

arr = [0,1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
n = len(arr)

# Solution 1 - Using temporary array

# temp = []

# # Move all the non zero elements to temporary array
# for i in range(n):
#     if arr[i] != 0:
#         temp.append(arr[i])

# nz = len(temp)

# # Place all the non zero elements from temporary array to the beginning of original array
# for i in range(nz):
#     arr[i] = temp[i]

# # Place all the zeroes in the end of original array
# for i in range(nz, n):
#     arr[i] = 0

# print(arr) 
# output - 1, 2, 3, 4, 1, 0, 0, 0]

# --------------------------------------------------------------------------------------------------------------------

# Solution 2 - Two Pointer approach

l = 0
# Moving non zero elements to left and moving zeroes to right
for i in range(n):
    if arr[i] !=0:
        arr[l], arr[i] = arr[i], arr[l]
        l += 1

print(arr)

# Time complexity - O(n)
# Space complexity - O(1)

