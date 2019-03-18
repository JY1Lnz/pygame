import pygame
from pygame.locals import *
from sys import exit

background_image_filenmae = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filenmae).convert()
sprite = pygame.image.load(sprite_image_filename)

clock = pygame.time.Clock()  # Clock对象
x, y = 100., 100.
speed_x, speed_y = 250., 300.


while True:
    """
        图片碰到墙壁自动改变方向回弹
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, y))

    time_passed = clock.tick()
    time_passed_sce = time_passed / 1000.0
    print(time_passed_sce)
    distance_moved_x = time_passed_sce * speed_x
    distance_moved_y = time_passed_sce * speed_y
    x += distance_moved_x
    y += distance_moved_y

    if x > 640 - sprite.get_width():
        speed_x = -speed_x
        x = 640 - sprite.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0.

    if y > 480 - sprite.get_height():
        speed_y = -speed_y
        y = 480 - sprite.get_height()
    elif y < 0:
        speed_y = -speed_y
        y = 0

    pygame.display.update()
