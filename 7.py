class Expedicao:
    def __init__(self, nome, energia):
        self.nome = nome
        self.energia = energia
        self.pontos = 0
        self.desafios = []

    def adicionar_desafio(self, desafio):
        self.desafios.append(desafio)

    def listar_desafios(self):
        for desafio in self.desafios:
            print(desafio)

    def superar_desafio(self, nome_desafio):
        for desafio in self.desafios:
            nome, custo, recompensa = desafio.split("/")

            if nome == nome_desafio:
                custo = int(custo)
                recompensa = int(recompensa)

                if self.energia >= custo:
                    self.energia -= custo
                    self.pontos += recompensa
                    print("Desafio superado!")
                else:
                    print("Energia insuficiente!")
                return

        print("Desafio não encontrado!")

    def resumo(self):
        print("Expedição:", self.nome)
        print("Energia:", self.energia)
        print("Pontos:", self.pontos)


exp = Expedicao("Templo Perdido", 50)

exp.adicionar_desafio("ponte quebrada/20/30")
exp.adicionar_desafio("sala escura/15/20")
exp.adicionar_desafio("guardiao antigo/40/80")

exp.listar_desafios()

exp.superar_desafio("ponte quebrada")
exp.superar_desafio("sala escura")

exp.resumo()