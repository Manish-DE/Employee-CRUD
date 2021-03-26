def binary_search(arr,start,end,num):
    if(end > start):
        mid = end-start // 2

        if(arr[mid] == num):
            return num
        
        elif(arr[mid] > num):
            binary_search(arr,0, mid-1, 10)
        else:
            binary_search(arr,mid + 1, end, 10)
    else:
        return -1



arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")