def CountofOneBit (a):
    count=0
    while(a!=0):
        x=a
        a=a>>1
       # print(bin(a))
        if x!=a<<1:
            count+=1
    return count

if __name__ == '__main__':
    x= eval(input("enter the number"))
    print(bin(x))
    print(CountofOneBit(x))t