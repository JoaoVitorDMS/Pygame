import pygame as MotorGame
import sys

class Jogo:
    def __init__(self, width, height):
        self.screen = MotorGame.display.set_mode((width, height))
        MotorGame.display.set_caption("Nome Provisório")
        self.width = width
        self.height = height

def run(self):
    clock = MotorGame.time.Clock()

    while True:
        for event in MotorGame.event.get():
            if event.type == MotorGame.QUIT:
                MotorGame.quit()
                sys.exit()
        
        self.handle_input()
        self.update()
        self.render()

        MotorGame.display.flip()
        clock.tick(30)

def entrada_comando(self):
    teclado = MotorGame.key.get_pressed()
    if teclado[MotorGame.K_LEFT]:
        pass
    if teclado[MotorGame.K_RIGHT]:
        pass
    if teclado[MotorGame.K_UP]:
        pass
    if teclado[MotorGame.K_DOWN]:
        pass

def update(self):
    pass

def render(self):
    pass

    