arr = [5,2,3,4,6]
max_value = 0
for i in range(len(arr)):
    if(arr[i]  > max_value):
        max_value = arr[i]

count=[0 for i in range(max_value+1)]
for i in range(len(arr)):
    count[arr[i]] = count[arr[i]]+1
    
for i in range(1, len(count)):
    for j in range(count[i]):
        print(i)

#Sort the characters (alphabets and digits)using the count count array
#ord() function is used to convert a character to its ASCII value
#chr() function is used to convert an ASCII value back to a character