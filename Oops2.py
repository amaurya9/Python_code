class Complex:
    def __init__(self,realpart, imagpart):
        self.real=realpart
        self.imag=imagpart
    def __str__(self):
        return str(self.real)+" "+str(self.imag)+"i"
    #to display object using print method
    def add(self,c2):
        print("adding")
