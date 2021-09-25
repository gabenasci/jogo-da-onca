import pygame

from .constantes import PRETO, LINHAS, COLUNAS, TAMANHO_POSICAO, LARGURA, ALTURA, titulo, madeira, fundo, posicoes, \
    iniciar, finalizar, onca, cachorro, placar
from .tabuleiro import Tabuleiro
from .tipo_jogador import TipoJogador

class InterfaceJogador:

    def __init__(self, ref):
        from .jogo import Jogo
        assert isinstance(ref, Jogo)
        self.jogo = ref
        self.tabuleiro = Tabuleiro()
        self.posicionar_pecas()
        self.janela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption('Jogo da Onça')

    def click(self):
        jogo_em_execucao = True
        clock = pygame.time.Clock()
        FPS = 60
        while jogo_em_execucao:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jogo_em_execucao = False
                    pygame.quit()
                    exit()


                # evento de click botao esquerdo do mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x, y = pos
                    #print(pos)

                    print(self.tabuleiro.casas)

                    # clique no botão iniciar partida
                    if x > 28 and x < 191 and y > 620 and y < 699:
                        self.jogo.iniciar()

                    # clique no tabuleiro
                    elif x > 45 and x < 345 and y > 150 and y < 570:
                        if self.jogo.partida_em_andamento:
                            linha, coluna = self.jogo.interface.get_linha_coluna_do_mouse(pos)
                            self.jogo.selecionar_peca(linha, coluna)
                            print(self.jogo.jogada)

                        else:
                            self.jogo.mensagem("Partida deve ser iniciada primeiro")

                    # clique no botão finalizar partida enquanto partida em andamento
                    elif x > 409 and x < 570 and y > 620 and y < 699 and self.jogo.partida_em_andamento == True:
                        self.jogo.finalizar()

            if self.jogo.partida_em_andamento:
                self.jogo.posicionar_pecas()
                self.jogo.atualizar_placar(self.jogo._validador.cachorros_comidos)
                if self.jogo.verificar_vencedor():
                    self.jogo.finalizar()
            else:
                self.jogo.desenhar_tela()


    def desenhar_tela(self):
        # desenhar imagem nas coordenadas especificadas da tela
        self.janela.blit(fundo, [0, -120])
        self.janela.blit(titulo, [120, -10])
        self.janela.blit(madeira, [20, 110])
        self.janela.blit(iniciar, [-80, 620])
        self.janela.blit(finalizar, [300, 620])
        self.janela.blit(placar, [380, 300])

        pos = 0
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                pos += 1
                self.janela.blit(posicoes[pos], [45 + coluna * TAMANHO_POSICAO, 150 + linha * TAMANHO_POSICAO])

    def atualizar_interface(self):
        pygame.display.update()

    def desenhar_mensagem(self, mensagem):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 18, bold=True, italic=True)
        mensagem_imagem = font.render(mensagem, True, PRETO)
        self.janela.blit(mensagem_imagem, [50, 565])

    def tempo_mensagem(self):
        pygame.time.wait(1000)

    def posicionar_pecas(self):
        self.tabuleiro.posicionar_pecas_inicio()

    def desenhar_pecas(self):
        self.desenhar_tela()
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                peca = self.tabuleiro._casas[linha][coluna]
                if peca != 0:
                    self.desenhar_peca(self.janela, peca)

    def desenhar_peca(self, janela, peca):
        if peca.jogador.tipo == TipoJogador.ONCA:
            janela.blit(onca, [peca.x + 15, peca.y + 120])
        elif peca.jogador.tipo == TipoJogador.CACHORRO:
            janela.blit(cachorro, [peca.x + 20, peca.y + 120])
        else:
            pass

    def desenhar_placar(self, cachorros_comidos):
        y = 320
        for placar in range(cachorros_comidos):
            self.janela.blit(cachorro, [395, y])
            y += 55

    def mover(self, peca, linha, coluna):
        self.tabuleiro.casas[peca.linha][peca.coluna], self.tabuleiro.casas[linha][coluna] = self.tabuleiro.casas[linha][coluna], self.tabuleiro.casas[peca.linha][peca.coluna]
        peca.mover(linha, coluna)

    def get_linha_coluna_do_mouse(self, pos):
        x, y = pos
        linha = (y - 150) // TAMANHO_POSICAO
        coluna = (x - 45) // TAMANHO_POSICAO
        return linha, coluna
