# Find if There is a pair in A[0...N-1] with given Sum
def isPairSum(A,N,X):
    for i in range(N):
        for j in range(N):
            # as equal i and j means same element
            if (i == j):
                continue
            # if pair exists
            if (A[i]+A[j]==X):
                return[A[i],A[j]]
            # as the array is sorted
            if(A[i]+A[j]>X):
                break
    return 0
arr = [2,3,5,8,9,10,11]

#value to search
val = 17
print(f"Pair with the sum {val} equal to is - {isPairSum(arr,len(arr),val)}")



