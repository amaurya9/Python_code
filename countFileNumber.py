import os
import argparse
def calculateFile(i):
    count1=0
    dirctList=os.listdir(i)
    for x in dirctList:
        if os.path.isfile(x):
            count1+=1
    print("number of file in directory is {}".format(count1))
def main():
    parser=argparse.ArgumentParser("please enter file name to calculate number of all files in parent directory")
    parser.add_argument("-i",type=str,help="enter input file name")
    pars=parser.parse_args()
    calculateFile(os.path.dirname(os.path.abspath(pars.i)))

if __name__ == '__main__':
    main()

    #Write a program to count total number of files in present directory