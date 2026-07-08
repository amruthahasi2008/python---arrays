# Program to show bubble sort 
def BubbleSort(arr):
    n = len(arr)
    #Traverse through an array
    for i in range(n):
        for j in range(0,n-i-1):
            #Traverse the array from 0-1 swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
#Drivers code
arr = [64,34,25,12,22,11,90]
BubbleSort(arr)
print("Sorted Array")
for i in arr:
    print(i,end = " ")