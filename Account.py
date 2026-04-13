from Bank import Bank

class Account(Bank):

    def deposit(self, account_number, amount):
        if not self.check_for_existence(account_number):
            self.account_details[account_number]['Balance'] += amount
            return f"Amount deposited - Balance - {self.account_details[account_number]['Balance']}"
        else:
            raise ValueError("Account doesn't exists")