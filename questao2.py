class PortalDimensional:
    def __init__(self, nome, destino, energia_necessaria, energia_disponivel):
        self.nome = nome
        self.destino = destino
        self.energia_necessaria = energia_necessaria
        self.energia_disponivel = energia_disponivel
    def pode_abrir(self):
        if self.energia_disponivel>=self.energia_necessaria:
            print("Pode abrir")
        else:
            falta=self.energia_necessaria-self.energia_disponivel
            print(f"Não pode abrir, ainda faltam {falta} de energia")
    def classificar_estabilidade(self):
        faltam=self.energia_necessaria-self.energia_disponivel
        if faltam<=0:
            print("Portal estável")
        elif faltam>0 and faltam<20:
            print("Portal quase estável")
        else:
            print("Portal instável")
    def exibir_resumo(self):
        print(f"nome:{self.nome} destino:{self.destino} energia disponível:{self.energia_disponivel} energia necessária:{self.energia_necessaria} ")
    

portal= PortalDimensional("Portal masmorra", "masmorra", 100, 50)

portal.pode_abrir()
portal.classificar_estabilidade()
portal.exibir_resumo()
