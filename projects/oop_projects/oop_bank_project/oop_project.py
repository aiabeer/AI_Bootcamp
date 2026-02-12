from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Abeer = BankAccount(89, "Abeer")

Dave.getBalance()
Abeer.getBalance()

Dave.addBalance(30)
Abeer.withdraw(900)

Dave.withdraw(5)
Dave.transfer(100, Abeer)

Dave.transfer(950, Abeer)

Jim = IntrestRewardsAccount(1000, "Jim")
Jim.getBalance()
Jim.addBalance(100)
Jim.transfer(1100, Abeer)

mimi = savingsAccount(1000, "mimi")
mimi.getBalance()
mimi.addBalance(100)
mimi.transfer(1000, Abeer)