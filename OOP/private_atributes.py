class Account:

    def __init__(self,name, account_no, balance, password):
        self.name = name
        self.account_no = account_no
        self.__balance = balance
        self.__password = password
    


member1 = Account("junaid",1,1000,1234)

print(member1.name) # public attributes
print(member1.__password) # private attributes
