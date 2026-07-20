#Program for Merge Sort in Python
def mergeSort(A):
    if len(A) > 1:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]

        #Recursion call on each half
        mergeSort(left)
        mergeSort(right)

        #Two iterators for traversing two halfs
        i = 0
        j = 0

        #Iterator for the main array
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                #The value from the left half has been used
                A[k] = left[i]
                i+=1

            else:
                A[k] = right[j]
                j+= 1

            #Move to the next slot
            k+=1
        while i < len(left):
            A[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            A[k] = right[j]
            j +=1
            k+=1

A = [59,80,38,17,90,31,56,55,21]
print("Unsorted Array: ",A)
mergeSort(A)
print("Sorted Array: ",A)

