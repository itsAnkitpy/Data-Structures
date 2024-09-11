# Pattern 1

# Hollow Right Triangle

# *         
# * *       
# *   *     
# *     *   
# * * * * * 

# n = 5

# for i in range(n):
#     for j in range(n):
#         if j == 0 or i == n-1 or i == j:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


#----------------------------------------------------------------------------------------------------------------------

# Pattern 2

# Reverse Hollow Right Triangle

# * * * * * 
# *     *   
# *   *     
# * *       
# *   

# n = 5

# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n-j-1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


#----------------------------------------------------------------------------------------------------------------------

# Pattern 3

# * * * * * 
#   *     * 
#     *   * 
#       * * 
#         * 

# n = 5

# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == n-1 or i==j:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


#----------------------------------------------------------------------------------------------------------------------

# Pattern 4

#         * 
#       * * 
#     *   * 
#   *     * 
# * * * * * 

# n = 5
# for i in range(n):
#     for j in range(n):
#         if j == n-1 or i == n-1 or i == n-j-1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

#----------------------------------------------------------------------------------------------------------------------

# Pattern 5

#         *         
#       *   *       
#     *       *     
#   *           *   
# * * * * * * * * * 

# n = 5
# for i in range(n):
#     for j in range(0, n*2-1):
#         if i == n-1 or i+j == n-1 or j-i == n-1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

#----------------------------------------------------------------------------------------------------------------------

# Pattern 6

# ********************
# *                  *
# *                  *
# *                  *
# *                  *
# ********************

# rows = 6
# columns = 20

# for i in range(rows):
#     for j in range(columns):
#         if i == 0 or i == rows-1 or j == 0 or j == columns-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()