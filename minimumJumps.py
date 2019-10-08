def minimumJumps(arr):
    jump = [float("inf") for _ in range(len(arr))]
    ind = [0]

    jump[0] = 0
    n = len(arr)
    for i in range(1,n):
        for j in range(i+1):
            print(j,end=" ")
            if i < j+arr[j]+1:
                jump[i] = min(jump[i],jump[j]+1)
                ind.append(j)
                break
        print("value of i:",i)
    print(jump)
    print(ind)
    jumpPath = []
    i = n-1
    jumpPath.append(arr[n-1])
    while i >0:
        i = ind[i]
        jumpPath.append(arr[i])
    print("Jump Path is:",*jumpPath[::-1])
    return jump[n-1]

if __name__ == "__main__":
    arr = [1, 3, 6, 1, 0, 9]
    #size = len(arr)
    print('Minimum number of jumps to reach',
          'end is', minimumJumps(arr))