# Binary Search Implementation
import time
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)
    # Test binary search with a timer
arr = list(range(1, 1000001))
target = 999999
start_time = time.time()
binary_search(arr, target, 0, len(arr) - 1)
end_time = time.time()
print(f"Binary Search Execution Time: {end_time - start_time:.6f} seconds")


# Merge Sort Implementation

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1

        else:
            sorted_array.append(right[j])
            j += 1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array
# Test merge sort with a timer
arr = [i for i in range(10000, 0, -1)]
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()
print(f"Merge Sort Execution Time: {end_time - start_time:.6f} seconds")


# Observing Time Complexity
# Let’s analyze time complexity by running each algorithm on arrays of increasing sizes
# and recording the time taken.
import numpy as np
def analyze_algorithm(algorithm, sizes, is_recursive=True):
    times = []
    for n in sizes:
        arr = list(range(n))
        if is_recursive:
            start_time = time.time()
            algorithm(arr, 0, n - 1) if algorithm == binary_search else algorithm(arr)
            end_time = time.time()
        else:
# For non-recursive calls like merge sort, call without bounds
            start_time = time.time()
            algorithm(arr)
            end_time = time.time()
        times.append(end_time - start_time)
    return times
# Test sizes for analysis
sizes = [2**10, 2**12, 2**14, 2**16, 2**18]
binary_search_times = analyze_algorithm(lambda arr: binary_search(arr, target, 0,
len(arr)-1), sizes)
merge_sort_times = analyze_algorithm(merge_sort, sizes)

# Display time results
print("Binary Search Times:", binary_search_times)
print("Merge Sort Times:", merge_sort_times)