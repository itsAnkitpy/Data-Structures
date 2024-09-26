# Given an array of size N. Find the highest and lowest frequency element.

# Example 1:
# Input: array[] = {10,5,10,15,10,5};
# Output: 10 15
# Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

# def countFreq(arr, n):
#     maxFreq = 0
#     minFreq = n
#     maxElem = 0
#     minElem = 0

#     visited = [False] * n

#     for i in range(n):
#         if visited[i] == True:
#             continue
#         count = 1

#         for j in range(i+1, n):
#             if arr[i] == arr[j]:
#                 visited[j] = True
#                 count += 1 

#         if count > maxFreq:
#             maxElem = arr[i]
#             maxFreq = count
            

#         if count < minFreq:
#             minElem = arr[i]
#             minFreq = count

#     print(maxElem, maxFreq)
#     print(minElem, minFreq)
            

# arr = [10,5,10,15,10,5]
# n = len(arr)
# countFreq(arr, n)

# Time Complexity: O(N*N), where N = size of the array. We are using the nested loop to find the frequency.
# Space Complexity:  O(N), where N = size of the array. It is for the visited array we are using.

#----------------------------------------------------------------------------------------------------------------------------


# Solution 2 - Using Hashmap

# def countFreq(arr,n):
#     mp = {}
#     maxFreq = 0
#     minFreq = n
#     maxElem = 0
#     minElem = 0

#     for i in range(n):
#         if arr[i] in mp:
#             mp[arr[i]] += 1
#         else:
#             mp[arr[i]] = 1

#     for each in mp:
#         if mp[each] > maxFreq:
#             maxElem = each
#             maxFreq = mp[each]

#         if mp[each] < minFreq:
#             minElem = each
#             minFreq = mp[each]

#     print(maxElem, maxFreq)
#     print(minElem, minFreq)

# arr = [10,5,10,15,10,5]
# n = len(arr)
# countFreq(arr, n)