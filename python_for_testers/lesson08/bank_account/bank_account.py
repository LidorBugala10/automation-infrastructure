class BankAccount:
    def __init__(self,balance,account_fee):
        self.balance = balance
        self.account_fee = account_fee
    def withdraw(self,amount):
        if self.balance >= amount+self.account_fee:
            self.balance -= (amount+self.account_fee)
            print(f"Success.new balance : {self.balance}")
        else :
            print("Insufficient funds")
            