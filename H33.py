#Part - 1
arr = [-4,6,2,0,0,1,1]
print("Full array :",arr)
print("Left of index 2: ",arr[:2])
print("Right of index 2: ",arr[3:])
print("Left Sum: ",sum(arr[:2]))
print("Right Sum: ",sum(arr[3:]))

#Part - 2
print("\n Balance Sum")
for i in range(len(arr)):
    L = sum(arr[:i])
    R = sum(arr[i+1:])
    print("Index",i,"->","Left: ",L,"Right: ",R)

#Part - 3 
print("\nEquillibrium point:")
for i in range(len(arr)):
    if sum(arr[:i]) == sum(arr[i+1:]):
        print("Index ",i,"Element",arr[i])

#Part -4
nums = [3,6,2,2,4,1]
target = 10
print("Growing window(start =1,target =",target, " ):")
curr = 0
for j in range(1,len(nums)):
    curr += nums[j]
    print("nums[1 to",j,"] =",nums[1:j+1],"sum =",curr)
    if curr > target:
        break

#Part -5
print("\nSearching all windows:")
found = False
for i in range(len(nums)):
    if found:
        break
    curr = 0
    for j in range(len(nums)):
        curr += nums[j]
        if curr == target:
            print("Found! Indexes",i,"to",j,":",nums[i:j+1])
            found = True
            break
        if curr > target :
            break
if not found:
    print("No subarray found")
