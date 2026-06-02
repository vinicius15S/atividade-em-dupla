class CofreDragao:
    def __init__(self):
        self.tesouros = []

    def adicionar_tesouro(self, tesouro):
        self.tesouros.append(tesouro)

    def listar_tesouros(self):
        for tesouro in self.tesouros:
            print(tesouro)

    def valor_total(self):
        total = 0
        for tesouro in self.tesouros:
            nome, valor = tesouro.split(":")
            total += int(valor)
        return total

    def mais_valioso(self):
        maior = self.tesouros[0]

        for tesouro in self.tesouros:
            nome1, valor1 = tesouro.split(":")
            nome2, valor2 = maior.split(":")

            if int(valor1) > int(valor2):
                maior = tesouro

        return maior

    def classificar_riqueza(self):
        total = self.valor_total()

        if total < 500:
            print("Cofre pobre")
        elif total <= 1000:
            print("Cofre rico")
        else:
            print("Cofre lendário")


cofre = CofreDragao()

cofre.adicionar_tesouro("coroa:500")
cofre.adicionar_tesouro("anel:120")
cofre.adicionar_tesouro("espada:300")

print("Tesouros:")
cofre.listar_tesouros()

print("Valor total:", cofre.valor_total())
print("Mais valioso:", cofre.mais_valioso())

cofre.classificar_riqueza()