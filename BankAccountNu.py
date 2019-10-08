#Write a simple BankAccount class. Account number should be auto-generated. Implement withdraw  and deposit methods for the same.
# Write a menu driven program to perform account operations.
class BankAccount():
    accountNumber=1000
    def __init__(self,name,address):
        self.Name=name
        self.Address=address
        self.balance=0
        BankAccount.accountNumber+=1
        self.AccountNumber=BankAccount.accountNumber

    def deposit(self,amount):
        self.balance+=amount
        print("Deposit is successful and total balance is {}".format(self.balance))

    def withdraw (self, amount):
        if (self.balance- amount)<0:
            print("insufisient valance, please try lower amount")
        else:
            self.balance-=amount
            print("withdrawal is successful and remaining amount is {}".format(self.balance))
    def details(obj):
        print("  name",obj.Name,"\n","Balance",obj.balance,"\n","Address",obj.Address,"\n","Account Number",obj.AccountNumber)

if __name__ == '__main__':
    #acc=[]
    #i=0
    """
    acc1=BankAccount("Ashok","Azamgarh")
    acc2=BankAccount("maurya","Azamgarh")
    acc1.details()
    acc1.deposit(10000)
    acc1.withdraw(2000)
    acc1.details()
    acc2.details()
    acc2.withdraw(2000)"""
    objectList={}
    while (True):
        print("please select on option from the menu ")
        print(" 1 for addition of new acc ","\n","2 for details of account","\n","3 for deposit of money","\n","4 for withdrawal of money","\n","5 for exit")
        option=eval(input())
        #print(option)
        if option==1:
            print("please input new account member name and address")
            name=input()
            address=input()
            objectList[name]=BankAccount(name,address)
            #acc.append(name)
            print(objectList[name].__dict__)
        elif option==2:
            print("please input account member name for details")
            accMember=input()
            if accMember in objectList:
                objectList[accMember].details()
            else:
                print("Entered member is not a member of our bank")
        elif option==3:
            accMember=input("please input account member name for deposit money, and amount ")
            amount=eval(input())
            objectList[accMember].deposit(amount)
        elif option==4:
            accMember=input("please input account member name for withdrawal of money, and amount to withdraw")
            amount=eval(input())
            objectList[accMember].withdraw(amount)
        elif option==5:
            print("exiting the program")
            break
        else:
            print("please enter a valid option from the menu")
