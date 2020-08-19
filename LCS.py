A = "BATD"
B = "ABACD"

# !Recursion
# def LCS(A,B,m,n):
#     if n == 0 or m == 0:
#         result = 0
#     elif A[m-1] == B[n-1]:
#         result = 1 + LCS(A,B,m-1,n-1)
#     else:
#         result = max(LCS(A,B,m,n-1),LCS(A,B,m-1,n))
#     return result

# !DP
def LCS(text1,text2):
    m,n = len(text1), len(text2)
    t = [ [0] *(n+1) for _i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i-1] == text2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1],t[i-1][j])
    return t[m][n]

print(LCS(A,B))