""""
1 . Mova o menor disco para a haste não recentemente visitada. 
    Se for o primeiro movimento do jogo, mova o disco menor para
    a haste destino se o número de discos for ímpar, caso contrário,
    mova o disco menor para a haste auxiliar.

2 . Mova o disco disponível (nesse ponto só há um movimento “legal” a ser feito)

3 . Repita os passos 1 e 2 até resolver o problema."""

"""
Recursivamente
Mova os n-1 discos do topo de ORI para AUX, usando DEST como auxiliar.
Mova o disco de baixo de ORI para DEST.
Mova os n-1 discos de AUX para DEST, usando ORI como auxiliar.
"""
class Hanoi:

    def __init__(self):
        pass

    def organizar(self, discos, origem, destino, auxiliar):
        if (discos == 1):
            print 'Mover disco {} de {} para {}'.format(discos, origem, destino)
        else:
            self.organizar(discos - 1, origem, auxiliar, destino)
            print 'Mover disco {} de {} para {}'.format(discos, origem, destino)
            self.organizar(discos - 1, auxiliar, destino, origem)

hanoi = Hanoi()

hanoi.organizar(1, 'pino1', 'pino3', 'pino2')