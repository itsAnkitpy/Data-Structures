# Remove Duplicates in-place from Sorted Array

# /Example 1:
# Input:
#  arr[1,1,2,2,2,3,3]

# Output:
#  arr[1,2,3,_,_,_,_]

arr = [1,1,2,2,2,3,3]

# Solution 1 - Using the set since it removes the repeating elements automatically

# mp = list(set(arr))

# print(mp)


# Solution 2 - Using two pointers

# i = 0
# for j in range(1, len(arr)):
#     if arr[j] != arr[i]:
#         i += 1
#         arr[i] = arr[j]

# print(arr[:i+1])

# Time Complexity - O(N)
# Space Complexity - O(1)



