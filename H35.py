def binary(arr,l,r,x):
    if r >=l:
        mid = l+(r-1)//2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary(arr,l,mid-1,x)
        else:
            return binary(arr,mid+1,r,x)
    else:
        return -1
    

arr = [2,3,4,10,40]
x = 10
result = binary(arr,0,len(arr)-1,x)
if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print("Element is not present in the array")
