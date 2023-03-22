import requests


def getCEP(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"

        res = requests.get(url)
        data = res.json()

        if res.status_code == 200:
            return data["localidade"], data["uf"]

    except:
        raise ValueError("cep nao encontrado", "status: 404")

