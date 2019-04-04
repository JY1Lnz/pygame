import pygame
from pygame.locals import *
from sys import exit
from vector_2d import vector
from math import *

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

pygame.mouse.set_visible(False)
pygame.event.set_grab(False)

sprite_pos = vector.Vector(200, 150)
sprite_speed = 300.
sprite_rotation = 0.
sprite_rotation_speed = 360

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

    pressed_keys = pygame.key.get_pressed()

    pressed_mouse = pygame.mouse.get_pressed()

    rotation_direction = 0
    movement_direction = 0

    rotation_direction = pygame.mouse.get
