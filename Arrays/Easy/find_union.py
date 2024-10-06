# Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

# The union of two arrays can be defined as the common and distinct elements in the two arrays.
# NOTE: Elements in the union should be in ascending order.

# Example 1:
# Input:
# n = 5,m = 5.
# arr1[] = {1,2,3,4,5}  
# arr2[] = {2,3,4,4,5}
# Output: {1,2,3,4,5}

arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5]

# # Solution 1 - Using sets 

# output = set(arr1).union(set(arr2))
# union = []

# for num in output:
#     union.append(num)

# print(union)

#----------------------------------------------------------------------------------------------------------------------

# Solution 2 - Using two pointers
i = 0
j = 0
n1 = len(arr1)
n2 = len(arr2)

union = []

while i < n1 and j < n2:
    if arr1[i] <= arr2[j]:
        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    else:
        if len(union) == 0 or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

# If any elements left in arr1
while i < n1:
    if len(union) == 0 or union[-1] != arr1[i]:
        union.append(arr1[i])
    i += 1
# If any elements left in arr2
while j < n2:
    if len(union) == 0 or union[-1] != arr2[j]:
        union.append(arr2[j])
    j += 1

print(union)

# Time Complexity: O(m+n), Because at max i runs for n times and j runs for m times. When there are no common elements 
# in arr1 and arr2 and all elements in arr1, arr2 are distinct. 

# Space Complexity : O(m+n) {If Space of Union ArrayList is considered} 

# O(1) {If Space of union ArrayList is not considered}





