from classes import Cd, Video, Game
from model.dataBase import DataBase

# instanciar meu banco de dados
DB = DataBase()

# adicionar objetos que herdam da classe item

cd1 = Cd("Depois da guerra", "1.40.20", 'heavy metal dos bons', "oficina G3", 10)
cd1.setOwn(True) # especificar se tenho esse album em minha colecao
DB.addItem(cd1)

cd2 = Cd("full concert", "1.54.56", "blues do bom", "Erick Clapton", 10)
DB.addItem(cd2)

video1 = Video("Curso POO", "10.00.00",
               "aulas com o professor que lhe ensina de tudo", "Gustavo Guanabara")
video1.setOwn(True)
DB.addItem(video1)

game1 = Game("call of duty", "infinito", "jogo de ação", "mutiplos")
DB.addItem(game1)


# exibir todos os itens armazenados no banco
DB.list()

