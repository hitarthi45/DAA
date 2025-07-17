arr = [9, 3, 7, 1, 5, 2, 8, 4, 6]
#in-place sorting algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort(arr))

#Q-1 Number of swaps Number of comparisions for different input types of array(Ascending, descending, all same, random)
def selection_sort_stats(arr):
    n = len(arr)
    swaps = 0
    comparisons = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return  comparisons, swaps

ascending = [1, 2, 3, 4, 5, 6, 7, 8, 9]
descending = [9, 8, 7, 6, 5, 4, 3, 2, 1]
all_same = [5] * 9
randomized = [9, 3, 7, 1, 5, 2, 8, 4, 6]

results = {
    "Ascending": selection_sort_stats(ascending),
    "Descending": selection_sort_stats(descending),
    "All Same": selection_sort_stats(all_same),
    "Randomized": selection_sort_stats(randomized)
}

for case, (comparisons, swaps) in results.items():
    print(f"{case}: Comparisons = {comparisons}, Swaps = {swaps}")