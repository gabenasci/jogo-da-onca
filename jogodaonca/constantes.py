import pygame

LARGURA, ALTURA = 600, 720
LINHAS, COLUNAS = 7, 5
TAMANHO_POSICAO = 60

# RGB
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)

titulo = pygame.transform.scale(pygame.image.load('imagens/titulo.png'), (379, 100))
fundo = pygame.transform.scale(pygame.image.load('imagens/fundo.png'), (600, 996))
madeira = pygame.transform.scale(pygame.image.load('imagens/madeira.png'), (350, 500))
cachorro = pygame.transform.scale(pygame.image.load('imagens/cachorro3.png'), (50, 50))
onca = pygame.transform.scale(pygame.image.load('imagens/onca3.png'), (60, 60))
iniciar = pygame.transform.scale(pygame.image.load('imagens/iniciar.png'), (379, 100))
finalizar = pygame.transform.scale(pygame.image.load('imagens/finalizar.png'), (379, 100))
placar = pygame.transform.scale(pygame.image.load('imagens/cemiterio.png'), (83, 310))

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