class Bank:
    def __init__(self):#Default class constructor
        self.balance=100.0
    def registerCustomer(self):
        self.accountNo=input("Enter account number\n")
        self.accountName=input("Enter account Name\n")
        self.branch=input("Enter branch\n")
    def depCash(self):
        self.deposit=float(input("Enter amount to deposit\n"))
        #update balance
        self.balance+=self.deposit
    def withdrawlCash(self):
        self.withdraw=float(input("Enter amount to withdraw\n"))
        self.balance-=self.withdraw
    def checkBalance(self):
        print(f"Your bank balance for account\t{self.accountNo}:-{self.accountName}\tis:\t{self.balance}\n")
#display menu
userChoice=1
b=Bank()
while userChoice==1 or userChoice==2 or userChoice==3 or userChoice==4:
    print("\t\t\tBank Operations\n")
    print("\t\t1.Create Account\n")
    print("\t\t2.Deposit cash\n")
    print("\t\t3.Withdraw Cash\n")
    print("\t\t4.Check Balance\n")
    print("\t\t5.Exit\n")
    userChoice=int(input("Select your choice\n"))
#Create Class object
    
    if userChoice==1:
        b.registerCustomer()
    elif userChoice==2:
        b.depCash()
    elif userChoice==3:
        b.withdrawlCash()
    elif userChoice==4:
        b.checkBalance()
    elif userChoice==5:
        exit