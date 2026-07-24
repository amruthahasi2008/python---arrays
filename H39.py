def twointer(arr1,arr2):
    i = 0
    j = 0
    l = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            l.append(arr1[i])
            i+=1 
            j+=1
        elif arr1[i] < arr2[j]:
            i += 1 
        else:
            j += 1 
    return l

arr1 = [1,3,4,5,7,8]
arr2 = [4,5,6,8,9,11]
print("intersection of two array is :",twointer(arr1,arr2))