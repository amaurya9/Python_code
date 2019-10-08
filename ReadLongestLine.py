print ("Enter config file name to open")
pd = open(input())
var1 = pd.readline()
length = len(var1)
var3=''
while var1 != '':
    var1 = pd.readline()
    if length < len(var1):
        length = len(var1)
        var3 = var1
print ("Longest line in file is- {} and length of file is- {}".format(var3,length))