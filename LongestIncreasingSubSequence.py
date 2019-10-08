def incresingSubSequence(arr):
    tmp = [1]*len(arr)
    position = [0]*len(arr)
    n = len(arr)
    for i in range(1,n):
        for j in range(i):
            if arr[i] > arr[j]:
                if tmp[j]+1 > tmp[i]:
                    position[i] = j
                    tmp[i] = tmp[j]+1

    maximum = max(tmp)
    ind = tmp.index(maximum)
    inSequence = [arr[ind]]
    #print(tmp)
    #print(position)
    while ind > 0:
        ind = position[ind]
        inSequence.insert(0,arr[ind])

    return maximum, inSequence

if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print("Length of lis is", incresingSubSequence(arr))