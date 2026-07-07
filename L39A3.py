#Program to find the pair with the sum closest to the given num
Max_val = 100000000

#Function to print the pair with the closest sum
def printClosest(arr,n,x):
    #To store indexes of result pair
    res_l,res_r = 0,0
    # Intialise left and right indexes and difference between pair sum and x
    l,r,diff = 0,n-1,Max_val

    while r>l:
        # check if this pair is closer then the closest pair so far
        if abs(arr[l]+arr[r]-x)<diff:
            res_l = l
            res_r = r
            diff = abs(arr[l]+arr[r]-x)
        if arr[l]+arr[r] > x:
            #if this pair has more sum ,move to smaller values
            r -=1
        else:
            #move to larger values
            l+=1
    print(f"The closest pair to sum {x} is {arr[res_l]} and {arr[res_r]}")

#Drivers code
if __name__ == '__main__':
    arr = [10,22,28,29,30,40]
    n = len(arr)
    x = 54
    printClosest(arr,n,x)

