class balanceExeption(Exception):
    pass

class BankAccount: 
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount '{self.name}' created \nBalance = $'{self.balance:.2f}'")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance '{self.balance:.2f}'")

    def addBalance(self, amount):
        self.balance = self.balance + amount
        print(f"Deposite Complete.")
        self.getBalance()

    def viabletransaction(self, amount):
        if self.balance >= amount:
            return 
        else: 
            raise balanceExeption(f"\nSorry, account '{self.name}' only has an amount of $'{self.balance:.2f}'")

    def withdraw(self, amount):
        try:
            self.viabletransaction(amount)
            self.balance = self.balance - amount
            print(f"withdraw complete.")
            self.getBalance()
        except balanceExeption as error:
            print(f"\nwithdraw interupted: {error}")

    def transfer(self, amount, account):
        try:
            print("Beginning a transfer ")
            self.viabletransaction(amount)
            self.withdraw(amount)
            account.addBalance(amount)
            print("\nTransfer complete\n")

        except balanceExeption as error:
            print(f"\n Transfer interrupted. '{error}'")

# a class that inherets form the BankAccount class 
class IntrestRewardsAccount(BankAccount):
    def addBalance(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\n Deposite complete")
        self.getBalance()

class savingsAccount(IntrestRewardsAccount):
    def __init__(self, initial_Amount, acctName):
        super(). __init__(initial_Amount, acctName)
        self.fee = 5
    def withdraw(self, amount):
        try: 
            self.viabletransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete.")
        except balanceExeption as error:
            print(f'\n Withdraw interupted: {error}')