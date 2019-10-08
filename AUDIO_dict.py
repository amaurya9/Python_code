def dictProgram(fd1):
    dict1={}
    var1=fd1.readline()
    while(var1!=""):
        if var1[0]=="[":
            break
        if "=" in var1 and var1[0]!="#":
            var1=var1.split("=")
            if "#" in var1[1]:
                var2=var1[1].split("#")
                dict1[var1[0]]=var2[0].rstrip()
            else:
                dict1[var1[0]]=var1[1].rstrip()
        var1=fd1.readline()
    return dict1,var1
def fullDict(fd2):
    dict2={}
    var1=fd2.readline()
    while(var1!=""):
        if var1[0] is "[" and var1[-2] is "]":
            dict3,var3=dictProgram(fd2)
            dict2[var1[1:-2]]=dict3
            var1=var3
        else:
            var1=fd2.readline()
    print(dict2)

if __name__ == '__main__':
    fd=open(input("please enter file name to open"))
    #dictProgram(fd)
    fullDict(fd)


#{"General":{"master":True,"Disable":"Getways,sources,socket","Autoconnect":true},"HeadSet":{"HFP":true,"ManConnected":1,"FastConnectble":False},"A2DP":{"SBCSources":"1","MPEGSources":0}}