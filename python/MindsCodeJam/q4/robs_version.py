#Created on 25 Apr 2015
#Rob Kelly, has an unknown mistake

import sys, math

lines = [line.strip() for line in sys.stdin.readlines()]

num = int(lines.pop(0))

points = []
for line in lines:
    x, y = map(int, line.split())
    points.append((x, y))


# find lowerst in y and x
p = None
p_idx = None
for idx, point in enumerate(points):
    if p == None:
        p_idx = idx
        p = point

    x1, y1 = p
    x2, y2 = point
    if y2 < y1 or (y2 == y1 and x2 < x1):
        p_idx = idx
        p = point

points.pop(p_idx)


# gragham scan

angles = []
p_x, p_y = p
for idx, point in enumerate(points):
    c_x, c_y = point
    delta_x = c_x - p_x
    delta_y = c_y - p_y
    angle = math.atan2(delta_y, delta_x) * (180 / math.pi)
    angles.append((angle, point))

def cross_prod(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return ((x2 - x1) * (y3 - y1)) - ((y2 - y1) * (x3 - x1))

angles.sort()

hull_points = []
p1 = p
a2, p2 = angles.pop(0)
hull_points.append(p1)
hull_points.append(p2)

for angle, p3 in angles:
    p1 = hull_points[-2]
    p2 = hull_points[-1]
    prod = cross_prod(p1, p2, p3)
    # This is the line that fucks everything up. Change to "<=" to fix
    while prod < 0:
        hull_points.pop()
        p1 = hull_points[-2]
        p2 = hull_points[-1]
        prod = cross_prod(p1, p2, p3)
    hull_points.append(p3)

for p in sorted(hull_points):
    print p[0], p[1]
