import pygame, time, sys, random, os
from pygame.locals import *
from time import gmtime, strftime

pygame.init()

w = 640
h = 400

screen = pygame.display.set_mode((w, h),RESIZABLE)
clock = pygame.time.Clock()
x = y = 100

def starting():
    basicfont = pygame.font.SysFont(None, 48)
    text = basicfont.render('Starting...', True, (255, 255, 255), (0, 0, 255))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.fill((0, 0, 255))
    screen.blit(text, textrect)

def taskbar():
    basicfont = pygame.font.SysFont(None, 24)
    taskbarrect = pygame.Rect((0, int(h-40)), (int(w), int(h)))
    text = basicfont.render(strftime("%Y-%m-%d", gmtime()), True, (0, 0, 0))
    text2 = basicfont.render(strftime("%H:%M:%S", gmtime()), True, (0, 0, 0))
    taskbarrect.blit(text, (w - 100, h - 37))
    taskbarrect.blit(text2, (w - 100, h - 17))
    pygame.display.update()

starting()
screen.fill((255,255,255))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==VIDEORESIZE:
            w = event.dict['size'][0]
            h = event.dict['size'][1]
            screen=pygame.display.set_mode(event.dict['size'],RESIZABLE)
    taskbar()
