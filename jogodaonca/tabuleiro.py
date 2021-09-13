from .jogador import Jogador
from .tipo_jogador import TipoJogador
from .peca import Peca


class Tabuleiro:
    def __init__(self):
        self._casas = [
                [Peca(0, 0, Jogador('', TipoJogador.VAZIA)), Peca(0, 1, Jogador('', TipoJogador.VAZIA)), Peca(0, 2, Jogador('', TipoJogador.VAZIA)), Peca(0, 3, Jogador('', TipoJogador.VAZIA)), Peca(0, 4, Jogador('', TipoJogador.VAZIA))],
                [Peca(1, 0, Jogador('', TipoJogador.VAZIA)), Peca(1, 1,Jogador('', TipoJogador.VAZIA)), Peca(1, 2,Jogador('', TipoJogador.VAZIA)), Peca(1, 3,Jogador('', TipoJogador.VAZIA)), Peca(1, 4, Jogador('', TipoJogador.VAZIA))],
                [Peca(2, 0,Jogador('', TipoJogador.VAZIA)), Peca(2, 1, Jogador('', TipoJogador.VAZIA)), Peca(2, 2, Jogador('', TipoJogador.VAZIA)), Peca(2, 3,Jogador('', TipoJogador.VAZIA)), Peca(2, 4,Jogador('', TipoJogador.VAZIA))],
                [Peca(3, 0,Jogador('', TipoJogador.VAZIA)), Peca(3, 1,Jogador('', TipoJogador.VAZIA)), Peca(3, 2, Jogador('', TipoJogador.VAZIA)), Peca(3, 3,Jogador('', TipoJogador.VAZIA)), Peca(3, 4,Jogador('', TipoJogador.VAZIA))],
                [Peca(4, 0,Jogador('', TipoJogador.VAZIA)), Peca(4, 1, Jogador('', TipoJogador.VAZIA)), Peca(4, 2, Jogador('', TipoJogador.VAZIA)), Peca(4, 3,Jogador('', TipoJogador.VAZIA)), Peca(4, 4,Jogador('', TipoJogador.VAZIA))],
                [Peca(5, 0,Jogador('', TipoJogador.VAZIA)), Peca(5, 1, Jogador('', TipoJogador.VAZIA)), Peca(5, 2,Jogador('', TipoJogador.VAZIA)), Peca(5, 3,Jogador('', TipoJogador.VAZIA)), Peca(5, 4,Jogador('', TipoJogador.VAZIA))],
                [Peca(6, 0,Jogador('', TipoJogador.VAZIA)), Peca(6, 1, Jogador('', TipoJogador.VAZIA)), Peca(6, 2,Jogador('', TipoJogador.VAZIA)), Peca(6, 3,Jogador('', TipoJogador.VAZIA)), Peca(6, 4,Jogador('', TipoJogador.VAZIA))],
                ]
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
    '''
    def get_peca(self, linha, coluna):
        return self.casas[linha][coluna]
    '''

    def get_peca(self, lin, col):
        todas_casas = self.casas
        return todas_casas[lin][col]

    def limpar_tabuleiro(self):
        jogador = Jogador('', TipoJogador.VAZIA)
        for linha in range(7):
            for coluna in range(5):
                self._casas[linha][coluna] = Peca(linha, coluna, jogador)

    def posicionar_pecas_inicio(self):
        self.limpar_tabuleiro()
        jogador = Jogador('', TipoJogador.CACHORRO)
        for linha in range(3):
            for coluna in range(5):
                self._casas[linha][coluna] = Peca(linha, coluna, jogador)
        jogador = Jogador('', TipoJogador.ONCA)
        self._casas[2][2] = Peca(2, 2, jogador)
