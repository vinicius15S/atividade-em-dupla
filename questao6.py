class GaleriaAlienigena:
    def __init__(self, nome_galeria, obras):
        self.nome_galeria = nome_galeria
        self.obras = []
    def adicionar_item(self, nome, valor):
        if nome!='' and valor>0:
            self.obras.update({"nome":nome})
            self.obras.update({"raridade":valor})

        else:
            return "Não foi possível adicionar"
        
    def listar_itens(self):
        print("Obras:")
        for nome in self.obras:
            print(f"{nome}")

    def calcular_total(self):
        for nome in self.obras:
            soma+=self.obras





lista = []
arte=GaleriaAlienigena("Galeria do Vitor", ["mona-lisa", 500])
arte.adicionar_item("Mona-Lisa", 500)
print(arte.obras)
