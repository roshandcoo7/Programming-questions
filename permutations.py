a = [1,2,3]

ans = []
def permutation(arr,size,n):
    if size == 1:
        ans.append(arr)
    for i in range(size):
        permutation(arr,size-1,n)
        if size & 1:
            arr[0],arr[size-1] = arr[size-1],arr[0]
        else:
            arr[i],arr[size-1] = arr[size-1],arr[i]

def combinations(arr,n):
    if n == 0:
        return [[]]
    else:
        l = []
        for i in range(len(arr)):
            m = arr[i]
            remList = arr[i+1:]

            for p in combinations(remList,n-1):
                l.append([m]+p)
        return l

# b = combinations(a,2)
# print(b)
permutation(a,len(a),len(a))
print(ans)