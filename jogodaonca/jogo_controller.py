import pygame
#from .constantes import
from .tabuleiro import Tabuleiro
from .ator_jogador import AtorJogador

class JogoController:
    def __init__(self, janela):
        self._init()
        self.janela = janela

    def update(self):
        self.interface.desenhar(self.janela)
        pygame.display.update()

    def _init(self):
        self.peca_selecionada = None
        self.interface = AtorJogador()
        self.tabuleiro = self.interface.tabuleiro
        self.turno = "onca"
        self.lances_validos = {}

    def resetar(self):
        self._init()

    def selecionar(self, linha, coluna):
        if self.peca_selecionada:
            result = self._mover(linha, coluna)
            if not result:
                self.peca_selecionada = None
                self.selecionar(linha, coluna)
        else:
            peca = self.tabuleiro.get_peca(linha, coluna)
            if peca != 0 and peca.tipo == self.turno:
                self.peca_selecionada = peca
                return True

        return False

    def _mover(self, linha, coluna):
        peca = self.tabuleiro.get_peca(linha, coluna)
        if self.peca_selecionada and peca == 0:
            self.tabuleiro.mover(self.peca_selecionada, linha, coluna)
            self.mudar_turno()
        else:
            return False

        return True

    def mudar_turno(self):
        if self.turno == "onca":
            self.turno = "cachorro"
        else:
            self.turno = "onca"

