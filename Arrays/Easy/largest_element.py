# Find the Largest element in an array

arr = [8,10,5,7,9]

# Solution 1 - Sorting the array in descending order and printing first element or last element if sorting in ascending order

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] < arr[j]:
#             arr[i],arr[j] = arr[j],arr[i]

# print(arr)
# # Print the largest element of the array
# print(arr[0])

# We can also use inbuilt functions like sort to sort the array in descending or ascending order

# arr.sort(reverse = True)
# print(arr[0])

# arr.sort()
# n = len(arr)
# print(arr[n-1])

#----------------------------------------------------------------------------------------------------------------------

# Solution 2 - Without Sorting

# max_elem = arr[0]

# for i in range(1,len(arr)):
#     if arr[i] > max_elem:
#         max_elem = arr[i]

# print(max_elem)
                   