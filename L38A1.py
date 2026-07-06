# Binary search
def binary(arr,l,r,x):
    while l<=r:
        mid = l+(r-1)//2

    # check if x is present at mid
        if arr[mid]==x:
            return mid
    # if x is greater ignore the left half
        elif arr[mid]<x:
            l=mid+1
    # if x is smaller ignore the right half
        else:
            r = mid-1
    # return -1 if element not found
    return -1

# Driver's code
arr = [2,3,4,10,40]
x = 10

# function call
result = binary(arr,0,len(arr)-1,x)
if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print("Element is not present in the array")