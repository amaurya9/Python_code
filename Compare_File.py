import argparse
import filecmp
def compareFile(i,o):
    if i!=None and o!=None:
        #fd = open(args.i)
        #fd1=open(args.o)
        #if sum(1 for line in fd if line.rstrip()) == sum(1 for line in fd1 if line.rstrip()):
        fd = open(i)
        fd1 = open(o)
        if len(fd.readlines())!=len(fd1.readlines()):
            print("both the file are different")
        else:
            fd.seek(0,0)
            fd1.seek(0,0)
            line1=fd.readline()
            line2=fd1.readline()
            count=0
            while line1!="" and line2!="":
                if line1==line2:
                    pass
                else:
                    count=+1
                    print("both the file is different")
                    break
                line1=fd.readline()
                line2=fd1.readline()
            if count==0 and (fd.tell()==fd1.tell()):
                print("both the file is same")
        #print(filecmp.cmp(args.i,args.o))
    else:
        print("please enter both the file name")
    fd.close()
    fd1.close()
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-i",type=str)
    parser.add_argument("-o",type=str)
    args=parser.parse_args()
    compareFile(args.i,args.o)

if __name__ == '__main__':
    main()