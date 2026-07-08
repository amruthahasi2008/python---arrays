# Program to show bubble sort 
def BubbleSort(arr):
    n = len(arr)
    #Traverse through an array
    for i in range(n):
        swap = False
        for j in range(0,n-i-1):
            #Traverse the array from 0 to n-i-1 swap if the element is greater then the next element
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
                swap = True
        #if no two elements were swapped by the inner loop,then break
        if swap == False:
            break
#Driver's Code
arr = [64,34,25,12,22,11,90]
BubbleSort(arr)
print("Sorted Array: ")
for i in arr:
    print(i,end = " ")
