#Shell sort in python
A = [9,8,3,7,5,6,4,1]
#Intialising n
n = len(A)
#Rearranging the elements at each n/2,n/4,... intervals
interval = n//2

while interval > 0:
    for i in range (interval,n):
        temp = A[i]
        j = i
        while j >= interval and A[j - interval] > temp:
            A[j] = A[j - interval]
            j-= interval
        A[j] = temp
    interval//=2

#Drivers code 
print("Sorted array")
print(A)