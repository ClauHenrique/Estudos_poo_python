class DataBase:
    """essa classe fornerce recursos para poder
    armazenar objetos de itens e imprimi-los
    """
    def __init__(self):
        self._items = []

    # adicionar item ao banco
    def addItem(self, theItem):
        self._items.append(theItem)

    def list(self):
        for item in self._items:
            item.print()
            print("") # linha em branco
