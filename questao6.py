class GaleriaAlienigena:
    def __init__(self, nome_galeria, obras):
        self.nome_galeria = nome_galeria
        self.obras = []

    def adicionar_item(self, nome, valor):
        if nome!='' and valor>0:
            self.obras.append({"nome":nome, "raridade": valor})
        else:
            return "Não foi possível adicionar"
        
    def listar_itens(self):
        i=0
        print("Obras:")
        while i<len(self.obras):
            print(f"{self.obras[i]}")
            i+=1

    def calcular_total(self):
        total = 0
        for obra in self.obras:
            obra=self.obras[valor]
            total+=obra
            return total



lista = []
arte=GaleriaAlienigena("Galeria do Vitor", lista)
arte.adicionar_item("Mona-Lisa", 600)
arte.listar_itens()
arte.calcular_total()


