# Check if an Array is Sorted

# Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing /
# Non-decreasing) order or not. If the array is sorted then return True, Else return False.


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_sorted = True

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[i]:
#             is_sorted = False

# print(is_sorted)

# Time complexity - O(N2)
# Space complexity - O(1)

for i in range(1, len(arr)):
    if arr[i] < arr[i-1]:
        is_sorted = False

print(is_sorted)

# Time complexity - O(N)
# Space complexity - O(1)