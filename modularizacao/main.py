from modularizacao.model.dataBase import DataBase
from modularizacao.store import store
from modules.calculations import calculateDiscount, calcularFrete
from modules.getCep import getCEP


# criar um objeto que receberá uma instancia do banco de dados
products = DataBase()
exibProducts = products.getProducts()

print("LOJA VIRTUAL:\n")

for item in exibProducts:
    print(f'{item["name"]} => {item["price"]:.2f}R$ || Em estoque: {item["quantidade_estoque"]}')

# informar nome do cliente e seu cep
client1 = store.Client("claudio", "20031900")

# comprar produto
client1.buy("calça", 10.50, 2)
products.removeProductFromDataBase(2, 2) # dar baixa no produto id 2 do banco de dados

client1.buy("cadeira", 20.99, 1)
products.removeProductFromDataBase(1, 1) # dar baixa no produto id 1 do banco de dados

print("\n")
print("#" * 30)

try:
    print("SEU CARRINHO:")
    exibCarrinho = client1.exibirCompras()

    for item in exibCarrinho:
        if "valor_total" not in item:
            print(f'{item["produto"]} => {item["preco"]:.2f}R$ | quantidade: {item["quantidade"]}')

        else:
            print("\nO VALOR DE SUAS COMPRAS SERÁ:")
            value = float(item["valor_total"])

            print(f'--{value}--')
            discount = calculateDiscount(value)

            cep = getCEP(client1.getCep()) # cidade, uf

            valor_do_frete = calcularFrete(cep[1])

            print(f"com {discount:.2f}% de desconto ficam: \n {value - discount:.2f}RS + "
                  f"{valor_do_frete:.2f}R$ de frete para {cep[0]} - CEP {client1.getCep()}")

except:
    print("cep invalido!!!")

print("#" * 30)
