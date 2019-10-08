import math
def IsQube(x):
    for i in range (1,int(math.sqrt(x))+1):
        if x%((i*i)*i)==0 and x/((i*i)*i)==1:
            return True
            break
def ListOfQubeInRange(lb,ub):
    return [x for x in range(lb,ub) if IsQube(x)]
if __name__ == '__main__':
    x= eval(input("enter lb for range of list"))
    y= eval(input("enter ub for range of list"))
    print(ListOfQubeInRange(x,y))