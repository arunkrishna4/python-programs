# Single Level-Inheritance
class demo:
    a = 10
    b = 20
    c = 30

class demo1(demo):
    d = 90
    e = 89
    f = 70

c1 = demo()
c2 = demo1()



class Bank:
    bname = 'SBI'
    contact = 2855622112
    def __init__(self, name, address, bal):
        self.name = name
        self.add = address
        self.bal = bal

    def deposit(self, amount):
        self.bal += amount

    def withdraw(self, amount):
        if self.bal >= amount:
            self.bal -= amount
        else:
            print('Insuffecient Balance')

    def display(self):
        print("the name of the customer is :" + self.name)
        print("the Address of the customer is :" + self.add)
        print("the available Balance is :" + str(self.bal))


c1 = Bank('allen', 'Banglore', 2500)

class Bank1(Bank):
    def __init__(self, name, add, bal, pno, email):
        Bank.__init__(self, name, add, bal)
        self.pno = pno
        self.email = email

    def display(self):
        Bank.display(self)
        print("the Email of the customer is :" + self.email)
        print("the Phone Number of the customer is :" + str(self.pno))
        
    
c2 = Bank1('anna', 'chili', 5000, 8179267926, 'anna@gmail.com')
# Multi-Level Inheritance:-
# Deriving the properties from oneclass to another by considering more than one level.
class demo:
    a = 10
    b = 20

class demo1(demo):
    c = 30
    d = 40

class demo2(demo1):
    e = 50
    f = 60
    

o1 = demo()
o2 = demo1()
o3 = demo2()

class Resume:
    def __init__(self, name, pno, email, add, tyop, tp):
        self.name = name
        self.pno = pno
        self.email = email
        self.add = add
        self.tyop = tyop
        self.tp = tp

    def ch_pno(self, new):
        self.pno = new

    def ch_email(self, new):
        self.email = new

    def display(self):
        d = self.__dict__
        for attribute, value in d.items():
            print(f"The {attribute} of the Candidate is {value}")

c1 = Resume('steve', 9876543210, 'steve@gmail.com', 'bbsr', 2013, 99)

class Resume1(Resume):
    def __init__(self, name, pno, email, add, tyop, tp, twyop, twp):
        super().__init__(name, pno, email, add, tyop, tp)
        self.twyop = twyop
        self.twp = twp

c2 = Resume1('allen', 8529637410, 'allen@gmail.com', 'puri', 2018, 75, 2020, 65)

class Resume2(Resume1):
    def __init__(self, name, pno, email, add, tyop, tp, twyop, twp, dyop, dp):
        super().__init__(name, pno, email, add, tyop, tp, twyop, twp)
        self.dyop = dyop
        self.dp = dp

c3 = Resume2('alex', 9658741230, 'alex@gmail.com', 'ganjam', 2015, 35, 2020, 35.5, 2025, 37) 







