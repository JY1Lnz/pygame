import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'

pygame.init()  # 初始化pygame

screen = pygame.display.set_mode((640, 480), 0, 32)  # 创建一个窗口,长640,高480
# 接受三个参数,第一个为元祖 表示窗口的分辨率,第二个是标志位,第三个为色深
# 返回一个Surface对象

pygame.display.set_caption("Hello World!")  # 设置窗口标题
background = pygame.image.load(background_image_filename).convert()
# 加载图片到background变量
# convert参数将图片转化为Surface对象
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
# 加载图片,convert_alpha使其具有每像素透明度
# convert_alpha 保留的了alpha的通道信息,可以理解为透明的部分

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()

    screen.blit(background, (0, 0))  # 将背景图画到屏幕
    x, y = pygame.mouse.get_pos()  # 获取鼠标位置
    x -= mouse_cursor.get_width() / 2  # 获取光标左上角位置
    y -= mouse_cursor.get_height() / 2
    screen.blit(mouse_cursor, (x, y))  # 画光标

    pygame.display.update()  # 刷新屏幕
