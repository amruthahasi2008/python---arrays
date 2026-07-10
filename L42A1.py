class Data:
    def __init__(self,value,index,count=0):
        self.value = value
        self.index = index
        self.count = count

# Custom sort by element's frequency and index
def sortbyfi(arr):
    if arr is None or len(arr)<2:
        return
    hm = {}

    #for each array element insert into dict its frequency and index of its first occurence in the array
    for i in range(len(arr)):
        hm.setdefault(arr[i],Data(arr[i],i)).count +=1
    
    #get the values
    values = [*hm.values()]

    #Sort the values based on a custom comparator
    # 1. if two elements have different frequencies, then the one which has more frequency comes first
    #2. if two elements have same frequencies, then one with the less index should come first
    values.sort(key = lambda x:(-x.count,x.index))


    k = 0
    for data in values:
        for j in range(data.count):
            arr[k] = data.count
            k +=1

if __name__ == "__main__":
    arr = [3,3,1,1,1,8,3,6,1,7,8]
    print("Orginal Array: ",arr)
    sortbyfi(arr)
    print("Sorted: ",arr)
    