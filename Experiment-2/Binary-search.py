# import numpy as np
# def binarysearch(arr,l,r,key):
#     if(l<=r):
#         mid = l + (r - l) // 2
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             return binarysearch(arr, mid+1,r,key)
#         else:
#             return binarysearch(arr, l, mid-1,  key)
#     else:
#         return -1

# arr = [1,2,4,5,6,9,11,14]
# x = 1
# l=0
# r=len(arr)-1
# result = binarysearch(arr, l, r, x)
# print(result)

import numpy as np

def binarysearch(arr, l, r, key):
    if(l <= r):
        mid = l + (r - l) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binarysearch(arr, mid + 1, r, key)
        else:
            return binarysearch(arr, l, mid - 1, key)
    else:
        return -1

arr = [1, 2, 4, 5, 6, 9, 11, 14]
x = 11
l = 0
r = len(arr) - 1
result = binarysearch(arr, l, r, x)

# Printing the result in a readable way
if result != -1:
    print(f"Element {x} found at index {result}")
else:
    print(f"Element {x} not found in the array")
