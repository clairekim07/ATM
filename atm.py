import os
import shutil

class atm:
    def __init__(self,carNum,pinNum,balance):
        self.carNum = carNum
        self.pinNum = pinNum
        self.balance = balance
    def cashWithdrawl(self):
        money=input("Enter the amount you want to withdraw: ")
        if money >= self.balance:
            print("Enter a number that is within your balance: ")
            money=input("Enter the amount you want to withdraw: ")
        else:
            withD = int(self.balance)-int(money)
            print(withD)
    def getBalance(self):
        print(self.balance)

    def cashDeposit(self):
        give=input("Enter the amount you want to deposit: ")
        deposit = int(self.balance)+int(give)
        print(deposit)
carNumber = input("Enter your card number: ")
pinNumber = input("Enter your pin number: ")
bal = input("Enter your balance: ")
returning = atm(carNumber,pinNumber,bal)
returning.cashWithdrawl()
returning.getBalance()
returning.cashDeposit()
returning.getBalance()
print(returning)