import pygame

from .constantes import PRETO, BRANCO, VERMELHO, AZUL, LINHAS, COLUNAS, TAMANHO_POSICAO, LARGURA, ALTURA, titulo, madeira, fundo
from .peca import Peca
from .tabuleiro import Tabuleiro



class AtorJogador:

    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.posicionar_pecas()


    def desenhar_tela(self, janela):
        # carregar imagens

        # redimensionar imagem madeira para 300x395
        #madeira = pygame.transform.scale(madeira, (350, 500))
        #titulo = pygame.transform.scale(titulo, (464, 130))

        # colocar imagem nas coordenadas especificadas da tela
        janela.blit(fundo, [0, 0])
        janela.blit(titulo, [80, -10])
        janela.blit(madeira, [20, 140])

        # ---------- IMAGENS TABULEIRO ------------
        pos1 = pygame.image.load('imagens/tabuleiro/1.png')
        pos2 = pos4 = pygame.image.load("imagens/tabuleiro/2-4.png")
        pos3 = pygame.image.load("imagens/tabuleiro/3.png")
        pos5 = pygame.image.load("imagens/tabuleiro/5.png")
        pos6 = pos16 = pygame.image.load('imagens/tabuleiro/6-16.png')
        pos7 = pos9 = pos13 = pos17 = pos19 = pos23 = pygame.image.load('imagens/tabuleiro/7-9-13-17-19-23.png')
        pos8 = pos12 = pos14 = pos18 = pos28 = pygame.image.load('imagens/tabuleiro/8-12-14-18-28.png')
        pos10 = pos20 = pygame.image.load('imagens/tabuleiro/10-20.png')
        pos11 = pygame.image.load('imagens/tabuleiro/11.png')
        pos15 = pygame.image.load('imagens/tabuleiro/15.png')
        pos21 = pygame.image.load('imagens/tabuleiro/21.png')
        pos22 = pos24 = pos33 = pygame.image.load('imagens/tabuleiro/22-24-33.png')
        pos25 = pygame.image.load('imagens/tabuleiro/25.png')
        pos26 = pos30 = pygame.image.load('imagens/tabuleiro/26-30.png')
        pos27 = pygame.image.load('imagens/tabuleiro/27.png')
        pos29 = pygame.image.load('imagens/tabuleiro/29.png')
        pos31 = pygame.image.load('imagens/tabuleiro/31.png')
        pos32 = pos34 = pygame.image.load('imagens/tabuleiro/32-34.png')
        pos35 = pygame.image.load('imagens/tabuleiro/35.png')

        posicoes = {
            1: pos1, 2: pos2, 3: pos3, 4: pos4, 5: pos5, 6: pos6, 7: pos7, 8: pos8, 9: pos9, 10: pos10,
            11: pos11, 12: pos12, 13: pos13, 14: pos14, 15: pos15, 16: pos16, 17: pos17, 18: pos18, 19: pos19, 20: pos20,
            21: pos21, 22: pos22, 23: pos23, 24: pos24, 25: pos25, 26: pos26, 27: pos27, 28: pos28, 29: pos29, 30: pos30,
            31: pos31, 32: pos32, 33: pos33, 34: pos34, 35: pos35
        }
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
