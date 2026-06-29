def reversed(arr,arr_size):
    if arr_size <=1:
        return arr
    else:
        return arr[::-1]
    
arr = [1,2,3]
arr_size = len(arr)
print("reversed array",reversed(arr,arr_size))
    

        