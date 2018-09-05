class Bank_Account:
    def __init__(self, account_type, amount):
        self.amount = amount
        self.account = account_type

    def deposit(self, deposit_amount):
        self.amount += deposit_amount
        print("${} have been deposited".format(deposit_amount))

    def withdrawal(self, withdraw_amount):
        self.amount -= withdraw_amount
        print("${} have been withdrawn".format(withdraw_amount))

    def __str__(self):
        return "Account type: {}, Amount: {}".format(self.account, self.amount)

richboy = Bank_Account("Chequing", 100)

print(richboy)
richboy.deposit(500)
print("Net Worth = ", richboy.amount)
richboy.withdrawal(100)
print("Net Worth = ", richboy.amount)