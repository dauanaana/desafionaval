from navio import Navio


class Jogador:
    def __init__(self, nome, mapa):
        self.lista_de_ataques = []
        self.mapa = mapa
        self.nome = nome
        self.lista_de_navios = []
    def criar_navio(self, coordIX, coordIY, coordFX, coordFY):
        if self.mapa.validar_coordenadas(coordIX, coordFX, coordFX, coordFY):
            navio = Navio(coordIX, coordIY, coordFX, coordFY)
            self.lista_de_navios.append(navio)
            return True
        else:
            return False
    def atacar(self, coordX, coordY, jogador):
        self.lista_de_ataques.append((coordX, coordY))
        for navio in jogador.lista_de_navios:
            if navio.verificar_dano(coordX, coordY):
                return True
        return False
    def verificar_status(self):
        for navio in self.lista_de_navios:
            if navio.vivo:
                return True
        return False
