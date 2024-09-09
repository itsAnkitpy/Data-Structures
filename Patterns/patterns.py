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