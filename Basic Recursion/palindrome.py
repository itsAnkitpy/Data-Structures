# Check if the given String is Palindrome or not

# Example 1:
# Input: Str =  “ABCDCBA”
# Output: Palindrome
# Explanation: String when reversed is the same as string.

given_string = "malayalam"

# Solution 1
# n = len(given_string)

# for i in range(n//2):
#     if given_string[i] != given_string[n-1-i]:
#         print("Not Palindrome")
        
#     else:
#         print("Palindrome")
#     break

# Time complexity: O(n)
# Auxiliary Space: O(1)

#--------------------------------------------------------------------------------------------------------------------------

# Solution 2

# if given_string == given_string[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Time complexity: O(n)
# Auxiliary Space: O(1)

#--------------------------------------------------------------------------------------------------------------------------


# Solution 3 - Using Recursion

# def isPalindrome(i, s):
#     s = s.lower()
#     n = len(s)

#     if i >= n//2:
#         return "Palindrome"
    
#     if s[i] != s[n-1-i]:
#         return "Not Palindrome"
    
#     return isPalindrome(i+1, s)

# print(isPalindrome(0,given_string))

# Time complexity: O(n)
# Auxiliary Space: O(n)
        



