# Quick Sort

def quick_sort(arr):
    # Base case: if the list has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose the pivot element (here, we are choosing the last element)
        pivot = arr[-1]
        
        # Partition the array into two sub-arrays:
        # One for elements less than or equal to the pivot
        # One for elements greater than the pivot
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        
        # Recursively apply quick_sort on the left and right sub-arrays
        return quick_sort(left) + [pivot] + quick_sort(right)

# Given dataset
data = [27, 15, 39, 21, 28, 70]

# Calling the quick sort function and printing the sorted array
sorted_data = quick_sort(data)
print("Sorted array:", sorted_data)

