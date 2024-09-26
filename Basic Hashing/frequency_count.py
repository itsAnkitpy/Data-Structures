# Count frequency of each element in the array

# Example 1:
# Input: arr[] = {10,5,10,15,10,5};
# Output: 10  3
# 	      5  2
#         15  1
# Explanation: 10 occurs 3 times in the array
# 	      5 occurs 2 times in the array
#               15 occurs 1 time in the array

# def countFreq(arr, n):
#     visited = [False] * n

#     for i in range(n):
#         if visited[i] == True:
#             continue
#         count = 1

#         for j in range(i+1, n):
#             if arr[i] == arr[j]:
#                 visited[j] = True
#                 count += 1
#         print(arr[i], count)

# arr = [10,5,10,15,10,5]
# n = len(arr)
# countFreq(arr, n)

#---------------------------------------------------------------------------------------------------------

# Solution 2 - Using map

def countFreq(arr,n):
    mp = {}
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

    for each in mp:
        print(each, mp[each])

arr = [10,5,10,15,10,5]
n = len(arr)
countFreq(arr, n)