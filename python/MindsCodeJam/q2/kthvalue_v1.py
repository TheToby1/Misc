#Created on 25 Apr 2015

fin1 = raw_input()
fin2 = raw_input()

info = map(int, fin1.split())
nums = map(int, fin2.split())

nums += nums[0:info[1]-1]
temp = sorted(nums[0:0+info[1]])
kth = temp[info[2]-1]
for num in range(1,info[0]):
    remove1 = nums[num-1]
    lo = 0
    hi = len(temp)
    while lo < hi:
        mid = (lo+hi)//2
        if temp[mid] < remove1: lo = mid+1
        else: hi = mid
    temp.pop(lo)
    lo = 0
    hi = len(temp)
    insert1 = nums[num+info[1]-1]
    while lo < hi:
        mid = (lo+hi)//2
        if temp[mid] < insert1: lo = mid+1
        else: hi = mid
    temp.insert(lo,insert1)
    if (temp[info[2]-1]<kth):
        kth = temp[info[2]-1]
print kth