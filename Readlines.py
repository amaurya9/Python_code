def readEvenLines():
    fd=open(eval(input("enter file name for print of even numbered lines")))
    line=fd.readline()
    while (line!=""):
        line=fd.readline()
        print(line)
        line=fd.readline()
    fd.close()
def readLines():
    fd=open(eval(input("enter file name")))
    line=fd.readline()
    while (line!=""):
        print(line)
        line=fd.readline()
    fd.close()
if __name__ == '__main__':
    #readLines()
    readEvenLines()