import pygame

from .ator_jogador import AtorJogador
from .peca import Peca

class Jogo:
    def __init__(self):
        self._interface = AtorJogador()
        self._init()
        #self.janela = janela

    def _init(self):
        self._peca_a_mover = None
        self._tabuleiro = self._interface.tabuleiro
        self._turno = 'onca'
        self._partida_em_andamento = False
        self._vencedor = None
        self._jogada = []
        self._numero_cachorros = 14

    def iniciar(self):
        self._partida_em_andamento = True
        self.posicionar_pecas()

    def finalizar(self):
        self._init()


    def eventos(self):
        jogo_em_execucao = True
        clock = pygame.time.Clock()
        FPS = 60
        while jogo_em_execucao:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jogo_em_execucao = False


                # evento de click botao esquerdo do mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x, y = pos
                    #print(pos)

                    print(self.tabuleiro.casas)

                    # clique no botão iniciar partida
                    if x > 28 and x < 191 and y > 620 and y < 699:
                        self.iniciar()
                        self.mensagem("Partida iniciada")

                    # clique no tabuleiro
                    elif x > 45 and x < 345 and y > 150 and y < 570:
                        if self.partida_em_andamento:
                            linha, coluna = self._interface.get_linha_coluna_do_mouse(pos)
                            self.selecionar_peca(linha, coluna)
                            print(self.jogada)
                        else:
                            self.mensagem("Partida deve ser iniciada primeiro")

                    # clique no botão finalizar partida enquanto partida em andamento
                    elif x > 409 and x < 570 and y > 620 and y < 699 and self.partida_em_andamento == True:
                        if len(self.jogada) > 2:
                            self.finalizar()
                            self.mensagem("Partida finalizada")
                        else:
                            self.mensagem("Finaliza o lance primeiro")

            if self.partida_em_andamento:
                self.posicionar_pecas()
            else:
                self.desenhar_tela()


    def desenhar_tela(self):
        self._interface.desenhar_tela()
        pygame.display.update()

    def posicionar_pecas(self):
        self._interface.desenhar_pecas()
        pygame.display.update()

    def mensagem(self, str):
        self._interface.desenhar_mensagem(str)
        pygame.display.update()
        pygame.time.wait(700)

    def selecionar_peca(self, linha, coluna):
        if not self._peca_a_mover:
            peca_clicada = self._tabuleiro.get_peca(linha, coluna)
            if peca_clicada != 0: #and self._turno == peca_clicada.tipo:
                self._peca_a_mover = peca_clicada
                self._jogada = []
                self.jogada.append(peca_clicada)
                self.jogada.append([linha, coluna])
            else:
                self.mensagem("Turno errado")
        else:
            casa_vazia = self._mover(linha, coluna)
            if not casa_vazia:
                self._peca_a_mover = None
                self.selecionar_peca(linha, coluna)

    def atualizar_placar(self):
        cachorros_comidos = 14 - self._numero_cachorros
        self._interface.desenhar_placar(cachorros_comidos)

    def _mover(self, linha, coluna):
        posicao = self.tabuleiro.get_peca(linha, coluna)
        if self._peca_a_mover and posicao == 0:
            # remover posições inexistentes do tabuleiro (parte inferior)
            if (linha < 5 or (linha == 5 and coluna != 0 and coluna != 4)) or (linha == 6 and coluna != 1 and coluna != 3):
                self._jogada.append([linha, coluna])
                self._tabuleiro.mover(self._peca_a_mover, linha, coluna)
                self.mudar_turno()
        else:
            return False

        return True

    def mudar_turno(self):
        if self._turno == 'onca':
            self._turno = 'cachorro'
        else:
            self._turno = 'onca'

    @property
    def tabuleiro(self):
        return self._tabuleiro

    @property
    def jogada(self):
        return self._jogada

    @jogada.setter
    def jogada(self, jogada):
        self._jogada = jogada

    @property
    def partida_em_andamento(self):
        return self._partida_em_andamento


