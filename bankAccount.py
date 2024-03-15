class BankAccount:
    def __init__(self,name,balance=0,interest_rate = 0.2,overdraft_limit=-100):
        self.name = name
        self.balance = balance
        self.transactions = []
        self.interest_rate = interest_rate
        self.is_closed = False
        self.overdraft_limit = overdraft_limit
    def deposit(self, amount):
        if not self.is_closed:
            if amount > 0:
                self.balance += amount
                self.transactions.append(["deposit", amount])
            else:
                print("Invalid deposit amount! Amount must be positive.")
        else:
            print("Account is closed!")
    def withdraw(self,amount):
        if not self.is_closed:
            if amount > 0 and self.balance - amount >= self.overdraft_limit:
                self.balance -= amount
                self.transactions.append(["withdraw", amount])
            else:
                raise ValueError("Invalid withdrawal amount or insufficient funds!")
        else:
            raise ValueError("Account is closed!")

    def get_balance(self):
        if not self.is_closed:
            return self.balance
        print("Account is closed!")
    def print_statement(self):
        if not self.is_closed:
            print("Account's holder name:",self.name)
            print("Account's balance:",self.balance,"\nTransaction history:")
            for transaction in self.transactions:
                print(transaction[0],":",transaction[1])
        else:
            print("Account is closed!")
    def add_interest(self,months):
        if not self.is_closed:
            interest_amount = months * self.interest_rate * self.balance
            self.balance += interest_amount
            self.transactions.append(["interest", interest_amount])
        else:
            print("Account is closed!")
    def transfer_funds(self, recipient,amount):
        if not self.is_closed:
            if not recipient.is_closed:
                if self.balance - amount >= self.overdraft_limit:
                    self.withdraw(amount)
                    recipient.deposit(amount)
                    print(f"Transferred {amount} to {recipient.name}")
                else:
                    print("Insufficient funds! Transfer failed.")
            else:
                print("Recipient's account is closed! Transfer failed.")
        else:
            print("your account is closed! Transfer failed.")
    def close_account(self):
        self.is_closed = True
        print(f"{self.name}'s account is closed.")
        
account = BankAccount("bruce wayne", 1000)
account2 = BankAccount("Peter Parker")
account.deposit(500)
account.withdraw(200)
account.add_interest(3)
account.print_statement()