print("Please enter a file name")
fileName = input()
print (fileName)
pd = open(fileName)
var1 = pd.read(10)
while var1!='':
    print(var1)
    pd.read(10)
    var1=pd.read(10)
