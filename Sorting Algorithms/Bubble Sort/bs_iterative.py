import os
os.system('cls')

arr = [5,15,3,0,12,17,0]

print(f'Original Array: {arr}')
# Ascending order
for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(f'Sorted array ascending: {arr}')

# Descending order
for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if arr[j] < arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(f'Sorted array descending: {arr}')