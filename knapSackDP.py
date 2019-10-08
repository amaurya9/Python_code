def knapSack(W,wt,val,n):
    K = [[0 for _ in range(W+1)] for _ in range (n+1)]
    for i in range(n + 1):
        for j in range(W+1):
            if i == 0 or j ==0:
                K[i][j] = 0
            elif(wt[i-1] <= j):
                K[i][j] = max(val[i-1]+K[i-1][j-wt[i-1]], K[i-1][j])
            else:
                K[i][j]=K[i-1][j]
    for x in K:
        print(x)
    max_value = K[i][j]
    wt_used = []
    while j > 0 and i > 0:
        if K[i][j] == K[i-1][j]:
            i = i-1
        else:
            wt_used.append(wt[i-1])
            i = i-1
            j = j-wt[i-1]
    print(wt_used)
    return max_value


if __name__ == "__main__":
    val = [100, 120, 70]
    wt = [1, 2, 3]
    W = 5
    n = len(val)
    print (knapSack(W, wt, val, n))
