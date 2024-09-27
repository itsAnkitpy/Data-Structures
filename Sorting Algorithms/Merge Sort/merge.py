# Without using temporary array

def merge_sort(arr):
    # Base case: if the array has more than one element
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2
        
        # Divide the array into two halves
        L = arr[:mid]  # Left half
        R = arr[mid:]  # Right half
        
        # Recursively sort both halves
        merge_sort(L)
        merge_sort(R)
        
        # Initialize indices for L, R, and arr
        i = j = k = 0
        
        # Merge the two sorted halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Check if any elements were left in L
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        # Check if any elements were left in R
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Example usage
arr = [9, 4, 7, 6, 3, 1, 5]
print("Original array:", arr)