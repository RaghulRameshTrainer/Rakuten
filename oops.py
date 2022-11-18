class Employee():
    hike=1.1
    #Construtor
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.salary=pay
        self.email=self.fname+'.'+self.lname+'@gamil.com'

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def appraisal(self):
        #self.hike=20
        self.salary=int(self.salary*self.hike)

    @classmethod
    def create_object(cls,emp_str):
        fn,ln,sl=emp_str.split("-")
        return cls(fn,ln,int(sl))

    @staticmethod
    def is_workingday(dt):
        if dt.weekday()==5 or dt.weekday()==6:
            return "HOLIDAY!!!"
        return "Working Day!"

    def __str__(self):
        return "This is the Employee class object."

    def __add__(self,other):
        return self.salary+other.salary

    def __len__(self):
        return len(self.fullname())

class Company():
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.salary=pay
        self.email=self.fname+'.'+self.lname+'@gamil.com'

    def appraisal(self):
        self.salary=self.salary*2

class Developer(Employee,Company):
    def __init__(self,fname,lname,pay,tech):
        self.tech=tech
        super().__init__(fname,lname,pay)

    def testMethod(self):
        print("Hello")

    def testMethod(self,name):
        print(f"Hello {name}")

    def fullname(self,title):
        return f"{title} {self.fname} {self.lname}"

    def appraisal(self):
        super(Employee,self).appraisal()
        #Company.appraisal(self)

dev_1=Developer('Siva','Murugan',10000,'Python')
dev_2=Developer('Priya','Raman',20000,'Java')

print(dev_1.salary)
dev_1.appraisal()
print(dev_1.salary)
# print(dev_1.fullname('Mr'))
# print(dev_2.fullname("Miss"))
#dev_1.testMethod('Durga')

# print(dev_1.email)
# print(dev_2.email)
# print(help(Developer))





# str1="Levin-Lenus-100000"
# str2="Dinesh-Kumar-200000"
#
# emp_1=Employee.create_object(str1)
# emp_2=Employee.create_object(str2)
#
# import datetime
# tday=datetime.date(2022,11,21)

# print(emp_1)
# print(emp_2)
#print(emp_1+emp_2)
# print(len(emp_1))
# print(Employee.is_workingday(tday))
# fn,ln,sal=str1.split("-")
# emp_1=Employee(fn,ln,int(sal))
#
# fn,ln,sal=str2.split("-")
# emp_2=Employee(fn,ln,int(sal))

# emp_1=Employee('Bala','Murugan',50000)
# emp_2=Employee('Ramya','Rajesh',60000)

# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())
# print(emp_2.fullname())

#emp_1.hike=1.2
# print("Levin's Current Salary: ", emp_1.salary)
# emp_1.appraisal()
# print("Levin's Revised Salary: ", emp_1.salary)
#
# print("Dinesh's Current Salary: ", emp_2.salary)
# emp_2.appraisal()
# print("Dinesh's Revised Salary: ", emp_2.salary)


# Types of method:

# Instance method/object METHOD
# Class method
# Static Method

#OOPS Features:
# Abstraction
# Inheritence
# Polymorphsim
# Encapsulation