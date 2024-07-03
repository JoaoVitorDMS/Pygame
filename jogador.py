import pygame as MotorGame

class Jogador():
    def __init__(self, x, y):
        super().__init__()
        self.imagem = MotorGame.surface((32, 32))
        self.rect = self.imagem.get_rect()
        self.rect.center = (x, y)
        self.velocidade = 5

    def mover():
        pass

    def update():
        pass
    