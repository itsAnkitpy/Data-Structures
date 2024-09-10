# Pattern 1

# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

# n = 5
# for i in range(n):
#     for j in range(n):
#         print("* ", end="")
#     print()

# ---------------------------------------------------------------------------------------------------------------------

# Pattern 2

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# n = 5                                                           
# for i in range(n):
#     for j in range(i+1):
#         print("* ", end="")
#     print()

# ---------------------------------------------------------------------------------------------------------------------

# Pattern 3

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# n = 5

# for i in range(n,0,-1):
#     for j in range(0,i):
#         print("* ", end="")
#     print()

# ---------------------------------------------------------------------------------------------------------------------

# Pattern 4

#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

# n = 5

# for i in range(n):
#     for j in range(i,n-1):
#         print("  ", end="") # Two spaces for each "unit" of alignment
#     for j in range(i+1):
#         print("* ", end="") # Space between asterisks
#     print()

# ---------------------------------------------------------------------------------------------------------------------

# Pattern 5

# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

# n = 5

# for i in range(n):
#     for j in range(i):
#         print("  ", end="")
#     for j in range(i,n):
#         print("* ", end="")
#     print()
    

# ---------------------------------------------------------------------------------------------------------------------

# Pattern 6

# Hill Pattern
#      *
#     ***
#    *****
#   *******
#  *********

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end="")
#     for j in range(i):
#         print("*", end="")
#     print()


# ---------------------------------------------------------------------------------------------------------------------

# Pattern 7

# Reverse Hill Pattern

#  *********
#   *******
#    *****
#     ***
#      *

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(i,n):
#         print("*", end="")
#     for j in range(i,n-1):
#         print("*", end="")
#     print()


# ---------------------------------------------------------------------------------------------------------------------

# Pattern 8

# Diamond Pattern - Combination of uphill and reverse hill pattern

#      *
#     ***
#    *****
#   *******
#  *********
#  *********
#   *******
#    *****
#     ***
#      *

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end="")
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(i,n):
#         print("*", end="")
#     for j in range(i,n-1):
#         print("*", end="")
#     print()


# ---------------------------------------------------------------------------------------------------------------------

# Pattern 9

# Sandglass Pattern - Reversal of Diamond Pattern

#  *********
#   *******
#    *****
#     ***
#      *
#      *
#     ***
#    *****
#   *******
#  *********

# n = 5

# for i in range(n):
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(i,n):
#         print("*", end="")
#     for j in range(i,n-1):
#         print("*", end="")
#     print()

# for i in range(n):
#     for j in range(i,n):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end="")
#     for j in range(i):
#         print("*", end="")
#     print()


# ---------------------------------------------------------------------------------------------------------------------

# Pattern 10

# Double Hill Pattern

#      *        *
#     ***      ***
#    *****    *****
#   *******  *******
#  ******************

# n = 5 
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end="")
#     for j in range(i):
#         print("*", end="")
#     for j in range(i,n-1):
#         print(" ", end="")
#     for j in range(i,n-1):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end="")
#     for j in range(i):
#         print("*", end="")
#     print()


# ---------------------------------------------------------------------------------------------------------------------

# Pattern 11

# Left Pascal Triangle

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# n = 5

# for i in range(n):
#     for j in range(i+1):
#         print("* ", end="")
#     print()

# for i in range(n):
#     for j in range(i,n-1):
#         print("* ", end="")
#     print()


# ---------------------------------------------------------------------------------------------------------------------

# Pattern 12

# Right Pascal Triangle

#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

# n = 5

# for i in range(n):
#     for j in range(i,n-1):
#         print("  ", end="")
#     for j in range(i+1):
#         print("* ", end="")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print("  ", end="")
#     for j in range(i,n-1):
#         print("* ", end="")
#     print()


# ---------------------------------------------------------------------------------------------------------------------

# Pattern 13

# Butterfly Pattern

# *                 * 
# * *             * * 
# * * *         * * * 
# * * * *     * * * * 
# * * * * * * * * * * 
# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * * 
# * *             * * 
# *                 * 

# n = 5

# for i in range(n):
#     for j in range(i+1):
#         print("* ", end="")
#     for j in range(i,n-1):
#         print("  ", end="")
#     for j in range(i, n-1):
#         print("  ",end= "")
        
#     for j in range(i+1):
#         print("* ", end="")
#     print()

# for i in range(n):
#     for j in range(i,n):
#         print("* ",end= "")
#     for j in range(i):
#         print("  ", end="")
#     for j in range(i):
#         print("  ",end= "")
        
#     for j in range(i,n):
#         print("* ", end="")
#     print()