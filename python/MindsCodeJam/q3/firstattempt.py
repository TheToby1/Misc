#Created on 25 Apr 2015

# Copyright (C) 2014 Liu Xinyu (liuxinyu95@gmail.com)
# Edited by Toby Burns for better understanding         
#   If there exists a decomposition for both a and b ==> a
#   else if there exists a decomposition for b ==> b
#   otherwise ==> a
import sys

class Judge:
    def __init__(self):
        self.both_OK = False
        self.b_OK = False

    def exist(self, a, b, n):
        if self.both_OK:
            return True

        if a == 1 and b==1:
            (self.both_OK, self.b_OK) = (True, True)
            return True

        if b == 1:
            self.b_OK = True

        for x in xrange(n, 1, -1):
            if b % x == 0 and self.exist(a, b/x, x-1):
                return True
            if a % x == 0 and self.exist(a/x, b, x-1):
                return True

        return self.both_OK

    def result(self, a, b, n):
        self.exist(a, b, n)
        return not ( self.b_OK and not self.both_OK)

def main():
    for line in sys.stdin:
        
        [s1, s2] = line.split()
        (a, b) = (int(s1), int(s2))
        if a < b:
            (a, b) = (b, a)
        if Judge().result(a, b, 100):
            print a
        else:
            print b
thing = raw_input()
main()
