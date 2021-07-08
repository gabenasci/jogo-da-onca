import pygame

LARGURA, ALTURA = 600, 900
LINHAS, COLUNAS = 7, 5
TAMANHO_POSICAO = 60#LARGURA//COLUNAS

# RGB
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)

titulo = pygame.transform.scale(pygame.image.load('imagens/titulo.png'), (464, 130))
fundo = pygame.transform.scale(pygame.image.load('imagens/fundo.png'), (600, 996))
madeira = pygame.transform.scale(pygame.image.load('imagens/madeira.png'), (350, 500))
cachorro = pygame.transform.scale(pygame.image.load('imagens/cachorro3.png'), (50, 50))
onca = pygame.transform.scale(pygame.image.load('imagens/onca3.png'), (50, 50))
