import pygame

from .constantes import PRETO, BRANCO, VERMELHO, AZUL, LINHAS, COLUNAS, TAMANHO_POSICAO, LARGURA, ALTURA, titulo, madeira, fundo, posicoes
from .peca import Peca
from .tabuleiro import Tabuleiro



class AtorJogador:

    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.posicionar_pecas()

    def desenhar_tela(self, janela):
        # colocar imagem nas coordenadas especificadas da tela
        janela.blit(fundo, [0, 0])
        janela.blit(titulo, [80, -10])
        janela.blit(madeira, [20, 140])

        pos = 0
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                pos += 1
                janela.blit(posicoes[pos], [45 + coluna * TAMANHO_POSICAO, 150 + linha * TAMANHO_POSICAO])


    def posicionar_pecas(self):
        for linha in range(LINHAS):
            self.tabuleiro.casas.append([])
            for coluna in range(COLUNAS):
                if linha < 2:
                    #tabuleiro.append_casas(Peca(linha, coluna, "cachorro"), linha)
                    self.tabuleiro.casas[linha].append(Peca(linha, coluna, "cachorro"))
                elif linha == 2 and coluna == 2:
                    self.tabuleiro.casas[linha].append(Peca(linha, coluna, "onca"))
                elif linha >= 2 and linha < 3 and coluna != 2:
                    self.tabuleiro.casas[linha].append(Peca(linha, coluna, "cachorro"))
                else:
                    self.tabuleiro.casas[linha].append(0)



    def desenhar(self, janela):
        self.desenhar_tela(janela)
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                peca = self.tabuleiro.casas[linha][coluna]
                if peca != 0:
                    peca.draw(janela)

    def mover(self, peca, linha, coluna):
        self.tabuleiro.casas[peca.linha][peca.coluna], self.tabuleiro.casas[linha][coluna] = self.tabuleiro.casas[linha][coluna], self.tabuleiro.casas[peca.linha][peca.coluna]
        peca.mover(linha, coluna)
