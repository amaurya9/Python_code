def mostFrequent(arr):
    hash = {}
    for x in arr:
        if x in hash.keys():
            hash[x] += 1
        else:
            hash[x] = 1
    hash = sorted(hash.items(),key=lambda x : x[1],reverse=True)
    print(hash[0][0])

def firstEleOccKtimes(arr,k):
    hash = {}
    for x in arr:
        if x in hash.keys():
            hash[x] += 1
        else:
            hash[x] = 1
    flag = True
    for x in arr:
        if hash[x] == k:
            print(x)
            flag = False
            break
    if flag:
        print(-1)



if __name__ == "__main__":
    #mostFrequent([10, 20, 10, 20, 30, 20, 20])
    firstEleOccKtimes([1, 7, 4, 3, 4, 8, 7],2)
