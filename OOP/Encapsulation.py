#create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance

class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
    

    def debit(self, amount):
        self.balance = self.balance - amount
        print("Rs.", amount , "was debited")
        self.printing()

    def credit(self, amount):
        if self.balance >= amount:
            self.balance += amount
        print("Rs.", amount , "was Credited")
        self.printing()
    
    def printing(self):
        print("Current balance is ", self.balance)

acc1 = Account(4000, 1)

acc1.debit(400)
acc1.credit(200)
acc1.printing()