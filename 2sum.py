A = [-1,0,1,2,-1,-4]
B = 3

ans = []

A = sorted(A)

l = len(A)

for i in range(l-3):
    p1 = i+1
    p2 = l - 1

    if i == 0 or A[i] > A[i-1]:
        while p1 < p2:
            if A[p1] + A[p2] + A[i] == B:
                ans.append([A[i],A[p1],A[p2]])
                p1 += 1
                p2 -= 1
            elif A[p1] + A[p2] + A[i] < B:
                p1 += 1
            elif A[p1] + A[p2] + A[i] > B:
                p2 -= 1

print(ans)

