#Created on 25 Apr 2015
#doesn't work
fin1 = raw_input()
fin2 = raw_input()

info = map(int, fin1.split())
nums = map(int, fin2.split())

nums += nums[0:info[1]-1]
print nums
temp = nums[info[1]-info[2]:len(nums)-info[2]]
print temp
temp.sort()
print temp
print temp[0]