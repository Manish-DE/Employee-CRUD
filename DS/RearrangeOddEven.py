import array as a 
import numpy as np 

def rearrangeArr(arr,num):
    tempArr = np.empty(num, dtype = object)
    for j in range(0, num): 
        tempArr[j] = arr[j] 
    tempArr.sort()
    
    mid = (num-1) // 2
    
    arr[0] = tempArr[mid]
    num1 = 0
    for i in range(0,num,2):
        num1 += 1
        if(i == 0):
            arr[0] = tempArr[mid]
        else:
            arr[i] = tempArr[mid + num1]
            arr[i + 1] = tempArr[mid - num1]
        
    for i in range(num):
        print(arr[i], end = " ")
    
         

         
# Driver code 
arr =  [9, 10, 9, 12, 13, 14, 16, 16 ]
9,9,10,12,13,14,16,16
#12,13,10,14,9,16,9,16
rearrangeArr(arr, 8) 


