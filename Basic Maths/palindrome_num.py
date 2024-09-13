# Given an integer N, return true if it is a palindrome else return false

n = 4554

# We make a copy of original number because later we will be performing operations on n which will change its value
n_copy = n
rev_num = 0

while n > 0:
    rem = n % 10
    rev_num = (rev_num * 10) + rem
    n = n // 10

if (rev_num == n_copy):
    print("Palindrome")
else:
    print("Not a palindrome")

# Time Complexity: O(log10N + 1) 
# Space Complexity: O(1)