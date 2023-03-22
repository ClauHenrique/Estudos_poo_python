class DataBase:
    def __init__(self):
        self.__products = [
    {
        "id": 1,
        "name": "cadeira",
        "price": 20.99,
        "quantidade_estoque": 2
    },
    {
        "id": 2,
        "name": "calça",
        "price": 10.50,
        "quantidade_estoque": 5
    },
    {
        "id": 3,
        "name": "computador",
        "price": 2500.00,
        "quantidade_estoque": 2
    }
]

    def getProducts(self):
        return self.__products

    def removeProductFromDataBase(self, id, quant):
        for index, item in enumerate(self.__products):
            if item["id"] == id:
                if item["quantidade_estoque"] - quant >= 0:
                    item["quantidade_estoque"] -= quant
                else:
                    raise Exception("a quantidade em estoque nao pode ser negativo")

