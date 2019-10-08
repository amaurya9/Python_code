class BankAccount:
    accountNumber =100
    def __init__(self,name, amount=0):
        self.name=name
        self.amount=amount
        self.autoNumber=BankAccount.accountNumber+1
    def balance(self,money):
        if money>self.amount:
            self.amount=self.amount+money
            print("total balance is less so adding amount to existing,Total balance is {}".format(self.amount))
        else:
            self.amount=self.amount-money
            print("total balance is more so  removing amount to existingTotal balance is {}".format(self.amount))

acc = BankAccount("ashok",1000)
acc2= BankAccount("maurya",10000)
acc.balance(100)
acc2.balance(1500)