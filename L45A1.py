#Quick sort in python 
#Fuction to find the partition
def part(A,low,high):
    #Choosing the rightmost element as pivot
    pivot = A[high]
    #Pointer for greater element
    i = low-1

    #Compare each element with pivot
    for j in range(low,high):
        if A[j] <= pivot:
            #If element smaller than pivot is found swap it with the greater element pointed by i
            i = i+1

            #Swapping element at i with j
            (A[i],A[j]) = (A[j],A[i])

    #Swap the pivot element with the greater element specified by i
    (A[i+1],A[high]) = (A[high],A[i+1])

    #Return the position from where the partition is done
    return i + 1

#Function to perform quick sort 
def quicksort(A,low,high):

    if low < high:

        #Find pivot elements such that 
        # elements smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = part(A,low,high)

        #recursive call on the left of the pivot
        quicksort(A,low,pi-1)

        # recursive call on the right of the pivot
        quicksort(A,pi+1,high)

A = [8,17,22,12,0,9,16]
print("Unsorted Array:")
print(A)

n = len(A)-1

quicksort(A,0,n)
print('Sorted array')
print(A)

