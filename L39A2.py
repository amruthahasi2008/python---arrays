#Find if There is a pair in A[0...N-1] with given Sum
# Using Two pointer method

def isPairSum(A,N,X):
    # represents first pointer
    i = 0
    # represents second pointer
    j = N - 1

    while (i < j):

        # If we find a pair
        if (A[i]+A[j] == X):
            return[A[i],A[j]]
        # if the sum of element in current pointers is less, we move towards higher values by doing i = i + 1
        elif (A[i]+A[j] < X):
            i +=1
        # if the sum of element in current pointers is more, we move towards lower values by doing j = j- 1
        else:
            j-=1
    return 0

# Array declaration
arr = [2,3,5,8,9,10,11]

#value to search
val = 17

print(f"Pair with the sum {val} equal to is - {isPairSum(arr,len(arr),val)}")

