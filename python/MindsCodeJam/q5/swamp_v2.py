#Created on 26 Apr 2015
import sys

with open("in.txt", "r") as fin:
    filein = fin.read().splitlines()
#filein = [line.strip() for line in sys.stdin.readlines()]
space = filein.pop(0)
space = space.split()
space = map(int, space)
times = int(filein.pop(0))

mapp = filein[0:times]
#print mapp

sets = dict()
print space
for nums in range(0,space[0]*space[1]):
    print nums
    y = nums%space[0]
    x = nums/space[0]
    sets[nums]=([x,y])
    print sets[nums]

mapp
