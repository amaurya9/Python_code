def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left,right)

def merge(left,right):
    if not len(left) or not len(right):
        return (left or right)

    result = []
    i,j = 0,0

    while(left[i] and right[j]):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1

        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result

def quickSort(arr,low,high):
    if low >= high:
        return

    pi = partition(arr,low,high)

    quickSort(arr,low,pi-1)
    quickSort(arr,pi+1,high)
    return arr

def partition(arr,low,high):
    pivot = arr[high]
    i = low -1
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]

    return i+1

if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    #print("sorted Array is",quickSort(array,0,len(array)-1))
    print("sorted Array is", mergeSort(array))