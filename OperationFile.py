import argparse
def appendFile(i,o,n):
    fd=open(i,"r+")
    fd1=open(o,"a+")
    if i !=None and o!=None and n !=None:
        if (n ==-1):
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
        fd.close()
        fd1.close()
    else:
        print("please enter input, output file and number of lines to copy")

def differanceFile(i,o):
     if i!=None and o!=None:
        fd = open(i)
        fd1 = open(o)
        line1=fd.readline()
        line2=fd1.readline()
        while line1!="" or line2!="":
            if line1==line2:
                pass
            else:
                print("below line are different","\n",line1,"\n",line2)
                print("-------------------------------------------------")
            line1=fd.readline()
            line2=fd1.readline()
     else:
        print("please enter both the file name")
def main():
    parser=argparse.ArgumentParser("please enter option to perform operation on files.")
    parser.add_argument("-i",type=str,help="enter input file name")
    parser.add_argument("-o",type=str,help="enter output file name")
    parser.add_argument("-n",type=int,help="enter number of line to copy")
    parser.add_argument("--operation",type=str,help="enter name of operation to perform on file")
    args=parser.parse_args()
    op=args.operation
    if op =="copy":
        import Copy_commandLine
        Copy_commandLine.copyFile(args.i,args.o,args.n)
    elif op=="comp":
        import Compare_File
        Compare_File.compareFile(args.i,args.o)
    elif op=="diff":
        differanceFile(args.i,args.o)
    elif op=="append":
        appendFile(args.i,args.o,args.n)
    else:
        print("Please Enter --operation with expected value to perform from (copy,comp,diff,append)")

if __name__ == '__main__':
    main()