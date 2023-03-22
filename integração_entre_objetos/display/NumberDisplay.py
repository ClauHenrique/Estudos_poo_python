class NumberDisplay:
    def __init__(self, limit):
        self.limit = limit
        self.value = 0

    def getValue(self):
        return self.value

    # configura o valor do mostrador
    def setValue(self, replaceValue):
        if replaceValue >= 0 and replaceValue < self.limit:
            self.value = replaceValue

    # retorna o valor do mostrador como uma istring
    def getDisplayValue(self):
        if int(self.value) < 10:
            return "0" + str(self.value)

        else:
            return "" + str(self.value)

    # incrementar o valor do mostrador
    def increment(self):
        self.value = int(self.value)
        self.value = (self.value + 1) % self.limit

