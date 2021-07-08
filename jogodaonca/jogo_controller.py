import pygame
#from .constantes import
from .tabuleiro import Tabuleiro
from .ator_jogador import AtorJogador

class JogoController:
    def __init__(self, janela):
        self.peca_selecionada = None
        self.interface = AtorJogador()
        self.turno = 'onca'
        self.lances_validos = {}
        self.janela = janela

    def update(self):
        self.interface.desenhar()
        pygame.display.update()