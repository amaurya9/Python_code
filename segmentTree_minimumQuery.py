def nextPowerOf2(n):
    p = 1
    if (n and not (n & (n - 1))):
        print("value of n", n)
        return n
    while(p < n):
        p <<= 1
    return p

def segmentTree(arr):
    max = float("INF")
    n = len(arr)
    size = nextPowerOf2(n)
    segTree = [max]*(2*size - 1)
    print(segTree)
    segTreeUtil(segTree,arr,0,n-1,0)
    return segTree

def segTreeUtil(segTree,arr,low,high,pos):
    if low == high:
        segTree[pos] = arr[low]
        return
    mid = (low + high)//2
    segTreeUtil(segTree,arr,low,mid,2*pos+1)
    segTreeUtil(segTree, arr, mid+1, high, 2*pos+2)
    segTree[pos] = min(segTree[2*pos+1], segTree[2*pos+2])
    #return

def rangeMinQuery(segTree,low,high,qlow,qhigh,pos):
    max_value = float("INF")
    if qlow > high or qhigh < low:
        return max_value
    elif low >= qlow and high <= qhigh:
        return segTree[pos]
    mid = (low + high)//2
    left = rangeMinQuery(segTree, low, mid, qlow, qhigh, 2 * pos + 1)
    right = rangeMinQuery(segTree, mid + 1, high, qlow, qhigh,2 * pos + 2)
    return min (left, right)

if __name__ == "__main__":
    arr = [1, 3, 2, 7]
    segTree = segmentTree(arr)
    n = len(arr)
    print(segTree)
    print(rangeMinQuery(segTree,0,n-1,2,3,0))