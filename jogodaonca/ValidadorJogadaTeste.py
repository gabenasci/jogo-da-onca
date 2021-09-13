import math
from enum import Enum


class TipoJogador(Enum):
    CACHORRO = 'C ' # depois dos testes trocar por 'cachorro'
    ONCA = 'O ' # depois dos testes trocar por 'onca'
    VAZIA = '* ' # depois dos testes trocar por 'vazia'


class Estados(Enum):
    ESPERA_ONCA = 1
    ESPERA_VAZIAO = 2
    ESPERA_CACHORRO = 3
    ESPERA_VAZIAC = 4
    JOGADA_MULTIPLA = 5


class Jogador:
    def __init__(self, nome: str, tipo: TipoJogador):
        self.__nome = nome
        self.__tipo = tipo
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

class Peca:
    def __init__(self, jogador: Jogador):
        self.__jogador = jogador

    @property
    def jogador(self):
        return self.__jogador
    
    @jogador.setter
    def tipo(self, jogador):
        self.__jogador = jogador

class Tabuleiro:
    def __init__(self):
        self.__casas = [
                [Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA))],
                [Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA))],
                [Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA))],
                [Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA))],
                [Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA))],
                [Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA))],
                [Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA)), Peca(Jogador('', TipoJogador.VAZIA))],
                ]

    @property
    def casas(self):
        return self.__casas
    
    @casas.setter
    def casas(self, casas):
        self.__casas = casas
            
    def limpar_tabuleiro(self):
        jogador = Jogador('', TipoJogador.VAZIA)
        peca = Peca(jogador)
        for linha in range(7):
            for coluna in range(5):
                self.__casas[linha][coluna] = peca
                
    def get_peca(self, lin, col):
        todas_casas = self.casas
        return todas_casas[lin][col]
    
    def mover(self, jogada: []):   # [[linha_org, col_org], [l_dest, c_dest)]]
        peca = self.__casas[jogada[0][0]][jogada[0][1]]
        self.__casas[jogada[0][0]][jogada[0][1]] = Peca(Jogador('', TipoJogador.VAZIA))
        self.__casas[jogada[1][0]][jogada[1][1]] = peca
        
    def posicionar_pecas_inicio(self):
        self.limpar_tabuleiro()
        jogador = Jogador('', TipoJogador.CACHORRO)
        peca = Peca(jogador)
        for linha in range(3):
            for coluna in range(5):
                self.__casas[linha][coluna] = peca
        jogador = Jogador('', TipoJogador.ONCA)
        peca = Peca(jogador)
        self.__casas[2][2] = peca
        
    def print_tabuleiro(self):
        for linha in range(7):
            for coluna in range(5):
                print(self.__casas[linha][coluna].jogador.tipo.value, ' ', end = '')
            print()
        print()

