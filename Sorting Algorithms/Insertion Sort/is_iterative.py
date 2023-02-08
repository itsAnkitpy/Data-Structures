import os
os.system('cls')

arr = [5,15,3,0,12,17,0]

print(f'Original Array: {arr}')


for i in range(1,len(arr)):
    current_element = arr[i]
    position = i

    while current_element < arr[position-1] and position > 0:
        arr[position] = arr[position-1]
        position = position - 1

    arr[position] = current_element

print(arr)
