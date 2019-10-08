if __name__ == '__main__':
    fd=open(input("please enter file name to open"))
    var1=fd.readline()
    var2=0
    while(var1!=""):
        if len(var1)>var2:
            var2=len(var1)
            var3=var1
        var1=fd.readline()
    print("longest line in file is {} and length is {}".format(var3,var2))