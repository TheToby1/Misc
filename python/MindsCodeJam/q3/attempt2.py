#Created on 25 Apr 2015

# Copyright (C) 2014 Liu Xinyu (liuxinyu95@gmail.com)
# Edited by Toby Burns for better understanding         
#   If there exists a decomposition for both a and b ==> a
#   else if there exists a decomposition for b ==> b
#   otherwise ==> a
import sys

b1 = False
both = False
def exist(a, b, n):
    global b1,both
    if both:
        return True
    if a == 1 and b==1:
        both,b1 = True,True
        return True
    if b==1:
        b1=True

    for x in xrange(n, 1, -1):
        if b % x == 0 and exist(a, b/x, x-1):
            return True
        if a % x == 0 and exist(a/x, b, x-1):
            return True

    return False

def main():
    global b1,both
    for line in sys.stdin:
        b1,both = False,False
        [s1, s2] = line.split()
        (a, b) = (int(s1), int(s2))
        if a < b:
            (a, b) = (b, a)
        exist(a,b, 100)
        if both:print a
        elif b1:print b
        else:print a
thing = raw_input()
main()
