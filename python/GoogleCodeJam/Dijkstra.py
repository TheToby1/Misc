'''
Created on 12 Apr 2015

@author: Toby
'''

with open("input.in", "r") as fin:
    filein = fin.read().splitlines()
times = int(filein.pop(0))

count = 0
x = 0
answer = False
dic = {'ii':'-1','ij':'+k','ik':'-k','ji':'-k','jj':'-1','jk':'+i','ki':'+j','kj':'-i','kk':'-1'}

with open("output3.in", "w") as fout:
    sign = True
    first = False
    second = False
    third = False
    leave = False
    for things in filein:
        spelling = ''
        if count%2==0:
            bit = things.split()
            x = int(bit[1])
        else:
            spelling = things
            spellinglong = ''.join([spelling for num in xrange(x)])
            print "start",spellinglong
            if len(spelling)<2: answer = False
            elif len(spellinglong)<3: answer = False
            elif ("j" not in spelling) & ("k" not in spelling): answer = False
            elif ("i" not in spelling) & ("k" not in spelling): answer = False
            elif ("i" not in spelling) & ("j" not in spelling): answer = False
            else:
                if spellinglong[0]=="i": 
                    first = True
                    spellinglong = spellinglong[1:]
                    if spellinglong[0]=="j": 
                        second = True
                        spellinglong = spellinglong[1:]
                        if spellinglong[0]=="k": 
                            third = True
                            spellinglong = spellinglong[1:]
                            leave = True
                if not leave:
                    for nums in range(0,len(spellinglong)):
                        mult = spellinglong[0:2]
                        spellinglong = spellinglong[2:]
                        print mult
                        mult = dic[mult]
                        if mult[0] == '+': sign = True
                        else: sign = False
                        if "1" not in mult:
                            spellinglong = mult[1]+spellinglong
                        print spellinglong
                    
        count+=1