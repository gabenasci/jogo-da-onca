from .ator_jogador import AtorJogador
from .peca import Peca
from .estados import Estados
from .jogador import Jogador
from .tipo_jogador import TipoJogador
from .validador_jogada import ValidadorJogada

class Jogo:
    def __init__(self):
        self._interface = AtorJogador(self)
        self._init()

    def _init(self):
        self._peca_a_mover = None
        self._tabuleiro = self._interface.tabuleiro
        self._estado = Estados.ESPERA_ONCA
        self._validador = ValidadorJogada()
        self._partida_em_andamento = False
        self._turno = 'onca'
        self._jogada = []
        self._vencedor = None
        self._peca_selecionada = None
        self._existe_vencedor = False
        self._mensagem = None

    def iniciar(self):
        self.tabuleiro.posicionar_pecas_inicio()
        self._interface.desenhar_pecas()
        self._interface.atualizar_interface()
        self._partida_em_andamento = True

    def finalizar(self):
        if not self.verificar_vencedor():
            self.mensagem("Partida finalizada")
        else:
            self.mensagem("VENCEDOR: " + (str(self._vencedor).upper()))
        self._init()

    def desenhar_tela(self):
        self._interface.desenhar_tela()
        self._interface.atualizar_interface()

    def atualizar_placar(self, cachorros_comidos):
        self._interface.desenhar_placar(cachorros_comidos)
        self._interface.atualizar_interface()

    def posicionar_pecas(self):
        self._interface.desenhar_pecas()
        self._interface.atualizar_interface()

    def mensagem(self, str):
        self._mensagem = str
        self._interface.desenhar_mensagem(str)
        self._interface.atualizar_interface()
        self._interface.tempo_mensagem()

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
            if peca_clicada.jogador.tipo.value == 'vazia' and not self._validador.jogada_multipla:
                self.mensagem("Você deve clicar em uma peça")
            if peca_clicada.jogador.tipo.value == 'vazia' and self._validador.jogada_multipla:
                self.mensagem("Clique na onça novamente")
        elif estado == 2 or estado == 4:
            if peca_clicada.jogador.tipo.value == 'vazia':
                self._jogada.append([linha, coluna])
                jogada_valida = self._validador.verificar_jogada(self._jogada, self.tabuleiro, self._validador.cachorros_comidos)
                if jogada_valida is True:
                    self._mover(linha, coluna)
                    if self._validador.cachorro_foi_comido:
                        self.remover_cachorro()
                    self._validador.verificar_vencedor()
                    vencedor = self._validador.vencedor
                    if not vencedor:
                        jogada_multipla = self.verificar_jogada_multipla()
                        print(self._turno)
                        if jogada_multipla:
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
            elif estado == 4 and peca_clicada.jogador.tipo.value == 'cachorro':
                self.mudar_estado(Estados.ESPERA_CACHORRO)
                self.selecionar_peca(linha, coluna)
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

    def _mover(self, linha, coluna):
        posicao = self.tabuleiro.get_peca(linha, coluna)
        if self._peca_a_mover and posicao.jogador.tipo == TipoJogador.VAZIA and self._validador.jogada_valida is True:
            # remover posições inexistentes do tabuleiro (parte inferior)
            if (linha < 5 or (linha == 5 and coluna != 0 and coluna != 4)) or (linha == 6 and coluna != 1 and coluna != 3):
                self._tabuleiro.mover(self._peca_a_mover, linha, coluna)
        else:
            return False
        return True

    def remover_cachorro(self):
        l, c = [abs(int((self._jogada[1][0] + self._jogada[2][0]) / 2)),
                abs(int((self._jogada[1][1] + self._jogada[2][1]) / 2))]
        print(l, c)
        self.tabuleiro.casas[l][c].jogador = Jogador('', TipoJogador.VAZIA)

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

    @property
    def interface(self):
        return self._interface