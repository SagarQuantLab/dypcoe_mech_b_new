class Bank:

    def __init__(self):
        self.account_details = {}

    def open_account(self, account_number, account_holder_details):
        if self.check_for_existence(account_number):
            self.account_details[account_number] = account_holder_details
            return f"Account open for - {account_holder_details['Name']} - {account_number}"
        else:
            raise ValueError(f"Account number already exists - {self.account_details[account_number]['Name']}")

    def delete_account(self, account_number):
        self.account_details.pop(account_number)
        return f"Account deleted for - {self.account_details[account_number]['Name']} - {account_number}"
    
    def check_for_existence(self, account_number):
        account_number_list = list(self.account_details.keys())
        account_status = True
        if account_number in account_number_list:
            account_status = False
        return account_status