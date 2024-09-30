def bubbleSortRecursive(arr,n):
    count = 0
    if n == 1:
        return
    # We do one pass of normal Bubble sort iterative method to fix the last element position.Then we reduce the size of 
    # array by 1(n-1)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            count += 1
    
    if count == 0:
        return
    
    bubbleSortRecursive(arr, n-1)

arr = [5,15,3,0,12,17,0]
n = len(arr)

print('Original array: ', arr)

bubbleSortRecursive(arr, n)

print('Sorted array: ', arr)