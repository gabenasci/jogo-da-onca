
class Tabuleiro:
    def __init__(self):
        self._casas = []
        self.jogadores = []
        #self.peca_selecionada = None
        self.cachorros = 14

    @property
    def casas(self):
        return self._casas

    @casas.setter
    def casas(self, val):
        self._casas = val

    def mover(self, peca, linha, coluna):
        self.casas[peca.linha][peca.coluna], self.casas[linha][coluna] = self.casas[linha][coluna], self.casas[peca.linha][peca.coluna]
        peca.mover(linha, coluna)

    def get_peca(self, linha, coluna):
        return self.casas[linha][coluna]