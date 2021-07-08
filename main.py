import pygame
from jogodaonca.constantes import LARGURA, ALTURA, TAMANHO_POSICAO
from jogodaonca.ator_jogador import AtorJogador
from jogodaonca.tabuleiro import Tabuleiro
from jogodaonca.jogo_controller import JogoController
FPS = 60

JANELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo da Onça')

def get_linha_coluna_do_mouse(pos):
    x, y = pos
    linha = (y-150)//TAMANHO_POSICAO
    coluna = (x-45)//TAMANHO_POSICAO
    return linha, coluna

def main():
    jogo_em_execucao = True
    clock = pygame.time.Clock()
    interface = AtorJogador()
    #tabuleiro = interface.tabuleiro

    jogo = JogoController(JANELA)
    #peca = tabuleiro.get_peca(1, 2)


    while jogo_em_execucao:
        clock.tick(FPS)

        # verificar se ocorreu evento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo_em_execucao = False

            # evento de click botao esquerdo do mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos
                print(pos)
                if x > 45 and x < 395 and y > 150 and y < 650:
                    linha, coluna = get_linha_coluna_do_mouse(pos)
                    jogo.selecionar(linha, coluna)
                    #peca = tabuleiro.get_peca(linha, coluna)
                    #tabuleiro.mover(peca, 4, 2)
                else:
                    print('pos invalida')
        pass
        #interface.desenhar(JANELA)
        #pygame.display.update()
        jogo.update()



main()

