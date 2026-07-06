# to do binary search recursively
def binary(arr,l,r,x):
    # check if the length of the array is greater then or equal to 0
    if r >=l:
        # find the mid element's index
        mid = l+(r-1)//2
        # if element is present in the middle itself
        if arr[mid] == x:
            return mid
        #if the element is smaller check in the left subarray
        elif arr[mid] > x:
            return binary(arr,l,mid-1,x)
        # else check in right subarray
        else:
            return binary(arr,mid+1,r,x)
    else:
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

