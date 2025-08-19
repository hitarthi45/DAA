import numpy as np
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merge_sort(left)
    merge_sort(right)
    return(merge_sort(left,right))
def merge(left,right): 
    merged = []
    i = j = 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1

    merge.extend(left[i:])
    merge.extend(right[j:])
    return merge

arr = [5,2,4,1,6,9,3]
print(merge_sort(arr))