class ValidadorJogada:
    def __init__(self):
        self.__jogada = [] # [[linha_org, col_org], [l_dest, c_dest)]]
        self.__posicao_onca: int
        self.__tabuleiro: Tabuleiro
        self.__jogador: Jogador
        self.__casas_primarias = []
        self.__casas_secundarias = []
        self.__jogada_valida: boolean
        self.__jogada_multipla: boolean
        self.__cachorro_comido: boolean
        self.__cachorros_comidos: int
        self.__peca: Peca
        self.__validado: boolean
        self.__passo: int
        
    def verificar_jogada(self, jogada: [], tabuleiro: Tabuleiro, cachorros_comidos: int):
        self.__cachorros_comidos = cachorros_comidos
        self.__jogada = jogada
        self.__tabuleiro = tabuleiro
        self.reset_atributos_jogada()
        primario = self.destino_primario()
        if not primario:
            print('Not primario')
            self.proximo_passo()
            onca = self.verificar_se_onca(self.__jogada[0])
            if onca:
                print('onça')
                self.proximo_passo()
                secundario = self.destino_secundario()
                if secundario:
                    print('É sec')
                    self.proximo_passo()
                    existe_cachorro = self.existe_cachorro(self.__jogada[0], self.__jogada[1])
                    if existe_cachorro:
                        print('Existe cachorro')
                        self.proximo_passo()
                        self.cachorro_comido()
                        self.__cachorros_comidos += 1
                        self.__jogada_multipla = self.avaliar_sequencia_multipla()
                        self.validado()
                        self.jogada_valida()
                    else:
                        print('Não existe cachorro')
                        self.validado()
                        self.jogada_nao_valida()
                else:
                    print('Não secundario')
                    self.validado()
                    self.jogada_nao_valida()   
            else:
                print('Não é onça')
                self.validado()
                self.jogada_nao_valida()      
        else:
            print('Primário')
            self.validado()
            self.jogada_valida()     
    
    def verificar_se_onca(self, posicao: []):
        return self.__tabuleiro.get_peca(posicao[0], posicao[1]).jogador.tipo.value == TipoJogador.ONCA.value
    
    def verificar_se_vazia(self, posicao: []):
        return self.__tabuleiro.get_peca(posicao[0], posicao[1]).jogador.tipo.value == TipoJogador.VAZIA.value
    
    def destino_primario(self):
        casa_origem = self.__jogada[0]
        self.traz_vizinhos(casa_origem)
        casa_destino = self.__jogada[1][0]*5 + self.__jogada[1][1] + 1
        return casa_destino in self.__casas_primarias
    
    def destino_secundario(self):
        casa_origem = self.__jogada[0]
        self.traz_vizinhos(casa_origem)
        casa_destino = self.__jogada[1][0]*5 + self.__jogada[1][1] + 1
        return casa_destino in self.__casas_secundarias
    
    def existe_cachorro(self, origem, destino):
        casa_intermediaria = [abs(int((destino[0] + origem[0])/2)),
                              abs(int((destino[1] + origem[1])/2))]
        return self.__tabuleiro.get_peca(casa_intermediaria[0], casa_intermediaria[1]).jogador.tipo.value == TipoJogador.CACHORRO.value
        
    def jogada_valida(self): 
        self.__jogada_valida = True
        
    def jogada_nao_valida(self): 
        self.__jogada_valida = False
    
    def cachorro_comido(self):
        self.__cachorro_comido = True
    
    def avaliar_sequencia_multipla(self):
        casa_onca = self.__jogada[1]
        self.traz_vizinhos(casa_onca)
        for casa_destino in self.__casas_secundarias:
            lin_dest = int((casa_destino-1)/5)
            col_dest = (casa_destino-1)%5
            if self.verificar_se_vazia([lin_dest, col_dest]) and self.existe_cachorro(self.__jogada[1], [lin_dest, col_dest]):
                return True
        return False
                   
    def get_posicao_onca(self):
        return self.__posicao_onca        
    
    def reset_atributos_jogada(self):
        self.__jogada_valida = False
        self.__jogada_multipla = False
        self.__cachorro_comido = False
        self.__validado = False
        self.__passo = 0
        
    def atributos_validacao_jogada(self):
        return self.__jogada_valida, self.__cachorro_comido, self.__jogada_multipla
    
    def verificar_vencedor(self):
        self.__vencedor = "None"
        cachorros_comidos = self.verificar_cachorros_comidos()
        if cachorros_comidos < 5:
            onca_cercada = onca_cercada()
            if onca_cercada:
                self.__vencedor = self.__jogador
                return
        else:
            self.__vencedor = self.__jogador
            return        
    
    def verificar_cachorros_comidos(self):
        return self.__cachorros_comidos
    
    def proximo_passo(self):
        self.__passo += 1
        
    def validado(self):
        self.__validado = True
        
    def onca_cercada(self):
        casa_onca = self.__jogada[0]
        self.traz_vizinhos(casa_onca)
        self.__onca_cercada = False
        for primaria in self.__casas_primarias:
            if self.__tabuleiro.get_peca(primaria[0], primaria[1]).jogador.tipo.value == TipoJogador.VAZIA.value:
                return self.__onca_cercada
        for secundaria in self.__casas_secundarias:
            if self.__tabuleiro.get_peca(secundaria[0], secundaria[1]).jogador.tipo.value == TipoJogador.VAZIA.value:
                return self.__onca_cercada
        self.__onca_cercada = True
        return self.__onca_cercada
    
    def traz_vizinhos(self, casa):
        casa1 = [[2, 6, 7], [3, 8, 13]]
        casa2 = [[1, 3, 7], [4, 12]]
        casa3 = [[2, 4, 7, 8, 9], [1, 5, 11, 13, 15]]
        casa4 = [[3, 5, 9], [2, 14]]
        casa5 = [[4, 9, 10], [3, 13, 15]]
        casa6 = [[1, 7, 11], [8, 16]]
        casa7 = [[1, 2, 3, 6, 8, 11, 12, 13], [9, 17, 19]]
        casa8 = [[3, 7, 9, 13], [6, 10, 18]]
        casa9 = [[3, 4, 5, 8, 10, 13, 14, 15], [7, 17,19]]
        casa10 = [[5, 9, 15], [8, 20]]
        casa11 = [[6, 7, 12, 16, 17], [1, 3, 13, 21, 23]]
        casa12 = [[7, 11, 13, 17], [2, 24, 22]]
        casa13 = [[7, 8, 9, 12, 14, 17, 18, 19], [1, 3, 5, 11, 15, 21, 23, 25]]
        casa14 = [[9, 13, 15, 19], [4, 12, 24]]
        casa15 = [[9, 10, 14, 19, 20], [3, 5, 13, 23, 25]]
        casa16 = [[11, 17, 21], [6, 18]]
        casa17 = [[11, 12, 13, 16, 18, 21, 22, 23], [7, 9, 19, 29]]
        casa18 = [[12, 17, 19, 23], [8, 16, 20, 28]]
        casa19 = [[13, 14, 15, 18, 20, 23, 24, 25], [7, 9, 17, 27]]
        casa20 = [[15, 19, 25], [10, 18]]
        casa21 = [[16, 17, 22], [11, 13, 23]]
        casa22 = [[17, 21, 23], [12, 24]]
        casa23 = [[17, 18, 19, 22, 24, 27, 28, 29], [11, 13, 15, 21, 25, 31, 33, 35]]
        casa24 = [[19, 23, 25], [14, 22]]
        casa25 = [[19, 20, 24], [13, 15, 23]]
        casa26 = [[], []]
        casa27 = [[23, 28, 31], [19, 29]]
        casa28 = [[23, 27, 29, 33], [18]]
        casa29 = [[23, 28, 35], [17, 27]]
        casa30 = [[], []]
        casa31 = [[27, 33], [23, 35]]
        casa32 = [[], []]
        casa33 = [[28], [23]]
        casa34 = [[], []]
        casa35 = [[29, 33], [23, 31]]
        posicao = [
                [casa1, casa2, casa3, casa4, casa5],
                [casa6, casa7, casa8, casa9, casa10],
                [casa11, casa12, casa13, casa14, casa15],
                [casa16, casa17, casa18, casa19, casa20],
                [casa21, casa22, casa23, casa24, casa25],
                [casa26, casa27, casa28, casa29, casa30],
                [casa31, casa32, casa33, casa34, casa35]
                ]
        vizinhos = posicao[casa[0]][casa[1]]
        self.__casas_primarias = vizinhos[0]
        self.__casas_secundarias = vizinhos[1]
        return self.__casas_primarias, self.__casas_secundarias

tabu = Tabuleiro()
tabu.posicionar_pecas_inicio()
tabu.print_tabuleiro()
tabu.mover([[2, 3], [2, 3]])
tabu.mover([[2, 3], [3, 3]])
tabu.print_tabuleiro()

validador = ValidadorJogada()
validador.verificar_jogada([[2, 2], [4, 2]], tabu, 2)
resultado = validador.atributos_validacao_jogada()
print('self.__jogada_valida, self.__cachorro_comido, self.__jogada_multipla')
print(resultado)
