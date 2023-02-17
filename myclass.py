class person:
    name=''
    phone=''
    fatherName=''
    bankAccountBalance=0

    def __init__(self,n,p, f, b):
        self.name=n
        self.phone=p
        self.fatherName=f
        self.bankAccountBalance=b
        
    def TellMeYourName(self):
        print(self.name)

    def depositFund(self, amount):
        self.bankAccountBalance=self.bankAccountBalance+amount

    
    


