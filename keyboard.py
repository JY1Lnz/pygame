import pygame
from pygame.locals import *
from sys import exit
from vector_2d import vector
from math kimport *

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

sprite_pos = vector.Vector(200, 150)
sprite_speed = 300.
sprite_rotation = 0.  # 初始角度
sprite_rotation_speed = 360.  # 每秒转动的角度数

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()

    rotation_direction = 0
    movement_direction = 0

    key_direction = vector.Vector(0, 0)
    if pressed_keys[K_LEFT]:
        rotation_direction = +1
    elif pressed_keys[K_RIGHT]:
        rotation_direction = -1

    if pressed_keys[K_UP]:
        movement_direction = +1
    elif pressed_keys[K_DOWN]:
        movement_direction = -1

    screen.blit(background, (0, 0))

    # 获得一条转向后的鱼
    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)

    w, h = rotated_sprite.get_size()
    # 获得绘制图片的左上角
    sprite_draw_pos = vector.Vector(sprite_pos.x - w / 2, sprite_pos.y - h / 2)
    screen.blit(rotated_sprite, sprite_draw_pos.int())

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds

    heading_x = sin(sprite_rotation * pi / 180.)
    heading_y = cos(sprite_rotation * pi / 180.)

    heading = vector.Vector(heading_x, heading_y)

    heading *= movement_direction

    sprite_pos += heading * sprite_speed * time_passed_seconds

    pygame.display.update()
