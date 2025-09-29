arr = ['a','b',3,2,1]
n = len(arr)
max_value = 0
for ch in arr:
    if ord(ch) > max_value:
        max_value = ord(ch)

# Step 2: Create count array of size (max ASCII + 1)
count = [0 for _ in range(max_value + 1)]

# Step 3: Count each character based on ASCII value
for ch in arr:
    count[ord(ch)] += 1

# Step 4: Print sorted characters using count array
for ascii_val in range(len(count)):
    for _ in range(count[ascii_val]):
        print(chr(ascii_val), end=' ')
