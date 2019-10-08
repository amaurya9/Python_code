def segmentTree(arr,segTree,low,high,root):
    if low == high:
        segTree[root] = arr[low]
        return #segTree[root]
    mid = (low+high)//2
    left = segmentTree(arr,segTree,low,mid,2*root+1)
    #print("Left is :",left)
    right = segmentTree(arr,segTree,mid+1,high,2*root+2)
    #print("Right is :", right)
    #segTree[root] = left + right
    segTree[root] = segTree[2*root+1]+segTree[2*root+2]
    #return segTree[root]

def maxSegTree(arr,segMTree,low,high,root):
    if low == high:
        segMTree[root] = arr[low]
        return

    mid = (low + high)//2
    maxSegTree(arr,segMTree,low,mid,2*root+1)
    maxSegTree(arr,segMTree,mid+1,high,2*root+2)
    segMTree[root] = max(segMTree[2*root+1],segMTree[2*root+2])

def minSegTree(arr,minTree,low, high,root):
    if low == high:
        minTree[root] = arr[low]
        return
    mid = (low+high)//2
    minSegTree(arr,minTree,low,mid,2*root+1)
    minSegTree(arr,minTree,mid+1,high,2*root+2)
    minTree[root] = min(minTree[2*root+1], minTree[2*root+2])


def SumInRange(arr,segTree,low,high,qlow,qhigh,root):
    if high < qlow or low > qhigh:
        return 0
    elif(low >= qlow and high <= qhigh):
        return segTree[root]
    else:
        mid = (low+high)//2
        return(SumInRange(arr,segTree,low,mid,qlow,qhigh,2*root+1)+SumInRange(arr,segTree,mid+1,high,qlow,qhigh,2*root+2))

def maxInRange(arr,segMTree,low,high,qlow,qhigh,root):
    if high < qlow or low > qhigh:
        return 0
    elif(low >= qlow and high <= qhigh):
        return segMTree[root]
    else:
        mid = (low+high)//2
        return max(SumInRange(arr,segMTree,low,mid,qlow,qhigh,2*root+1),SumInRange(arr,segMTree,mid+1,high,qlow,qhigh,2*root+2))

def minInRange(arr,minTree,low,high,qlow,qhigh,root):
    if low > qhigh or high < qlow:
        return 100000
    elif(low >= qlow and high <= qhigh):
        return minTree[root]
    else:
        mid = (low+high)//2
        return min(minInRange(arr,minTree,low,mid,qlow,qhigh,2*root+1), minInRange(arr,minTree,mid+1,high,qlow,qhigh,2*root+2))

if __name__ == "__main__":
    arr = [1,2,3,4]
    segTree = [0 for i in range(2*len(arr)-1)]
    segMTree = [-100000 for i in range(2*len(arr)-1)]
    minTree = [100000 for i in range(2*len(arr)-1)]
    #segmentTree(arr,segTree,0,3,0)
    #for x in segTree:
    #    print(x)
    #print("Sum is :",SumInRange(arr,segTree,0,3,1,3,0))
    #maxSegTree(arr,segMTree,0,3,0)
    #for x in segMTree:
    #    print(x)
    #print("Max is :", maxInRange(arr, segMTree, 0, 3, 1, 3, 0))
    minSegTree(arr, minTree, 0, 3, 0)
    for x in minTree:
        print(x)
    print("Min is :", minInRange(arr, minTree, 0, 3, 1, 3, 0))