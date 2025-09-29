arr = [1, 3, 7, 5, 2, 6, 4, 8]
key = int(input("Enter the value: "))
def linear_search (arr,key):
    for i in range(0,len(arr)):
        if(key==arr[i]):
            print("element found")
            return
    print("element not found")
linear_search(arr,key)

#Q-1 write code for counting occurence of key
def occurence_count(arr,key):
    count = 0
    for i in range(0,len(arr)):
        if(key==arr[i]):
            count += 1
    return count
occurence_count(arr,key)
print("count of key is", occurence_count(arr,key))

#Q-2 Identify the number of times a key is occuring in odd indices
def odd_indice_occurence_count(arr,key):
    count = 0
    for i in range(0,len(arr)):
        if(key==arr[i]):
            if(i%2!=0):
                count += 1
    return count
odd_indice_occurence_count(arr,key)
print("count of key in odd indices is", odd_indice_occurence_count(arr,key))