def sortArray(A):
    #Base case
    if len(A) <= 1:
        return
    x = -1
    y = -1
    prev = A[0]

    #process each pair of adjacent elements
    for i in range(1,len(A)):
        #if the previous value greater than the next element
        if prev > A[i]:
            #first occurence of conflict
            if x == -1:
                x = i-1
                y = i
            else:
                #second occurence of conflict
                y = i
        prev = A[i]

    #Swap the element at index x and y
    swap(A,x,y)

def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

if __name__ == '__main__':
    a = [3,5,6,9,8,7]
    print("Orginal Array",a)
    sortArray(a)
    print("Sorted Array: ",a)
