def max_product(arr):
    if len(arr) < 2:
        return None
    arr.sort() 
    prod_start = arr[0] * arr[1]     
    prod_end = arr[-1] * arr[-2]     
    if prod_start > prod_end:
         return (arr[0], arr[1])
    else :
        return (arr[-2], arr[-1])
    
arr = [1,6,4,6,5,9,18,55,78,54,4,7]
print(max_product(arr))
