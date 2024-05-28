# Public Access Specifiers
class Bank:
    b_name = 'SBI'
    ceo = 'singa'
    mbl = 'Mumbai'

    def __init__(self, name, pno, email, add, bal, gender, aadhar):
        self.name = name
        self.pno = pno
        self.email = email
        self.add = add
        self.bal = bal
        self.gender = gender
        self.aadhar =aadhar
        self.transactions = []

    def deposit(self, amount):
        self.bal += amount
        self.transactions.append(f"Credited amount of {amount}")
        self.msg()

    def withdraw(self, amount):
        if self.bal >= amount:
            self.bal -= amount
            self.msg()
            self.transactions.append(f"Debited amount of {amount}")
        else:
            print('In suffiecient Balance')

    def display(self):
        d = self.__dict__
        for attribute, value in d.items():
            print(f"The {attribute} of the customer is {value}")

    def statement(self):
        for transaction in self.transactions:
            print(transaction)

    @staticmethod
    def msg():
        print('Transaction Successfull')

c1 = Bank('steve', 8529637410, 'steve@gmail.com', 'bbsr', 5000, 'Male', 987456321012)


# protected Access Specifiers


class Bank:
    b_name = 'SBI'
    ceo = 'singa'
    mbl = 'Mumbai'

    def __init__(self, name, pno, email, add, bal, gender, aadhar):
        self._name = name
        self._pno = pno
        self._email = email
        self._add = add
        self._bal = bal
        self._gender = gender
        self._aadhar =aadhar
        self._transactions = []

    def deposit(self, amount):
        self._bal += amount
        self._transactions.append(f"Credited amount of {amount}")
        self._msg()

    def withdraw(self, amount):
        if self._bal >= amount:
            self._bal -= amount
            self._msg()
            self.transactions.append(f"Debited amount of {amount}")
        else:
            print('In suffiecient Balance')

    def display(self):
        d = self.__dict__
        for attribute, value in d.items():
            print(f"The {attribute} of the customer is {value}")

    def statement(self):
        for transaction in self.transactions:
            print(transaction)

    @staticmethod
    def _msg():
        print('Transaction Successfull')

c2 = Bank('steve', 8529637410, 'steve@gmail.com', 'bbsr', 5000, 'Male', 987456321012)

    

    


class Bank:
    b_name = 'SBI'
    ceo = 'singa'
    mbl = 'Mumbai'

    def __init__(self, name, pno, email, add, bal, gender, aadhar):
        self.__name = name
        self.__pno = pno
        self.__email = email
        self.__add = add
        self.__bal = bal
        self.__gender = gender
        self.__aadhar =aadhar
        self.__transactions = []

    def deposit(self, amount):
        self.__bal += amount
        self.__transactions.append(f"Credited amount of {amount}")
        self.__msg()

    def withdraw(self, amount):
        if self.__bal >= amount:
            self.__bal -= amount
            self.__msg()
            self.__transactions.append(f"Debited amount of {amount}")
        else:
            print('In suffiecient Balance')

    def display(self):
        d = self.__dict__
        for attribute, value in d.items():
            print(f"The {attribute} of the customer is {value}")

    def statement(self):
        for transaction in self.__transactions:
            print(transaction)

    @staticmethod
    def __msg():
        print('Transaction Successfull')

c3 = Bank('steve', 8529637410, 'steve@gmail.com', 'bbsr', 5000, 'Male', 987456321012)
