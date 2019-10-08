def nextGreaterElement(arr):
    n = len(arr)
    stack = []
    stack.append(0)
    result = [-1]*n
    for i in range(1,n):
        while len(stack) > 0 and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

if __name__ == "__main__":
    arr = [4,5,2,25,13,7,6,12]
    print(nextGreaterElement(arr))