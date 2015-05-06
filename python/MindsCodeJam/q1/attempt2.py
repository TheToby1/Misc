#Created on 25 Apr 2015

fin = raw_input()
nums = fin.split()
equal = False
answer = 0
mini = 0
for chars in fin:
    if ord(chars)>mini:
        mini = ord(chars)
if mini < 58:
    mini = mini - 47
else:
    mini = mini -86

for num in range(mini,33):
    a = int(nums[0],num)
    b = int(nums[1],num)
    c = int(nums[2],num)
    if a + b == c:
        equal = True
        answer = num
        break
if equal:
    print answer
else:
    print "No solution"