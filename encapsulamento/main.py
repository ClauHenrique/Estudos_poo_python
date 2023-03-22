from bank_account import BankAccount

user1 = BankAccount("222-77", "Xico Tripa")

# publico
print(user1.client_name)

# nao é permitido acessar o atributo de fora da classe
# user1.balance = 3000

user1.setBalance(100.00)

# sacar
user1.withdrawValue(50.99)

print(user1.getBalance())

print("\n")

x = user1.getAccoount()
print(f""" SUA CONTA
nome: {x['name']}
conta: {x['account']}
saldo: {x['balance']}""")
