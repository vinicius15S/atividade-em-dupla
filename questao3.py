class RoboColetor:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.amostras = []
        self.capacidade = capacidade

    def adicionar_amostra(self, amostra):
        if len(self.amostras) < self.capacidade:
            self.amostras.append(amostra)
            print("Amostra coletada!")
        else:
            print("Armazenamento cheio!")

    def listar_amostras(self):
        print("Amostras coletadas:")
        for amostra in self.amostras:
            print(amostra)

    def armazenamento_cheio(self):
        if len(self.amostras) == self.capacidade:
            return True
        return False


robo = RoboColetor("Explorer", 3)

robo.adicionar_amostra("Rocha")
robo.adicionar_amostra("Areia")
robo.adicionar_amostra("Cristal")
robo.adicionar_amostra("Gás")

robo.listar_amostras()

print("Armazenamento cheio?", robo.armazenamento_cheio())