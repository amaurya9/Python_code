#Write a program to accept a filename from user & display it in reverse order
import argparse
items=[]
def push(item):
    items.append(item)

def pop():
    return items.pop()
def is_empty():
    return (items == [])

def ReadFile(i):
    fd=open(i)
    char1=fd.read(1)
    while char1:
        push(char1)
        char1=fd.read(1)
    fd1=open("NewTestFile.txt","w+")
    while not is_empty():
        fd1.write(pop())
    fd1.close()
    fd1=open("NewTestFile.txt")
    print(fd1.read())

def main():
    parser=argparse.ArgumentParser("please enter file name to reverse")
    parser.add_argument("-i",type=str,help="enter input file name")
    pars=parser.parse_args()
    ReadFile(pars.i)
if __name__ == '__main__':
    main()