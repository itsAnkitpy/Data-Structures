# Given two integers N1 and N2, find their greatest common divisor.

# The Greatest Common Divisor of any two integers is the largest number that divides both integers. 

# Example 1:
#                 Input:N1 = 9, N2 = 12
                
                
#                 Output:3
#                 Explanation:Factors of 9: 1, 3 and 9
#                 Factors of 12: 1, 2, 3, 4, 6, 12
#                 Common Factors: 1, 3 out of which 3 is the greatest hence it is the GCD.

N1 = 9
N2 = 12

# Solution 1

# gcd = 1
# We start from 1 because the GCD of any two numbers is at least 1, and it cannot be greater than the smaller of the two 
# numbers.
# for i in range(1,min(N1,N2) + 1):
#     if N1%i == 0 and N2%i == 0:
#         gcd = i

# print(gcd)

# Time Complexity: O(min(N1, N2))
# Space Complexity: O(1)

#------------------------------------------------------------------------------------------------------------------------------


# Solution 2

# for i in range(min(N1,N2), 0, -1):
#     if N1%i == 0 and N2%i == 0:
#         print(i)
#         break # Stops after finding the first common divisor
    
# Time Complexity: O(min(N1, N2))
# Space Complexity: O(1)

#------------------------------------------------------------------------------------------------------------------------------

# Solution 3 - Euclidean Algorithm
    # Repeatedly subtract the smaller number from the larger number until one of them becomes 0.
    # Once one of them becomes 0, the other number is the GCD of the original numbers.

# while N1 > 0 and N2 > 0:
#     if N1 > N2:
#         N1 = N1 % N2
#     else:
#         N2 = N2 % N1

# if N1 == 0:
#     print(N2)
# else:
#     print(N1)

# Time Complexity: O(min(N1, N2)) where N1 and N2 is the input number. The algorithm iterates from the minimum of N1 and N2 
# to 1 and each iteration checks whether both the numbers are divisible by the current number (constant time operations).

# Space Complexity: O(1) as the space complexity remains constant and independent of the input size. Only a fixed amount of 
# memory is required to store the integer variable





