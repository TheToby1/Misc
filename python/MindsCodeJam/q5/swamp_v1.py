# Enter your code here. Read input from STDIN. Print output to STDOUT#Created on 26 Apr 2015
import sys

def searcher(start, end):
    #print start
    try:
        if end in dick[start]:
            return True
        elif start in dick[end]:
            return True
        else:
            for things in dick[start]:
                dick[things].remove(start)
                dick[start].remove(things)
                if searcher(things,end):
                    return True
    except:
        None
    return False

#with open("in.txt", "r") as fin:
    #filein = fin.read().splitlines()
filein = [line.strip() for line in sys.stdin.readlines()]
filein.pop(0)
times = int(filein.pop(0))

mapp = filein[0:times]
#print mapp

dick = {}

for thing in mapp:
    thing = thing.split()
    first = (thing[0],thing[1])
    second = [(thing[2],thing[3])]
    dick[first] = second
for thing in mapp:
    thing = thing.split()
    first = (thing[0],thing[1])
    second = (thing[2],thing[3])
    try:
        dick[second].append(first)
    except:
        dick[second] = [first]
#print dick

querys = filein[times+1:]
#print querys

for thing in querys:
    thing = thing.split()
    first = (thing[0],thing[1])
    second = (thing[2],thing[3])
    if searcher(first,second): print "T"
    else: print "F"
            