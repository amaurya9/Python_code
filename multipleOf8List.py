def IsMultipleEight(n):
    if (n & 7)==0:
        return True
    #else:
      #  return True
def MultipleOfEightList(lb,ub):
    return [x for x in range(lb,ub) if IsMultipleEight(x)]
if __name__ == '__main__':
    x= eval(input("enter lb for range of list"))
    y= eval(input("enter ub for range of list"))
    print(MultipleOfEightList(x,y))