# Merge sort is more efficient than Quick sort.

import random
import time

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle of the array
        left_half = arr[:mid]  # Dividing the elements into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort the first half
        merge_sort(right_half)  # Recursively sort the second half

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for remaining elements in left_half or right_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Quick Sort implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Function to measure sorting time
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time

# Main function to compare both sorting algorithms
def compare_sorts():
    # Generate a random list of 1000 integers
    arr_size = 1000
    arr_merge = [random.randint(1, 10000) for _ in range(arr_size)]
    arr_quick = arr_merge.copy()  # Use the same random list for both sorts

    # Measure the time for Merge Sort
    merge_time = measure_time(merge_sort, arr_merge)

    # Measure the time for Quick Sort
    quick_time = measure_time(quick_sort, arr_quick)

    print(f"Time taken by Merge Sort: {merge_time:.6f} seconds")
    print(f"Time taken by Quick Sort: {quick_time:.6f} seconds")

# Run the comparison
if __name__ == "__main__":
    compare_sorts()

    
