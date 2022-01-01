import time
import random
import pygame
from pygame import mixer
import sys
import os
pygame.init()


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
bg = (38, 47, 78, 255)
snake = (4, 184, 113, 255)
screen_Height = 600
screen_Width = 900
gameDisplay = pygame.display.set_mode((screen_Width, screen_Height))
font = pygame.font.SysFont(None, 30)
screen = pygame.display.set_mode((1000, 1000))


def bg_Func():
    rand = 0

    #background = pygame.image.load('BG Pics/IMG0.jpg').convert_alpha()
    clock = pygame.time.Clock()
    fps = 40
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        file = os.listdir('G:\Python\Alexa\BG Pics')
        background = pygame.image.load(f'BG Pics/IMG{rand}.jpg')
        screen.blit(background, (-40, -40))
        rand += 1
        if rand > len(file)-50:
            rand = 0
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    sys.exit()


bg_Func()
