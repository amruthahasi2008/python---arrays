def minelement(a,size):
    temp = a[0]
    for i in range(1,size):
        if a[i]<temp:    # min(temp,a[i])
            temp = a[i]
    return temp

def maxelement(a,size):
    temp = a[0]
    for i in range(1,size):
        if a[i]> temp :  #max(temp,a[i])
            temp = a[i]
    return temp

a = [12,1234,45,67,1]
size = len(a)
print("Min",minelement(a,size))
print("Max",maxelement(a,size))

