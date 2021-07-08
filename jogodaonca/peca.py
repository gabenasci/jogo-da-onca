import pygame
from .constantes import VERMELHO, AZUL, TAMANHO_POSICAO, PRETO, onca, cachorro

class Peca:
    PADDING = 10
    BORDA = 2

    def __init__(self, linha, coluna, tipo):
        self.linha = linha
        self.coluna = coluna
        self.tipo = tipo

        self.x = 0
        self.y = 0
        self.calc_pos()

    # Calcular coordenadas x e y da tela referente às linhas/colunas
    def calc_pos(self):
        # tamanho de cada posição * a linha + metade do tamanho da posição pra ser posicionado no meio
        self.x = TAMANHO_POSICAO * self.coluna + TAMANHO_POSICAO // 2
        self.y = TAMANHO_POSICAO * self.linha + TAMANHO_POSICAO // 2

    def draw(self, janela):
        raio = TAMANHO_POSICAO//2 - self.PADDING

        # desenhar circulo com raio acima + tamanho da borda, depois desenhar circulo menor dentro deste maior
        # para desenhar uma peça com borda
        #pygame.draw.circle(win, PRETO, (self.x + 45, self.y + 150), raio + self.BORDA)
        #pygame.draw.circle(win, self.cor, (self.x + 45, self.y + 150), raio)
        if self.tipo == "onca":
            janela.blit(onca, [self.x + 20, self.y + 120])
        elif self.tipo == "cachorro":
            janela.blit(cachorro, [self.x + 20, self.y + 120])

    def mover(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
        self.calc_pos()

    def __repr__(self):
        return str(self.tipo)