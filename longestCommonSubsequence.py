def commonSubsequence(A,B):
    mat = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

    print(mat)
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if A[i-1] == B[j-1]:
                mat[i][j] = mat[i-1][j-1]+1
            else:
                mat[i][j] = max(mat[i-1][j],mat[i][j-1])
    max_length = mat[i][j]
    array = []

    while (i > 0 and j > 0):
        if mat[i][j] == mat[i-1][j]:
            i = i-1
        elif mat[i][j] == mat[i][j-1]:
            j = j-1
        else:
            array.insert(0,A[i-1])
            i= i-1
            j = j-1
    print(array,"max length of common Subsequence is:",max_length)

if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    commonSubsequence(X,Y)