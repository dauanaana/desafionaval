#!/usr/bin/env python3

from jogador import Jogador
from mapa import Mapa


class BatalhaNaval:

    def __init__(self):
        x = int(input("Defina o valor máximo do eixo X:"))
        y = int(input("Defina o maior valor do eixo Y:"))
        self.mapa = Mapa(x, y)

    def inicializar_jogador(self):

        nome = input("Qual nome do Jogador 1:")
        jogador = Jogador(nome, self.mapa)
        nNavios = int(input("Quantos navios serão criados:"))
        for i in range(nNavios):
            cordIX = int(input("Qual a coordenada x inicial:"))
            cordIY = int(input("Qual a coordenada y inicial:"))
            cordFX = int(input("Qual a coordenada x final:"))
            cordFY = int(input("Qual a coordenada y final:"))
            jogador.criar_navio(cordIX, cordIY, cordFX, cordFY)
        return jogador

    def verificar_status(self, j1, j2):
        return j1.verificar_status() and j2.verificar_status()

    def jogar(self):
        j1 = self.inicializar_jogador()
        j2 = self.inicializar_jogador()
        while self.verificar_status(j1, j2):
            print("jogador 1")
            x = int(input("x:"))
            y = int(input("y:"))
            j1.atacar(x, y, j2)
            if not j2.verificar_status():
                print("Jogador 1 venceu!!")
            else:
                print("jogador 2")
                x = int(input("x:"))
                y = int(input("y:"))
                j2.atacar(x, y, j1)
                if not j1.verificar_status():
                    print("Jogador 2 venceu!!")

if __name__ == "__main__":
    b = BatalhaNaval()
    b.jogar()
