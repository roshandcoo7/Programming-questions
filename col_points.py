def slopeOf(p1,p2):
    x1,y1,x2,y2 = p1[0],p1[1],p2[0],p2[1]
    if x2 == x1:
        return 'inf'
    else:
        if y1 == y2:
            return 0
        else:
            return (y2-y1)/(x2-x1)

points = [(0,0),(1,1),(-1,-1)]
max_points = 2
for i in range(len(points)):
    p = points[i]
    h = dict()
    for j in range(len(points)):
        if j != i:
            slope = slopeOf(points[j],p)
            h[slope] = h.get(slope,0)+1
    max = 1
    for m in h:
        if h[m] > max:
            max = h[m]
    if max_points < max + 1:
        max_points = max+1
    
print(max_points)

    
