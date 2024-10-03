# Rotate array by K elements - Given an array of integers, rotating array of elements by k elements either left or right.

# Example 1:
# Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
# Output: 6 7 1 2 3 4 5
# Explanation: array is rotated to right by 2 position .

# Example 2:
# Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
# Output: 9 10 11 3 7 8
# Explanation: Array is rotated to right by 3 position.

arr = [1,2,3,4,5,6,7]
k = 2
n = len(arr)

# To rotate to right

# Create a copy of last k elements
# temp = arr[-k:]
# # Shift elements to right
# arr[k:] = arr[:-k]
# # Place the saved elements at the beginning
# arr[:k] = temp

# print(arr) # [6, 7, 1, 2, 3, 4, 5]

# To rotate to left

# Create a copy of first k elements
# temp = arr[:k]
# # Shift elements to left
# arr[:-k] = arr[k:]
# # Place the saved elements at the end
# arr[-k:] = temp

# print(arr) # [3, 4, 5, 6, 7, 1, 2]

#------------------------------------------------------------------------------------------------------------


# Solution 2 - Without using another array

# Rotate the array from right
# arr[:] = arr[-k:] + arr[:-k]

# print(arr)

# Rotate the array from left

# arr[:] = arr[k:] + arr[:k]
# print(arr)
