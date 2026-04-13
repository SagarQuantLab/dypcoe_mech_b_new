from Bank import Bank
from Account import Account

actIns = Account()
account_holder_details = {'Name':'Payal', 'Age':21, 'Gender':'Female', 'Account_type':'Savings', 'Balance':10000}
account_number = 123456789
print(actIns.open_account(account_number, account_holder_details))
account_holder_details = {'Name':'Bhakti', 'Age':20, 'Gender':'Female', 'Account_type':'Current', 'Balance':5000}
account_number = 123456788
print(actIns.open_account(account_number, account_holder_details))

print(actIns.deposit(123456789, 5000))
print(actIns.deposit(123456780, 5000))

