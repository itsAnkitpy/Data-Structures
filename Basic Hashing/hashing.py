# Brute force approach with number and string hashing

# given_array = [1,2,1,3,2] 
# count = 0
# num = 3

# for i in range(len(given_array)):
#     if given_array[i] == num:
#         count+=1
# print(count)

# given_string = 'missisippi'
# str = 's'
# cnt = 0
# for i in range(len(given_string)):
#     if given_string[i] == str:
#         cnt += 1
# print(cnt)

# --------------------------------------------------------------------------------------------------------------------

# Character hashing with lowercase string and queries

# Create a hashmap of size 26 - indexing from 0  to 25 representing each lowercase letter a to z
# s = input()

# # Precompute: Count the frequency of each character
# hash_map = [0] * 26
# for char in s:
#     hash_map[ord(char) - ord('a')] += 1

# # Read the number of queries
# q = int(input())

# # Process each query
# for _ in range(q):
#     c = input().strip()
#     # Fetch: Print the frequency of the queried character
#     print(hash_map[ord(c) - ord('a')])


# --------------------------------------------------------------------------------------------------------------------
# Using the array of size 256 with upper and lower case string

# s = input()

# # Precompute: Count the frequency of each character
# hash_map = [0] * 256
# for char in s:
#     hash_map[ord(char)] += 1

# # Read the number of queries
# q = int(input())

# # Process each query
# for _ in range(q):
#     c = input().strip()
#     # Fetch: Print the frequency of the queried character
#     print(hash_map[ord(c)])


# --------------------------------------------------------------------------------------------------------------------

# Hashing - Mapping key and value

# Read the number of elements
n = int(input())

# Read the array of numbers
arr = list(map(int, input().split()))

# Precompute: Count the frequency of each number
mp = {}
for num in arr:
    mp[num] = mp.get(num, 0) + 1

# Uncomment to iterate over the dictionary and print frequencies
# for key, value in mp.items():
#     print(f"{key} -> {value}")

# Read the number of queries
q = int(input())

# Process each query
for _ in range(q):
    number = int(input())
    # Fetch: Print the frequency of the queried number
    print(mp.get(number, 0))

   
