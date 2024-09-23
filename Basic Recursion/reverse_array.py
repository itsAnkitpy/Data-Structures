# You are given an array. The task is to reverse the array and print it. 

# Example 1:
# Input: N = 5, arr[] = {5,4,3,2,1}
# Output: {1,2,3,4,5}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, 
# the second element occupies the fourth position and so on.

# Solution 1 - Using another empty array and appending the elements in reverse order

# given_array = [5,4,3,2,1]
# original_array = []

# for i in range(len(given_array), 0 ,-1):
#     original_array.append(given_array[i-1])

# print(original_array)

# Solution 2 - Two pointer solution

# arr = [5,4,3,2,1,0]
# l = 0
# r = len(arr) - 1

# while l < r:
#     arr[l], arr[r] = arr[r], arr[l]
#     l += 1
#     r -= 1

# print(arr)

#Solution 3 - Recursive Method

# def reverse_array(arr,l,r):

#     if l >= r:
#         return

#     arr[l], arr[r] = arr[r], arr[l]

#     reverse_array(arr,l+1,r-1)

#     return arr

# arr = [5,4,3,2,1]
# l = 0
# r = len(arr) - 1

# print(reverse_array(arr,l,r))