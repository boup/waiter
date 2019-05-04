import pygame, sys, random
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


textures = {
DIRT : pygame.image.load('home1.png'),
GRASS : pygame.image.load('home1.png'),
WATER : pygame.image.load('home1.png'),
COAL : pygame.image.load('home1.png')
}
TILWSIZE = 100
MAPWIDTH = 5
MAPHIGHT = 5

resourses = [DIRT, GRASS, WATER, COAL]

tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHIGHT)]
for rw in range(MAPHIGHT):
    for cl in range(MAPWIDTH):
        randomNumber = random.randint(0, 15)
        if randomNumber == 0:
            title = COAL
        elif randomNumber == 1 or randomNumber == 2:
            title = WATER
        elif randomNumber >=3 and randomNumber <=7:
            title = GRASS
        else:
            title = DIRT

        tilemap[rw][cl] = title

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILWSIZE, MAPHIGHT*TILWSIZE))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for row in range(MAPHIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILWSIZE, row*TILWSIZE))
            pygame.display.update()
