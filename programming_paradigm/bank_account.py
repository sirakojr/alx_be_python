
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    

    def display_balance(self):
        print(f"Current Balance: ${self.__balance}")

# my_account = BankAccount("Alice Smith", 1000)