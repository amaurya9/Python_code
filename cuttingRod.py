def cuttingRod(arr,price,lenth):
    mat = [[0 for _ in range(length+1)] for _ in range(len(arr)+1)]

    for i in range(1,len(arr)+1):
        for j in range(1,lenth+1):
            if arr[i-1] > j:
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = max(mat[i-1][j], price[i-1] + mat[i][j-arr[i-1]])

    for x in range(len(mat)):
        print(mat[x])
    return mat[i][j]

if __name__=="__main__":
    lengthArray = [1, 2, 3, 4]
    price = [2,5,7,8]
    length = 9
    print("Maximum Obtainable price for length is:",cuttingRod(lengthArray,price,length))