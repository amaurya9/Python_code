
def IsFebonacii(x):
    if x <= 2:
        return x
    print(x)
    return IsFebonacii(x-2) + IsFebonacii(x-1)
    '''a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
        print (a)
    return a'''

def ListOffebonaciiInRange(lb,ub):
    return [ x for x in range(lb,ub) if FebonaciList(x)<=ub] #[1,3,6,10,15,21]
[x for x in range(lb, ub) if x in fibotill(x)]

if __name__ == '__main__':
    x= eval(input("enter lb for range of list"))
    y= eval(input("enter ub for range of list"))
    print(ListOffebonaciiInRange(x,y))