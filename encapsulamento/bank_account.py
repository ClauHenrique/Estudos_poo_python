class BankAccount:
    def __init__(self, account, client_name):
        self.__account = account # privado
        self.client_name = client_name # publico
        self.__balance = 0 # privado

    def getBalance(self):
        return self.__balance

    def setBalance(self, value):
        self.__balance = value

    # sacar valor
    def withdrawValue(self, value):
        if self.__balance - value >= 0:
            self.__balance -= value

        else:
            print("Saldo insuficiente para a operacao")

    # depositar valor
    def depositValue(self, value):
        self.__balance += value

    def getAccoount(self):
        return {"name": self.client_name, "account": self.__account, "balance": self.__balance}

    # impedir o acesso ao atribudo balance
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        raise ValueError("acesso negado ao atributo. "
                         "Utilize os metodos setBalance(), depositValue(), withdrawValue()")
