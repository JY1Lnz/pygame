import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'
fish_image_filename = 'fugu.png'

pygame.init()
pygame.display.list_modes()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("fish to bowl")
background_image = pygame.image.load(background_image_filename).convert()
fish_image = pygame.image.load(fish_image_filename).convert_alpha()

x, y = 0, 0
move_x, move_y = 0, 0
"""
my_event = pygame.event.Event(KEYDOWN, key=K_SPACE, mod=0, unicode=u' ')
# 构造事件 第一个参数为按下键的类型 第二个参数为一个字典 对应具体值下面有另一种写法
my_event = pygame.event.Event(KEYDOWN, {"key": K_SPACE, "mod": 0, "unicode": u' '})
CATONKEYBOARD = USEREVENT+1
my_event2 = pygame.event.Event(CATONKEYBOARD, message="Bad cat!")
pygame.event.post(my_event2)  # 将事件添加到事件列表
"""

while True:
    for event in pygame.event.get():
        # 按键事件右不同种类,不同种类有不同值
        # 同时pygame.event.get() 返回一个列表,当没有事件发生时，列表为空
        # 此循环就无法执行
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:  # 如果键盘按下
            if event.key == K_ESCAPE:
                exit()
            if event.key == K_LEFT:
                move_x = -0.5
            elif event.key == K_RIGHT:
                move_x = 0.5
            elif event.key == K_UP:
                move_y = -0.5
            elif event.key == K_DOWN:
                move_y = 0.5
        else:
            move_x = move_y = 0

    x = x + move_x
    y = y + move_y

    screen.fill((0, 0, 0))  # 屏幕重新绘色
    screen.blit(background_image, (0, 0))
    screen.blit(fish_image, (x, y))

    pygame.display.update()
