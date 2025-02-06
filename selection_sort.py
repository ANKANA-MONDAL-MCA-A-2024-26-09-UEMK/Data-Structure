#Selection Sort
def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Swap the found minimum element with the element at index i
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Given dataset
data = [27, 15, 39, 21, 28, 70]

# Calling the selection sort function
selection_sort(data)

# Printing the sorted array
print("Sorted array:", data)

