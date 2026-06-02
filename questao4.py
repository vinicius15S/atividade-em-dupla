class MochilaDeMissao:
    def __init__(self, agente, equipamentos, capacidade_maxima):
        self.agente = agente
        self.equipamentos = equipamentos
        self.capacidade_maxima = capacidade_maxima

    def adicionar_equipamento(self, equipamento):
        if equipamento!= "" and len(self.equipamentos)<self.capacidade_maxima:
            self.equipamentos.append(equipamento)
            print(f"Equipamento '{equipamento}' adicionado com sucesso.")
        else:
            print("Não foi possível adicionar o equipamento.")

    def listar_equipamentos(self):
        print("Equipamentos na mochila:")
        for equipamento in self.equipamentos:
            print(f"{equipamento}")

    def contar_equipamentos(self):
        return len(self.equipamentos)

    def verificar_espaco(self):
        if len(self.equipamentos) >= self.capacidade_maxima:
            print("A mochila está cheia.")
        else:
            print("A mochila ainda possui espaço.")

    def exibir_relatorio(self):
        print(f"Agente: {self.agente}")
        print(f"Quantidade de equipamentos: {self.contar_equipamentos()}")
        print(f"Capacidade máxima: {self.capacidade_maxima}")
        print(f"Situação: {self.verificar_espaco()}")



mochila = MochilaDeMissao( "Agente 007", ["Rádio", "Lanterna"], 4)

mochila.adicionar_equipamento("Mapa")
mochila.adicionar_equipamento("Binóculo")

mochila.listar_equipamentos()
print(f"Total de equipamentos: {mochila.contar_equipamentos()}")
print(mochila.verificar_espaco())

mochila.exibir_relatorio()