# Given an integer N return the reverse of the given number.

# Note: If a number has trailing zeros, then its reverse will not include them.
# For e.g., reverse of 10400 will be 401 instead of 00401.

n = 10400

rev_num = 0

while n > 0:
    rem = n % 10
    rev_num = rev_num * 10 + rem
    n = n // 10

print(rev_num) 

# Complexity Analysis

# Time Complexity: O(log10N + 1) where N is the input number. The time complexity is determined by the number of digits in
#  the input integer N. In the worst case when N is a multiple of 10 the number of digits in N is log10 N + 1.

# In the while loop we divide N by 10 until it becomes 0 which takes log10N iterations.
# In each iteration of the while loop we perform constant time operations like modulus and division and pushing elements into
#  the vector.

# Space Complexity: O(1) as only a constant amount of additional memory for the reversed number regardless of size of the
# input number.


