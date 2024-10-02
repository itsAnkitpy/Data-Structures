# Find Second Smallest and Second Largest Element in an array

arr = [8,10,5,7,9]

# We can again sort the arrays and print the results based on our sorting

# arr.sort()
# print(arr)
# print(arr[1])
# print(arr[-2])

# Time Complexity - O(nlogn)
# Space Complexity - O(1)

# Solution without using Sorting

max1 = arr[0]
max2 = 0

for element in arr:
    if element > max1:
        max2 = max1
        max1 = element
    elif element > max2 and element != max1:
        max2 = element

print(max2)

# Time Complexity - O(n)
# Space Complexity - O(1)