#Created on 6 May 2015
import time
def multi(start):
    return (start * 1.25).is_integer()

a = time.clock()
start = 6
count = 0
temp = start
while True:
    if multi(temp):
        if count == 0:
            temp = start
        temp = (temp*1.25)+1
        count +=1
    else:
        count = 0
        start +=5
        temp = start
    if count == 5:
        break
print temp
print "This took: %ss" % (time.clock()-a)