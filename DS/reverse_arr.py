def reverseList(arr, min, max):
    while(min < max):
        temp = arr[min]
        arr[min] = arr[max]
        arr[max] = temp
        min += 1
        max -= 1
    return arr

def reverserecList(arr, min, max):
    if(min >= max):
        return;
    else:
        arr[min],arr[max]=arr[max],arr[min]
        reverserecList(arr,min+1, max-1)

A = [1, 2, 3, 4, 5, 6]
print(A)
reverserecList(A, 0, 5)
print("Reversed list is")
print(A)