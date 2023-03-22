class Product:
    def __init__(self, name, price, quant):
        self.__name = name
        self.__price = price
        self.__quant = quant # quantidade que deseja comprar

    def getPrice(self):
        return self.__price

    def getProduct(self):
        return self.__name, self.__price, self.__quant


class Carrinho:
    def __init__(self):
        self.__amount = 0 # valor das compras
        self.__carrinho = []


    def exibirValorCompras(self):
        return self.__amount

    def exibirCarrinho(self):
        return self.__carrinho

    def addProduct(self, product: Product, quant: int):
        price = product.getPrice()
        value = self.__calculateValue(price, quant)

        self.__amount += value
        self.__carrinho.append(product)

    def __calculateValue(self, valueProduct, quant):
        return valueProduct * quant


class Client:
    def __init__(self, name, cep):
        self.__name = name
        self.__cep = cep
        self.__myCarrinho = Carrinho()

    def getCep(self):
        return self.__cep

    def buy(self, name, price, quant):
        myProduct = Product(name, price, quant)

        self.__myCarrinho.addProduct(myProduct, quant)

    def exibirCompras(self):
        carrinho = [] # adicionar m dicionario para cada item
        valor_compra = f"{ self.__myCarrinho.exibirValorCompras():.2f}"

        for i in self.__myCarrinho.exibirCarrinho():
            carrinho.append(
                {"produto": i.getProduct()[0],
                 "preco": i.getProduct()[1],
                 "quantidade": i.getProduct()[2]})

        carrinho.append({"valor_total": valor_compra})
        return carrinho
