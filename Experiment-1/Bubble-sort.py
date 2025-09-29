# Input number of elements
n = int(input("Enter the number of elements: "))

# Input array elements
arr = []
print("Enter", n, "elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

# Bubble Sort algorithm
for i in range(n - 1):  #  number of passes
    for j in range(n - i - 1):  #  comparing adjacent elements
        if arr[j] > arr[j + 1]:
            # Swap the elements 
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)
