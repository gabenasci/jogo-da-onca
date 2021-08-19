import pygame

from .constantes import PRETO, LINHAS, COLUNAS, TAMANHO_POSICAO, LARGURA, ALTURA, titulo, madeira, fundo, posicoes, \
    iniciar, finalizar, onca, cachorro
from .peca import Peca
from .tabuleiro import Tabuleiro

#JANELA = pygame.display.set_mode((LARGURA, ALTURA))
#pygame.display.set_caption('Jogo da Onça')

class AtorJogador:

    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.posicionar_pecas()
        self.janela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption('Jogo da Onça')
        self.mensagem = ""
        self.placar = 0

    def desenhar_tela(self):
        # desenhar imagem nas coordenadas especificadas da tela
        self.janela.blit(fundo, [0, -120])
        self.janela.blit(titulo, [120, -10])
        self.janela.blit(madeira, [20, 110])
        self.janela.blit(iniciar, [-80, 620])
        self.janela.blit(finalizar, [300, 620])

        pos = 0
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                pos += 1
                self.janela.blit(posicoes[pos], [45 + coluna * TAMANHO_POSICAO, 150 + linha * TAMANHO_POSICAO])

    def desenhar_mensagem(self, mensagem):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 18, bold=True, italic=True)
        mensagem_imagem = font.render(mensagem, True, PRETO)
        self.janela.blit(mensagem_imagem, [50, 565])

    def posicionar_pecas(self):
        for linha in range(LINHAS):
            self.tabuleiro.casas.append([])
            for coluna in range(COLUNAS):
                if linha < 2:
                    self.tabuleiro.casas[linha].append(Peca(linha, coluna, 'cachorro'))
                elif linha == 2 and coluna == 2:
                    self.tabuleiro.casas[linha].append(Peca(linha, coluna, 'onca'))
                elif linha >= 2 and linha < 3 and coluna != 2:
                    self.tabuleiro.casas[linha].append(Peca(linha, coluna, 'cachorro'))
                else:
                    self.tabuleiro.casas[linha].append(0)

    def desenhar_pecas(self):
        self.desenhar_tela()
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                peca = self.tabuleiro.casas[linha][coluna]
                if peca != 0:
                    self.desenhar_peca(self.janela, peca)

    def desenhar_peca(self, janela, peca):
        if peca.tipo == 'onca':
            janela.blit(onca, [peca.x + 15, peca.y + 120])
        elif peca.tipo == 'cachorro':
            janela.blit(cachorro, [peca.x + 20, peca.y + 120])

    def desenhar_placar(self, nro_cachorros):
        self.placar = nro_cachorros

    def mover(self, peca, linha, coluna):
        self.tabuleiro.casas[peca.linha][peca.coluna], self.tabuleiro.casas[linha][coluna] = self.tabuleiro.casas[linha][coluna], self.tabuleiro.casas[peca.linha][peca.coluna]
        peca.mover(linha, coluna)

    def get_linha_coluna_do_mouse(self, pos):
        x, y = pos
        linha = (y - 150) // TAMANHO_POSICAO
        coluna = (x - 45) // TAMANHO_POSICAO
        return linha, coluna
