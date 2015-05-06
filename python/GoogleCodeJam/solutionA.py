'''
Created on 12 Apr 2015

@author: Toby
'''
with open("A-large-practice.in", "r") as fin:
    filein = fin.read().splitlines()

num_cases = int(filein.pop(0))
with open("useless1.in", "w") as fout:
    for case in range(num_cases):
        raw_counts = filein[case].split()[1]
        counts = map(int, list(raw_counts))
        
        standing = 0
        invited = 0
        for i, count in enumerate(counts):
            if count:
                to_invite = max(i - standing, 0)
                invited += to_invite
                standing += to_invite + count
        print 'Case #%d: %d' % (case + 1, invited)
        fout.write('Case #%d: %d\n' % (case + 1, invited))