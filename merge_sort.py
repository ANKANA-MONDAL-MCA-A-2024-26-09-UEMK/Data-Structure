# Merge Sort

def merge_sort(arr):
    # Base case: If the list has one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle of the array
    mid = len(arr) // 2
    
    # Recursively divide the array into two halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the two sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0
    
    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    # If there are any remaining elements in either half, add them to the result
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

# Given dataset
data = [27, 15, 39, 21, 28, 70]

# Calling the merge sort function and printing the sorted array
sorted_data = merge_sort(data)
print("Sorted array:", sorted_data)

