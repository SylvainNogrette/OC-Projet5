class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount: float):
        if amount + balance < 0:
            print("You cannot withdraw more money than you have")
        else:
            self.balance += amount
    def withdraw(self, amount: float):
        if amount < self.balance:
            self.balance -= amount
            return
        else:
            print("You cannot withdraw more money than you have")
    def display_balance(self):
        print(self.balance)

# Point d'amélioration faire un décorateur qui vérifie que le résultat de withdraw et deposit est positif