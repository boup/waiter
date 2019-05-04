import pygame, sys
from pygame.locals import *

#colours
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (153, 76, 0)

#tipes
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3


colours = {
DIRT : BROWN,
GRASS : GREEN,
WATER : BLUE,
COAL : BLACK
}

tilemap = [
[GRASS, COAL, DIRT, WATER, COAL],
[WATER, WATER, GRASS, DIRT, GRASS],
[COAL, GRASS, WATER, DIRT,COAL],
[DIRT, GRASS, COAL, DIRT, GRASS],
[GRASS, WATER, DIRT, GRASS, WATER]
]

TILWSIZE = 100
MAPWIDTH = 5
MAPHIGHT = 5
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILWSIZE, MAPHIGHT*TILWSIZE))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for row in range(MAPHIGHT):
        for column in range(MAPWIDTH):
            pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column*TILWSIZE, row*TILWSIZE, TILWSIZE,  TILWSIZE))
            pygame.display.update()
