#Program for insertion sort
A = [10,5,13,8,2]

# Traverse through the array
for i in range(1, len(A)):
    value = A [i]
    #Move Elements of A[0...i-1]that are greater than value to one position ahead than their current
    j = i-1
    while j >=0 and value < A[j]:
        A[j+1] = A[j]
        j-=1
        A[j+1] = value
#Driver Code
print("Sorted Array")
for i in range(len(A)):
    print("%d"%A[i],end = " ")
