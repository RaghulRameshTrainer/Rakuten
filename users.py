from bank import Account

acc=Account('Raghul','Ramesh','ARGTH6566R',10000)
print("Current Balance:",acc._Account__balance)
print("User ID:", acc.userid)
print("Password:",acc.password)

acc._Account__balance=10000000
print("Current Balance:",acc._Account__balance)

# print("Balance is :",acc.getBalance())
# acc.setBalance(10000)
# print("New Balance is :",acc.getBalance())
