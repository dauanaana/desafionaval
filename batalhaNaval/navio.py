"""
:mod:'Jogador'
==============

    module:: jogador
    :plataform: All
    :synopsisi: Esté modulo implementa a classe navio
    moduleauthor:: Ríad Mattos Nassiffe
"""


class Navio:
    """
        A classe navio é assim...
    """
    def __init__(self, coordIX, coordIY, coordFX, coordFY):
        """
            O método init inicializa o navio de acordo com as cooredenadas
            enviadas
        """
        self.vivo = True
        if coordIX == coordFX:
            self.tamanho = coordFY - coordIY
        else:
            self.tamanho = coordFX - coordIX
        self.tamanho += 1
        self.coordIX = coordIX
        self.coordIY = coordIY
        self.coordFX = coordFX
        self.coordFY = coordFY
        self.vida = self.tamanho
        self.danos = []
        self.lista_posicoes = []
        self.listar_posicoes()

    def verificar_dano(self, posX, posY):
        """
            O método init inicializa o navio de acordo com as cooredenadas
            enviadas
        """
        coordenada = (posX, posY)
        acertar = False
        if coordenada in self.lista_posicoes:
            acertar = True
            if coordenada not in self.danos:
                self.danos.append(coordenada)
                if len(self.danos) == self.tamanho:
                    self.vivo = False
        return acertar
    def listar_posicoes(self):
        if self.coordFX == self.coordIX:
            for y in range(self.coordIY, self.coordFY+1):
                coordenada = (self.coordIX, y)
                self.lista_posicoes.append(coordenada)
        else:
            for x in range(self.coordIX, self.coordFX+1):
                coordenada = (x, self.coordFY)
                self.lista_posicoes.append(coordenada)
