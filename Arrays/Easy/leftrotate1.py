# Given an array of N integers, left rotate the array by one place.
# Input:
#  N = 5, array[] = {1,2,3,4,5}
# Output: 2,3,4,5,1


# Solution 1 - Using another array

# arr = [1,2,3,4,5]
# n = len(arr)

# temp = [0] * n

# for i in range(1, n):
#     # Shifting all elements from index 1 to left by one
#     temp[i-1] = arr[i]

# # shifting the first element to end
# temp[n-1] = arr[0]

# print(temp)

# Time Complexity: O(n), as we iterate through the array only once.

# Space Complexity: O(n) as we are using another array of size, same as the given array.

#------------------------------------------------------------------------------------------------------------------------s

# Solution 2 - Without using another array

arr = [1,2,3,4,5]
n = len(arr)
# Storing initial array value in another variable
temp = arr[0]

# Shifting values from index 1 to left by one
for i in range(n-1):
    arr[i] = arr[i+1]

arr[n-1] = temp

print(arr)





