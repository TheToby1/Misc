'''
Created on 11 Apr 2015

@author: Toby
'''

with open("A-large-practice.in", "r") as fin:
    filein = fin.read().splitlines()

times = int(filein.pop(0))
case = 0
with open("useless.in", "w") as fout:
    for things in filein:
        case+=1
        things1 = things.split()
        maxim = int(things1[0])
        total = 0
        shy = True
        position = 2
        needed = 0
        nums = []
        for num in things1[1]:
            nums.append(int(num))
        for value in range(0,len(nums)-1):
            total += nums[value]
            if nums[value+1]>0:
                if total<value + 1:
                    needed += value+1-total
                    total+=needed
        print nums
        print maxim
        print "Case #%s: %s" % (case, needed)
        fout.write("Case #%s: %s\n" % (case, needed))