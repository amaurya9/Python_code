def nQueen(n):
    result = []
    if nQueenUtil(n,0,result):
        print(*result)
    else:
        print("Not Possible to have Queen")

def nQueenUtil(n,row,result):
    if n == row :
        return True
    for col in range(n):
        isSafe = True
        for pos in result:
            if pos[1] == col or pos[0] - pos[1] == row - col or pos[0] + pos[1] == row + col:
                isSafe = False
                break
        if isSafe:
            result.append([row,col])
            if nQueenUtil(n,row+1,result):
                return True
    result.pop()
    return False

if __name__ == "__main__":
    nQueen(8)
