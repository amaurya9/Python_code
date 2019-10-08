def dictProgram(fd1):
    dict1={}
    var1=fd1.readline()
    while(var1!=""):
        if "=" in var1 and var1[0]!="#":
            var1=var1.split("=")
            if "#" in var1[1]:
                var2=var1[1].split("#")
                dict1[var1[0]]=var2[0].rstrip()
            else:
                dict1[var1[0]]=var1[1].rstrip()
        var1=fd1.readline()
    print(dict1)

if __name__ == '__main__':
    fd=open(input("enter file name to open"))
    dictProgram(fd)
