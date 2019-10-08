class Human:
    planet="Earth" #class Attributes
    #constructors:implisitly invoked  on object creation
    def__init__(self,age,name):
        print ("Constructor")
        self.age=age
        self.name=name
        print (id(self.age))
        print (id(Human.planet))

    def__del__(self):
        print("Destructor Invoked")
    def Walk(self):
        print ("Waking")

if __name__=="__main__":
    x=Human(28,"Jeetendra")
    print(x.age)
    peint(x,name)
    x.walk()
    x.teach=True
    #add new attribute at run time.
    print (dir(x))
    print (dir(y))
    print (dir(Human))