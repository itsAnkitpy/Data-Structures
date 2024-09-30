def insertionSortRecursive(arr, n):
    if n <= 1:
        return
    insertionSortRecursive(arr, n-1)

    last = arr[n-1]
    j = n-2
    
    
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = last

arr = [5,15,3,0,12,17,0]
n = len(arr)

print('Original array: ', arr)

insertionSortRecursive(arr, n)

print('Sorted array: ', arr)