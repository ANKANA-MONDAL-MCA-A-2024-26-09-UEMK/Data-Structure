# Quick sort is better than the Bubble sort

import random
import time

# Bubble Sort implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if elements are in the wrong order

# QuickSort implementation
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
    arr_bubble = [random.randint(1, 10000) for _ in range(arr_size)]
    arr_quick = arr_bubble.copy()  # Use the same random list for both sorts

    # Measure the time for Bubble Sort
    bubble_time = measure_time(bubble_sort, arr_bubble)

    # Measure the time for Quick Sort
    quick_time = measure_time(quick_sort, arr_quick)

    print(f"Time taken by Bubble Sort: {bubble_time:.6f} seconds")
    print(f"Time taken by Quick Sort: {quick_time:.6f} seconds")

# Run the comparison
if __name__ == "__main__":
    compare_sorts()
