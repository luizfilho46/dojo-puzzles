class CaixaEletronico:
    def __init__(self):
        self.notas = [100, 50, 20, 10]

    def sacar(self, valor):
        
        self.valor_restante = valor
        self.notas_sacadas = []

        for nota in self.notas:
            quantidade = self.valor_restante / nota
            self.valor_restante = self.valor_restante % nota
            self.notas_sacadas.append(quantidade)

        return self.notas_sacadas