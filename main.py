import pygame as MotorGame
import sys
from controle import Jogo

MotorGame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    jogo = Jogo(SCREEN_WIDTH, SCREEN_HEIGHT)
    jogo.run()

if __name__ == "__main__":
    main()
