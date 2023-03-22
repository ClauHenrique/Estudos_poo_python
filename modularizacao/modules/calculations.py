def calculateDiscount(value_products):
    if value_products >= 100:
        return (15 / 100) * value_products

    elif value_products >= 50:
        return (10 / 100) * value_products

    elif value_products >= 20:
        return (5 / 100) * value_products


def calcularFrete(uf):
    """tabela de frete"""
    """ RN: 0.00
        CE, PB, PE, AL SE: 10.00
        MA, PI, BA: 15.00
        ES, RJ, MG: 20.00
        OTHERS: 30.00"""

    if uf == "RN":
        return 0.00

    elif uf == "CE" or uf == "PB" or uf == "PE" or uf == "AL" or uf == "SE":
        return 10.00

    elif uf == "MA" or uf == "PI" or uf == "BA":
        return 15.00

    elif uf == "ES" or uf == "RJ" or uf == "MG":
        return 20.00

    else:
        return 30.00

