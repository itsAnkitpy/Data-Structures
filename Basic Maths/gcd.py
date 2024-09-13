# Given two integers N1 and N2, find their greatest common divisor.

# The Greatest Common Divisor of any two integers is the largest number that divides both integers. 

# Example 1:
#                 Input:N1 = 9, N2 = 12
                
                
#                 Output:3
#                 Explanation:Factors of 9: 1, 3 and 9
#                 Factors of 12: 1, 2, 3, 4, 6, 12
#                 Common Factors: 1, 3 out of which 3 is the greatest hence it is the GCD.

N1 = 20
N2 = 15

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

for i in range(min(N1,N2), 0, -1):
    if N1%i == 0 and N2%i == 0:
        print(i)
        break # Stops after finding the first common divisor
    
# Time Complexity: O(min(N1, N2))
# Space Complexity: O(1)

#------------------------------------------------------------------------------------------------------------------------------

# Solution 3





