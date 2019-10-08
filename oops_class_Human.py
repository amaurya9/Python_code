class Human(object):
    religion="humanity"
    def __init__(self,name,address):
        self.name=name
        self.address=address
        print("done with constructor")
    def __del__(self):
        print("destructor called")
if __name__ == '__main__':
    emp1=Human("ashok","pune")
    emp2=Human("maurya","azamgarh")
    print(emp1)
    print(emp1.__dict__)
    print(Human.__dict__)