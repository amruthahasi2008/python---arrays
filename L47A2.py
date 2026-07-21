#Program to check the array is rotated and sorted
arr = [3,4,5,1,2]
n = len(A)
count = 0

#iterating the loop from 1 to length of array
for i in range(1,n):
    #Comparing items of array
    if(arr[i-1]>arr[i]):
        count +=1
    
#Special case- comparing last element to the first element
if (arr[n-1]< arr[0]):
    count +=1

#drivers code
print(count <=1)