# Function to find the missing element in a sorted array
def findsmallest(nums,l = None,r = None):
    #intialise left and right
    if l is None and r is None:
        (l,r) = (0,len(nums)-1)
    # base condition
    if l >r:
        return l
    mid = l +(r-l)//2
    # if the mid index matches with its value , then miss match
    # lies on the right half
    if nums[mid] == mid:
        return findsmallest(nums,mid+1,r)
    # if mismatch lies on right half
    else:
        return findsmallest(nums,l,mid-1)

if __name__ =='__main__'  :
    nums = [0,1,2,6,9,11,15]

    print("The smallest missing element is",findsmallest(nums))