class Account():
    def __init__(self,fname,lname,pan,deposit):
        self.fname=fname
        self.lname=lname
        self.pan=pan
        self.__balance=deposit  #protected(_) , private(__)
        self.userid=self.fname+'@123'
        self.password=self.lname+self.pan[:3]

    def setBalance(self,amt):
        self.__balance=self.__balance+amt

    def getBalance(self):
        return self.__balance