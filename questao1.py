 class Capsuladotempo:
    def __init__(self, autor, mensagem, ano_abertura, ano_atual):
        self.autor = autor
        self.mensagem = mensagem
        self.ano_abertura = ano_abertura
        self.ano_atual = ano_atual

    def pode_abrir(self):
        return self.ano_atual >= self.ano_abertura

    def calcular_espera(self):
        return self.ano_abertura - self.ano_atual

    def classificar_espera(self):
        espera = self.calcular_espera()

        if espera == 0:
            print("pode abrir agora")
        elif 1 <= espera <= 3:
            print("espera curta")
        else:
            print("espera longa")

    def situacao_capsula(self):
        if self.pode_abrir():
            return "aberta"
        else:
            return "fechada"

    def exibir_resumo(self):
        print("Autor:", self.autor)
        print("Ano de abertura:", self.ano_abertura)
        print("Situação:", self.situacao_capsula())

capsula = Capsuladotempo("Arthur", "oi", 2027, 2027)

capsula.exibir_resumo()

if capsula.pode_abrir():
    print("capsula aberta dentro vc encontra algumas fotos, ahhh essa nostalgia... como o tempo passa")
else:
    print("a capsula se fecha nao esta na hora ainda")

capsula.classificar_espera()