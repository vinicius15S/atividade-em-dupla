class TorneioDeDrones:
    def __init__(self, nome_torneio, provas, bateria_inicial):
        self.nome_torneio = nome_torneio
        self.provas = provas
        self.bateria = bateria_inicial
        self.pontos = 0
        self.provas_concluidas = []

    def listar_provas(self):
        print("Provas disponíveis:")
        for i, prova in enumerate(self.provas):
            print(
                f"{i} - Nome: {prova['nome']} | "
                f"Custo: {prova['custo']} | "
                f"Pontuação: {prova['pontuacao']}"
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
        print("\n=== RELATÓRIO DO TORNEIO ===")
        print(f"Torneio: {self.nome_torneio}")
        print(f"Bateria restante: {self.bateria}")
        print(f"Pontos: {self.pontos}")
        print(f"Provas concluídas: {self.calcular_progresso()}")
        print(f"Situação: {self.verificar_situacao()}")
