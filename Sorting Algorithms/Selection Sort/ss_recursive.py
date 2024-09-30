def selectionSortRecursive(arr, n):
    if n == 1:
        return
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    selectionSortRecursive(arr, n-1)


arr = [5,15,3,0,12,17,0]

print('Original array: ', arr)

selectionSortRecursive(arr, len(arr))

print('Sorted array: ', arr)