A = [8,0,9,3]
for i in range(len(A)):
    min_i = i
    for j in range(i+1,len(A)):
        if A[min_i] > A[j]:
            min_i = j
    A[i] , A[min_i] = A[min_i],A[i]

print("Sorted Array")
for i in A:
    print(i,end=" ")