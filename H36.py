Max_val = 100000000
def printClosest(arr,n,x):
    res_l,res_r = 0,0
    l,r,diff = 0,n-1,Max_val
    while r>l:
        if abs(arr[l]+arr[r]-x)<diff:
            res_l = l
            res_r = r
            diff = abs(arr[l]+arr[r]-x)
        if arr[l]+arr[r] > x:
            r -=1
        else:
            l+=1
    print(f"The closest pair to sum {x} is {arr[res_l]} and {arr[res_r]}")

if __name__ == '__main__':
    arr = [7,18,65,84,87,91,99,113]
    n = len(arr)
    x = 118
    printClosest(arr,n,x)