
from .constantes import TAMANHO_POSICAO

class Peca():

    def __init__(self, linha, coluna, jogador):
        self.linha = linha
        self.coluna = coluna
        self.jogador = jogador

        self.x = 0
        self.y = 0
        self.calc_pos()

    # Calcular coordenadas x e y da tela referente às linhas/colunas
    def calc_pos(self):
        # tamanho de cada posição * a linha + metade do tamanho da posição pra ser posicionado no meio
        self.x = TAMANHO_POSICAO * self.coluna + TAMANHO_POSICAO // 2
        self.y = TAMANHO_POSICAO * self.linha + TAMANHO_POSICAO // 2

    def mover(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
        self.calc_pos()

    def __repr__(self):
        return str(self.jogador.tipo)