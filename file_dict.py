import os
if __name__ == '__main__':
    fd = open(input("Please enter the file name to open"),"r+")
    print(fd.seekable())
    var1 = str(fd.read(10))
    while (var1 != ""):
        print(var1)
        #fd.seekable()
        #fd.tell()
        fd.seek(fd.tell()+10,0)
        var1 = str(fd.read(10))
    print("-------------------------------------------------------------------------------------")
    fd.seek(10, 0)
    var1 = str(fd.read(10))
    while (var1 != ""):
        print(var1)
        fd.seek(fd.tell()+10,0)
        var1 = str(fd.read(10))
    fd.close()