# Given an integer N, return true it is an Armstrong number otherwise return false.

# An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of 
# digits. 
                
n = 153

# Solution 1
# total = 0

# for each in str(n):
#     total += int(each) ** len(str(n))

# if total == n:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong number")


# Solution 2
# total = 0
# temp = n
# while temp > 0:
#     digit = temp % 10
#     total += digit ** len(str(n))
#     temp //= 10

# if total == n:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong number")

					
            

