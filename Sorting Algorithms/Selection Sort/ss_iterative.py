import os
os.system('cls')

arr = [5,15,3,0,12,17,0]

print(f'Original Array: {arr}')

# Sorting in Ascending Order
for i in range(len(arr)):
    min_index = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i],arr[min_index] = arr[min_index],arr[i]

print(f'Sorted in ascending: {arr}')

# Sorting in Descending Order
for i in range(len(arr)):
    min_index = i

    for j in range(i+1, len(arr)):
        if arr[j] > arr[min_index]:
            min_index = j

    arr[i],arr[min_index] = arr[min_index],arr[i]

print(f'Sorted in descending: {arr}')


# Using min() and max() function
for i in range(len(arr)):
    min_val = min(arr[i:])
    min_ind = arr.index(min_val,i)
    arr[i],arr[min_ind] = arr[min_ind],arr[i]

print(f'Sorted using min(): {arr}')

for i in range(len(arr)):
    max_val = max(arr[i:])
    max_ind = arr.index(max_val,i)
    arr[i],arr[max_ind] = arr[max_ind],arr[i]

print(f'Sorted using max(): {arr}')