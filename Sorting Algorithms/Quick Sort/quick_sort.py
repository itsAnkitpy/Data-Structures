def partition(elements,start,end):
    pivot_index = start

    pivot = elements[pivot_index]

    while start < end:
        # The start should not exceed the whole length of array
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            elements[start],elements[end] = elements[end],elements[start]

    elements[end],elements[pivot_index] = elements[pivot_index],elements[end]
    # We return the pivot element index here.
    return end

def quick_sort(elements,start,end):
    if start < end:
        pivot = partition(elements,start,end)
        quick_sort(elements,start,pivot-1)
        quick_sort(elements,pivot+1,end)

elements = [11,9,29,7,2,15,28]

quick_sort(elements,0,len(elements)-1)
print(elements)

# Time Complexity - O(nlogn)
# Space Complexity - O(1)