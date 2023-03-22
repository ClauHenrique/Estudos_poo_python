class Product:
    # variavel da classe
    # o desconto vale pra todas as instancias que usam essa classe
    discount = 5

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def buy(self, discount=0):
        print(f"voce comprou {self.name} por {self.__price - discount:.2f}")

    @classmethod
    def setDiscount(cls, discount=0):
        cls.discount = discount


product1 = Product("cadeira", 50.99)

product2 = Product("oculos", 200.0)

# com desconto de 5.00
product1.buy(Product.discount)

# alterando valor do desconto
Product.setDiscount(20)

product1.buy(Product.discount)
product2.buy(Product.discount)

