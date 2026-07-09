#build in Function
def compare(n1,n2):
    return str(n1)+str(n2) > str(n2)+str(n1)

def largest(num):
    for i in range(len(num),0,-1):
        temp = 0
        for j in range(i):
            if not compare(num[j],num[temp]):
                temp = j
        num[temp],num[i-1] = num[i-1],num[temp]
    return str(int("".join(map(str,num))))

#Drivers Code
arr = [3,30,34,5,9]
print("given array",arr)
print("Largest possible number",largest(arr))
