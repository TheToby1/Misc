'''
Created on 11 Apr 2015

@author: Toby
'''
from collections import Counter
from operator import itemgetter
with open("B-small-attempt4.in", "r") as fin:
    filein = fin.read().splitlines()

times = int(filein.pop(0))
count = 0
case = 0
with open("output1.in", "w") as fout:
    for things in filein:
        things = things.split()
        total = 0
        if count%2==0:
            cust = int(things[0])
        else:
            case+=1
            print things
            nums = Counter()
            for num in things:
                nums[int(num)]+=1
            nums = nums.items()
            for things in range(0,len(nums)):
                nums[things] = list(nums[things])
            working = True
            while(working):
                nums.sort(key=itemgetter(0))
                num = 1
                while num < len(nums)-1:
                    if (nums[num])[0]==(nums[num-1])[0]:
                        (nums[num])[1]+=(nums[num-1])[1]
                        nums.remove(nums[num-1])
                    elif len(nums)>2:
                        if(nums[num])[0]==(nums[num+1])[0]:
                            (nums[num])[1]+=(nums[num+1])[1]
                            nums.remove(nums[num+1])
                    num+=1
                if (nums[0])[0]==0:
                    nums.pop(0)
                print nums
                if len(nums)>1:
                    if (nums[-1])[0]<4:
                        total += (nums[-1])[0]
                        working = False
                    elif (nums[-1])[0]%2!=0:
                        for things in nums:
                            things[0]-=1
                        total+=1
                    elif ((nums[-1])[1]<(nums[-2])[0])&((nums[-1])[0]/2>(nums[-1])[1]):
                        total+=(nums[-1])[1]
                        temp = nums.pop()
                        temp[0]=temp[0]/2
                        temp[1]=temp[1]*2
                        nums.append(temp)
                    else: 
                        total += (nums[-1])[0]
                        working = False
                else:
                    if (nums[-1])[0]<4:
                        total += (nums[-1])[0]
                        working = False
                    elif (nums[-1])[0]%2!=0:
                        for things in nums:
                            things[0]-=1
                        total+=1
                    elif ((nums[-1])[0]/2>=(nums[-1])[1]):
                        total+=(nums[-1])[1]
                        temp = nums.pop()
                        temp[0]=temp[0]/2
                        temp[1]=temp[1]*2
                        nums.append(temp)
                    else: 
                        total += (nums[-1])[0]
                        working = False
                print total
            print total
            fout.write("Case #%s: %s\n" % (case, total))
        count+=1