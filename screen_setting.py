import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
background_image = pygame.image.load(background_image_filename).convert()

Fullscreen = False

while True:

    for event in pygame.event.get():
        pass
