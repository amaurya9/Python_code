def numberOfPath(row, col, n, m, row_array, col_array, array):
    if row == n-1 and col == m-1:
        print(array)
        return
    for i in range(len(row_array)):
        new_row = row + row_array[i]
        new_col = col + col_array[i]

        if new_row < n and new_col < m:
            array.append((new_row, new_col))
            #print("value of i and index", i, new_row, new_col,"********************")
            numberOfPath(new_row, new_col, n, m, row_array, col_array, array)
            #print("value of i and index",i,new_row,new_col)
            array.pop()
    return

def maxNumberOfPath(n,m):
    mat = [[0 for _ in range (m)] for _ in range (n)]

    if m ==1 or n == 1:
        return 1
    for i in range (n):
        mat[i][0] = 1
    for i in range(m):
        mat[0][i] = 1

    for i in range(1,n):
        for j in range(1,m):
            mat[i][j] = mat[i-1][j] + mat[i][j-1]
    return mat[n-1][m-1]

n, m = 3,3
array = [(0, 0)]
row_array = [0, 1]
col_array = [1, 0]
#numberOfPath(0, 0, int(n), int(m), row_array, col_array, array)
print(maxNumberOfPath(n,m))