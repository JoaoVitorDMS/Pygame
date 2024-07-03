import pygame as motor
import math as matematica
class ObjetoPersonagem:
    _vida = 0
    _velocidade = 0
    _estaMorto = False
    _estaAtacando = False
    _jogadorPosicao = [0,0]
    _inimigoPosicao = [0,0]

    def __init__(self, vector):
        motor.sprite.Sprite.__init__(self)
        tela = motor.display.get_surface()
        self.area = tela.get_rect()
        self.vector = vector

    def update(self):
        saude = self.mortePersonagem(self._vida, self._estaMorto)
        novaPosicao = self.calculaNovaPosicao(self.rect, self.vector)
        self.rect = novaPosicao
        self.vida = saude
    
    def calculaNovaPosicao(self, rect, vector):
        pass

    def mortePersonagem(self, _vida, _estaMorto):
        if self.vida == 0:
            self._estaMorto = True
            motor.event.type == quit
        else:
            self._estaMorto = False
    
    def ataquePersonagem(self, _estaAtacando):
        pass
class ObjetoFase:
    posicaoPlataforma = [0,0]
    pontos = 0
    tempoFase = 0
    