class MyDate():
    def __init__(self,date,month,year):
        self.Date=date
        self.Month=month
        self.Year=year
    def __del__(self):
        print("distructor is called")

    def get (self):
        print(self)
        return self.__dict__

    def setDay(self,Day):
        if Day >
    def set (self,date,month,year):






if __name__=="__main__":
    date1=MyDate(24,1,2017)
    print(date1.get())