#Created on 22 Apr 2015

go = True
first = raw_input()
test = []
for chars in first:
    test.append(chars)
test = set(test)
if len(test)<4:
    go = False

try:
    nums = first.split()
except:
    print("No solution")
    go = False
if go:    
    #print nums

    dick = {'0':1,'1':2,'2':3,'3':4,'4':5,'5':6,'6':7,'7':8,'8':9,'9':10,'a':11,'b':12,'c':13,'d':14,'e':15,'f':16,'g':17,'h':18,'i':19,'j':20,'k':21,'l':22,'m':23,'n':24,'o':25,'p':26,'q':27,'r':28,'s':29,'t':30,'u':31,'v':32}
    stuff = []
    for stuffs in nums:
        for bits in stuffs:
            stuff.append(bits)
    stuff = set(stuff)
    
    mini = len(stuff)+1
    maxi = 0
    for things in range(mini,33):
        #print things
        maxi = things
        a=0
        b=0
        c=0
        for num in range(0,len(nums[0])):
            count = 0
            first = dick[((nums[0])[num])]-1
            for leng in range(num+1,len(nums[0])):
                count+=1
            first = int(first)
            a += first*(things**count)
            #print "a",a
        for num in range(0,len(nums[1])):
            count = 0
            first = dick[((nums[1])[num])]-1
            for leng in range(num+1,len(nums[1])):
                count+=1
            first = int(first)
            b += first*(things**count)
            #print "b",b
        for num in range(0,len(nums[2])):
            count = 0
            first = dick[((nums[2])[num])]-1
            #print first
            for leng in range(num+1,len(nums[2])):
                count+=1
            #print count
            first = int(first)
            c += first*(things**count)
            #print "c",c
        #print a+b,c
        if a + b == c: 
            print maxi
            break
        elif things == 32:
            print("No solution")