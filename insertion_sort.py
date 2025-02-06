# Insertion Sort

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place key in the correct position
        arr[j + 1] = key

# Given dataset
data = [27, 15, 39, 21, 28, 70]

# Calling the insertion sort function
insertion_sort(data)

# Printing the sorted array
print("Sorted array:", data)
