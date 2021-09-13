from .tipo_jogador import TipoJogador


class Jogador:
    def __init__(self, nome: str, tipo: TipoJogador):
        self._nome = nome
        self._tipo = tipo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
