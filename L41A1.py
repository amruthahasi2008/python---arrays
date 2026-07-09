# Program for selection sort
# Array
A = [64,25,12,22,11]
#Traverse through the array
for i in range(len(A)):
    # Find the min element in the remaining array
    min_i = i
    for j in range(i+1,len(A)):
        if A[min_i] > A[j]:
            min_i = j
    # Swap the min element with the first element
    A[i] , A[min_i] = A[min_i],A[i]

# Driver code
print("Sorted Array")
for i in A:
    print(i,end=" ")


