def isPermutedMatrix(mat, n):
    # Creating a string that contains
    # elements of first row.
    tmp = mat[0]*2
    print(tmp)

    # Start traversing remaining rows
    for i in range(1, n):
        flag = True
        for j in range(len(mat[i])):
            print(mat[i] == tmp[j:j + len(mat[i])])
            if mat[i] != tmp[j:j+len(mat[i])]:
                print(mat[i],tmp[j:j+len(mat[i])])
            else:
                flag = False
                break
        if flag:
            return False
    return True


# Driver code
if __name__ == "__main__":
    n = 4
    mat = [[1, 2, 3, 4],
           [4, 1, 2, 3],
           [3, 1, 4, 2],
           [2, 3, 4, 1]]

    if (isPermutedMatrix(mat, n)):
        print("Yes")
    else:
        print("No")
