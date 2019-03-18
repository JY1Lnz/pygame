import pygame
from pygame.locals import *
from sys import exit
from vector_2d import vector

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = vector.Vector(100.0, 100.0)
heading = vector.Vector()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, position.int())

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    # 参数前面加×意味着把列表或元祖展开
    destination = vector.Vector(*pygame.mouse.get_pos())
    # 计算鱼儿到当前鼠标位置的向量
    vector_to_mouse = destination - position
    # 向量规格化
    vector_to_mouse = vector_to_mouse.unit()

    heading = heading + (vector_to_mouse * .6)

    position += heading * time_passed_seconds

    pygame.display.update()
