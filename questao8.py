class TorneioDeDrones:
    def __init__(self, nome_torneio, provas, bateria_inicial):
        self.nome_torneio = nome_torneio
        self.provas = provas
        self.bateria = bateria_inicial
        self.pontos = 0
        self.provas_concluidas = []

    def listar_provas(self):
        print("Provas disponíveis:")
        for prova in self.provas:
            print(
                f"- Nome: {self.provas['nome']}"
                f"Custo: {self.provas['custo']}"
                f"Pontuação: {self.provas['pontuacao']}"
            )

    def tentar_prova(self, numero_prova):
        if numero_prova < 0 or numero_prova >= len(self.provas):
            print("Erro: número de prova inválido.")
            return

        if numero_prova in self.provas_concluidas:
            print("Essa prova já foi concluída.")
            return

        prova = self.provas[numero_prova]

        if self.bateria >= prova["custo"]:
            self.bateria -= prova["custo"]
            self.pontos += prova["pontuacao"]
            self.provas_concluidas.append(numero_prova)

            print(
                f"Prova '{prova['nome']}' concluída com sucesso! "
                f"+{prova['pontuacao']} pontos."
            )
        else:
            print("Bateria insuficiente para realizar essa prova.")

    def calcular_progresso(self):
        return len(self.provas_concluidas)

    def verificar_situacao(self):
        if len(self.provas_concluidas) == len(self.provas):
            return "Torneio concluído."
        elif self.bateria == 0:
            return "Torneio encerrado sem bateria."
        else:
            return "Torneio em andamento."

    def exibir_relatorio(self):
        print(f"Torneio: {self.nome_torneio}")
        print(f"Bateria restante: {self.bateria}")
        print(f"Pontos: {self.pontos}")
        print(f"Provas concluídas: {self.calcular_progresso()}")
        print(f"Situação: {self.verificar_situacao()}")



drone=TorneioDeDrones("Torneio óvni", "Prova de matemática", 50)
drone.listar_provas()
drone.tentar_prova(2)
drone.calcular_progresso()
drone.verificar_situacao()
drone.exibir_relatorio()