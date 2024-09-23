# Print your Name N times using recursion

def print_name(i,n):
    if i!=n:
        print("Ankit")
        print_name(i+1, n)

print_name(0, 5)
