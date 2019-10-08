total = 12
str = [1,1,1,0,0,0,0,0,0,0,0,0]
if str[0] == 0:
    print(total)
if str[total - 1] == 1:
    print(0)
i = 0
n = total - 1
while (i < n):
    mid = (i + n) // 2
    if str[mid] == 0:
        if str[mid - 1] == 1:
            print("value of n,mid and i",n,mid,i)
            indZero = mid
            break
        else:
            n = mid
    if str[mid] == 1:
        if str[mid + 1] == 0:
            print("value of n and i", n,mid, i)
            indZero = mid + 1
            break
        else:
            i = mid
print("Total number of zeros are :",total - (mid + 1))