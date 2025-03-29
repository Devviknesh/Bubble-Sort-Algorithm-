def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # Track if any swaps occur
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                swapped = True
        if not swapped:  # If no swaps, list is already sorted
            break

# Example usage
if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", sample_list)
    
    bubble_sort(sample_list)
    
    print("Sorted list:", sample_list)
