A = 3
arr = ['0','1']

while len(arr) != pow(2,A):
    arr_ = arr[::-1]
    newarr = ['0'+i for i in arr]
    newarr_ = ['1'+i for i in arr_ ]
    arr = newarr + newarr_

print(a