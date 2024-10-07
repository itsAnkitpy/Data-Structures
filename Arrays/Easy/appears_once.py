# Find the number that appears once, and the other numbers twice or more 

# Example 2:
# arr[] = {4,1,2,1,2}
# Result: 4
# Explanation: In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.

arr = [4,4,1,2,1,2,3]

# Solution 1 -  Brute force approach
# for i in range(len(arr)):
#     num = arr[i]
#     count = 0
#     for j in range(len(arr)):
#         if arr[j] == num:
#             count += 1
#     if count == 1:
#         break

# print(num)

#-----------------------------------------------------------------------------------------------------------------------------

# Solution 2 - Using hashmap counting frequency

# hashmap = [0] * len(arr)

# for i in range(len(arr)):
#     hashmap[arr[i]] += 1

# for i in range(len(arr)):
#     if hashmap[arr[i]] == 1:
#         break

# print(arr[i])

#------------------------------------------------------------------------------------------------------------------------

# Solution 3 - using XOR property

xorr = 0
for num in arr:
    xorr ^= num

print(xorr)