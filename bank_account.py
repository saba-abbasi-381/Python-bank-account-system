import time
def log_transaction(func):
        def wrapper_func(self,amount):
            print("Starting transaction...")
            time.sleep(4)
            result = func(self,amount)
            print("Transaction complete")
            return result
        return wrapper_func

class BankAccount:
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance

    def check_balance(self):
        
        if self.balance == 0:
            print("No balance available.")
        else:
            print(f"your current balance is {self.balance}")

    @log_transaction
    def deposite(self,amount):
        self.balance = self.balance + amount
        return self.balance
    
    @log_transaction
    def withdraw(self,amount):
        if amount < 0:
            print("Invalid amount")
        elif self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance = self.balance - amount
            print(f"now your current balance is {self.balance}.")


try:
    name = input("enter name: ")
    balance = int(input("enter balances: "))
    acc1 = BankAccount(name,balance)
    print("Hello! Welcome",acc1.name)

except Exception as e:
    print("Error!",e)
while True:
   
    print("\n1 for check_balance")
    print("2 for deposite")
    print("3 for withdraw")
    print("4 for Exit")

    try:   
        option = int(input("enter your choice: "))
    
        if option == 1:
            acc1.check_balance()
        elif option == 2:
            amount = int(input("enter amount: "))
            acc1.deposite(amount)
        elif option == 3:
            amount = int(input("enter amount: "))
            acc1.withdraw(amount)
        elif option == 4:
            print("Thanks for using")
            break
        else:
            print("Something went wrong!")
    except ValueError:
        print("Invalid input!")