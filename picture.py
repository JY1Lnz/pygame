import pygame
from pygame.locals import *
from sys import exit
from random import randint

bland_surface = pygame.Surface((256, 256))
bland_alpha_surface = pygame.Surface((256, 256), flags=SRCALPHA, depth=32)

my_rect1 = (100, 100, 200, 150)
my_rect2 = ((100, 100), (200, 150))
# 上两种为基础方法，表示的矩形也是一样的
my_rect3 = Rect(100, 100, 200, 150)
my_rect4 = Rect((100, 100), (200, 150))
clip_rect = ((320, 0), (640, 480))

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.set_clip(clip_rect)
    rand_cool = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.lock()
    for _ in range(100):
        rand_pos = (randint(0, 639), randint(0, 479))
        screen.set_at(rand_pos, rand_cool)
    screen.unlock()

    pygame.display.update()
