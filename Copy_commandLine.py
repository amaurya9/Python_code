import argparse
def copyFile(i,o,n):
    fd=open(i,"r+")
    fd1=open(o,"w+")
    if i !=None and o!=None and n !=None:
        if (n ==-1):
            #fd.read(i)
            fd1.write(fd.read())
        elif(n==0):
            pass
        elif(n<-1):
            print("Error,value enter is a negative number")
        else:
            for x in range (n):
                fd1.write(fd.readline())
        fd1=open(o)
        print(fd1.read())
    else:
        print("please enter input, output file and number of lines to copy")
    fd.close()
    fd1.close()
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-i",type=str)
    parser.add_argument("-o",type=str)
    parser.add_argument("-n",type=int)
    args=parser.parse_args()
    copyFile(args.i,args.o,args.n)
if __name__ == '__main__':
    main()