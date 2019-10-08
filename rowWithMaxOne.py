def rowWithMaxOne(mat,row,col):
    flag = False
    for j in range(col):
        for i in range(row):
            if mat[i][j] == 1:
                print(i+1,end= " ")
                flag = True
        if flag :
            break

if __name__ == "__main__":
    mat=[[1,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]
    rowWithMaxOne(mat,4,4)