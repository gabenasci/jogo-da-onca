import pygame
import os

from .constantes import PRETO, BRANCO, VERMELHO, AZUL, LINHAS, COLUNAS, TAMANHO_POSICAO, LARGURA, ALTURA
from .peca import Peca

class Tabuleiro:
    def __init__(self):
        self._casas = []
        self.jogadores = []
        self.jogada_da_vez = 0
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

    def append_casas(self, peca, linha):
        self._casas[linha].append(peca)
