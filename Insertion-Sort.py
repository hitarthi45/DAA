arr = [5, 2, 8, 4, 6]

def insertion_sort(arr):
    n = len(arr)
    # Traverse from the second element to the end of the array
    for i in range(1, n):
        key = arr[i]  # Current element to be inserted into the sorted part
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Place the key after the element just smaller than it
        arr[j + 1] = key
        print(arr)  # Print the array after each insertion step
    return(arr)

print(insertion_sort(arr))  # Call the function and print the sorted array