import pygame

from .ator_jogador import AtorJogador
from .peca import Peca
from .estados import Estados
from .jogador import Jogador
from .tipo_jogador import TipoJogador
from .validador_jogada import ValidadorJogada

class Jogo:
    def __init__(self):
        self._interface = AtorJogador()
        self._init()
        #self.janela = janela

    def _init(self):
        self._peca_a_mover = None
        self._tabuleiro = self._interface.tabuleiro
        self._jogadores = [Jogador('Jogador 1', 'onca'), Jogador('Jogador 2', 'cachorro')]
        self._estado = Estados.ESPERA_ONCA
        self._validador = ValidadorJogada()
        self._partida_em_andamento = False
        self._numero_cachorros = 14
        self._turno = 'onca'
        self._jogada = []
        self._vencedor = None
        self._peca_selecionada = None
        self._existe_vencedor = False


    def iniciar(self):
        self._partida_em_andamento = True
        self.posicionar_pecas()

    def finalizar(self):
        self._init()
        self.tabuleiro.posicionar_pecas_inicio()

    def click(self):
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
                        if len(self.jogada) > 2 or len(self.jogada) == 0:
                            self.finalizar()
                            self.mensagem("Partida finalizada")
                        else:
                            self.mensagem("Finaliza o lance primeiro")

            if self.partida_em_andamento:
                self.posicionar_pecas()
                self.atualizar_placar(self._validador.cachorros_comidos)
                if self.verificar_vencedor():
                    self.mensagem("Vencedor: " + str(self._vencedor))
                    self.finalizar()
            else:
                self.desenhar_tela()


    def desenhar_tela(self):
        self._interface.desenhar_tela()
        pygame.display.update()

    def atualizar_placar(self, cachorros_comidos):
        self._interface.desenhar_placar(cachorros_comidos)
        pygame.display.update()

    def posicionar_pecas(self):
        self._interface.desenhar_pecas()
        pygame.display.update()

    def mensagem(self, str):
        self._interface.desenhar_mensagem(str)
        pygame.display.update()
        pygame.time.wait(1000)

    def selecionar_peca(self, linha, coluna):
        peca_clicada = self._tabuleiro.get_peca(linha, coluna)
        estado = self.get_estado()
        if estado == 1 or estado == 3:
            if peca_clicada.jogador.tipo.value == 'onca' or peca_clicada.jogador.tipo.value == 'cachorro':
                turno_correto = self.verificar_turno(peca_clicada)
                print(self._turno)
                if turno_correto:
                    self._jogada = []
                    self._peca_a_mover = peca_clicada
                    self._jogada.append(peca_clicada)
                    self._jogada.append([linha, coluna])
                    self._validador.jogada = self._jogada
                    if estado == 1:
                        self.mudar_estado(Estados.ESPERA_VAZIAO)
                    elif estado == 3:
                        self.mudar_estado(Estados.ESPERA_VAZIAC)
                else:
                    self.mensagem("Turno errado")
            if peca_clicada.jogador.tipo.value == 'vazia':
                self.mensagem("Você deve clicar em uma peça")
        elif estado == 2 or estado == 4:
            if peca_clicada.jogador.tipo.value == 'vazia':
                self._jogada.append([linha, coluna])
                jogada_valida = self._validador.verificar_jogada(self._jogada, self.tabuleiro, self._validador.cachorros_comidos)
                if jogada_valida is True:
                    self._mover(linha, coluna)
                    if self._validador.cachorro_foi_comido:
                        l, c = [abs(int((self._jogada[1][0] + self._jogada[2][0]) / 2)),
                                abs(int((self._jogada[1][1] + self._jogada[2][1]) / 2))]
                        print(l, c)
                        self.tabuleiro.casas[l][c].jogador = Jogador('', TipoJogador.VAZIA)
                    self._validador.verificar_vencedor()
                    vencedor = self._validador.vencedor
                    if not vencedor:
                        jogada_multipla = self.verificar_jogada_multipla()
                        print(self._turno)
                        if jogada_multipla:
                            self.mensagem("JOGADA MULTIPLA")
                            self.mudar_estado(Estados.JOGADA_MULTIPLA)
                        elif self._turno == 'onca':
                            print("MUDANDO TURNO E ESTADO PARA CACHORRO")
                            self.mudar_turno()
                            self.mudar_estado(Estados.ESPERA_CACHORRO)
                        elif self._turno == 'cachorro':
                            self.mudar_turno()
                            self.mudar_estado(Estados.ESPERA_ONCA)
                    else:
                        self._existe_vencedor = True
                        self._vencedor = self._validador.vencedor
                else:
                    self._jogada.pop()
                    self.mensagem("Jogada não é válida")
            else:
                self.mensagem("Jogada inválida")
        elif estado == 5:
            if peca_clicada.jogador.tipo.value == 'onca' or self._peca_a_mover.jogador.tipo.value == 'onca':
                self.mudar_estado(Estados.ESPERA_ONCA)
                self.selecionar_peca(linha, coluna)
            elif peca_clicada.jogador.tipo.value == 'cachorro':
                self.mudar_estado(Estados.ESPERA_CACHORRO)
                self.selecionar_peca(linha, coluna)
            elif peca_clicada.jogador.tipo.value == 'vazia':
                self.mudar_estado(Estados.ESPERA_VAZIAO)
                self.selecionar_peca(linha, coluna)


        '''
        if not self._peca_a_mover:
            peca_clicada = self._tabuleiro.get_peca(linha, coluna)
            if peca_clicada.jogador.tipo.value != 'vazia' and self._turno == peca_clicada.jogador.tipo.value:
                self._peca_a_mover = peca_clicada
                self._jogada = []
                self.jogada.append(peca_clicada)
                self.jogada.append([linha, coluna])
            else:
                self.mensagem("Turno errado")
        else:
            self._jogada.append([linha, coluna])
            self._validador.verificar_jogada(self._jogada, self.tabuleiro, self._validador.cachorros_comidos)
            print("Jogada Valida ",self._validador.jogada_valida)
            print("cachorros comidos", self._validador.cachorros_comidos)
            casa_vazia = self._mover(linha, coluna)
            if self._validador.cachorro_foi_comido:
                l, c = [abs(int((self._jogada[1][0] + self._jogada[2][0]) / 2)), abs(int((self._jogada[1][1] + self._jogada[2][1])/2))]
                print(l, c)
                self.tabuleiro.casas[l][c].jogador = Jogador('',TipoJogador.VAZIA)
            if not casa_vazia:
                self._peca_a_mover = None
                self.selecionar_peca(linha, coluna)
        '''

    def _mover(self, linha, coluna):
        posicao = self.tabuleiro.get_peca(linha, coluna)
        if self._peca_a_mover and posicao.jogador.tipo == TipoJogador.VAZIA and self._validador.jogada_valida is True:
            # remover posições inexistentes do tabuleiro (parte inferior)
            if (linha < 5 or (linha == 5 and coluna != 0 and coluna != 4)) or (linha == 6 and coluna != 1 and coluna != 3):
                self._tabuleiro.mover(self._peca_a_mover, linha, coluna)
        else:
            return False
        return True

    #TESTAR ESTADOS
    def mudar_estado(self, estado: Estados):
        self._estado = estado

    def mudar_turno(self):
        if self._turno == 'onca':
            self._turno = 'cachorro'
        else:
            self._turno = 'onca'

    def verificar_turno(self, peca: Peca):
        return peca.jogador.tipo.value == self._turno

    def verificar_vencedor(self):
        return self._existe_vencedor

    def verificar_jogada_multipla(self):
        return self._validador.jogada_multipla

    def get_estado(self):
        return self._estado.value

    @property
    def vencedor(self):
        return self._vencedor

    @vencedor.setter
    def vencedor(self, jogador: Jogador):
        self._vencedor = jogador

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

    @partida_em_andamento.setter
    def partida_em_andamento(self, valor: bool):
        self._partida_em_andamento = valor

    @property
    def estado(self):
        return self._estado

    def __repr__(self):
        return str(self._jogadores)