import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640, 480)  # 屏幕分辨率
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []

while True:

    event = pygame.event.wait()  # 只有等待到事件执行后才会继续
    event_text.append(str(event))  # 将事件名添加进event_text
    event_text = event_text[int(-SCREEN_SIZE[1]/font_height):]
    # 这个切片操作保证了event_text里面只保留一个屏幕的文字

    if event.type == QUIT:
        exit()

    screen.fill((255, 255, 255))

    y = SCREEN_SIZE[1] - font_height

    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 0, 0)), (0, y))

        y -= font_height

    pygame.display.update()
