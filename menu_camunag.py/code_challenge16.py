#you will create a function that will breakdown a filipino denomination and then print it 
#Create a python proram that can create banking accounts, with the following information initial deposit, name 
#user can also deposit, withdraw, and every deposit program should be able to deposit, current balance
#program will only terminate if user choose to terminate the program.


import sys
class Bank:
  def __init__(self, name,Bal=0.0):
    self.name=name
    self.Bal=Bal

  def deposit(self,amount):
    self.Bal+=amount
    return self.Bal
    
  def withdraw(self,amount):
    if(amount> self.Bal):
      print("Balance is Less, so no withdraw")
    else:
      self.Bal-=amount
      return self.Bal
    
  def denomination_breakdown(self):
        print("\nDenomination Breakdown:")
        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
        amount = self.Bal
        for denom in denominations:
            count = int(amount // denom)
            if count > 0:
                print(f"{denom}: {count}")
            amount %= denom
        print()
    
name=input("Enter name: ")
B=Bank(name)
while(True):
  print("Enter D-for Deposit")
  print("Enter W-Withdraw")
  print("Enter E-for Exit")
  
  choice=input("Enter your Choice: ")
  if(choice=="e" or choice=="E"):
    sys.exit()
  amt=float(input("Enter amount:"))
  
  if(choice=="d" or choice=="D"):
    print("Balance after Deposit:",B.deposit(amt))
    B.denomination_breakdown()

  elif(choice=="w" or choice=="W" ):
    print("Balance after Withdraw:", B.withdraw(amt))
    B.denomination_breakdown()

  else:
        print("Invalid choice. Please try again.")

  
  
