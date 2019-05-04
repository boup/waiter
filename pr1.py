import pygame, sys, random
from pygame.locals import *

#colours
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (153, 76, 0)
WHITE = (255, 255,255)

#tipes
HOME = 0
BIN_PLASTIC = 1
BIN_PAPER = 2
BIN_GLASS = 3
BIN_ORGANIC = 4
BIN_WASTE = 5

trash_Pos =[]
trashcounter=0

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('background.jpg', [0,0])
textures = {
HOME : pygame.image.load('images1.png'),
BIN_PLASTIC : pygame.image.load('home1.png'),
BIN_PAPER : pygame.image.load('home1.png'),
BIN_GLASS : pygame.image.load('home1.png'),
BIN_ORGANIC : pygame.image.load('home1.png'),
BIN_WASTE : pygame.image.load('home1.png')
}
TILWSIZE =100
MAPWIDTH = 8
MAPHIGHT = 8

PLAYER = pygame.image.load('GT.png')
playerPos = [8, 7]

resourses = [HOME, BIN_PLASTIC, BIN_PAPER, BIN_GLASS, BIN_ORGANIC, BIN_WASTE]
Q_homes=0
Q_glass=0
Q_paper=0
Q_plastic=0
Q_organic=0
Q_waste=0
tilemap = [ [HOME for w in range(MAPWIDTH)] for h in range(MAPHIGHT)]

#반복문 동작 안함
for rw in range(MAPHIGHT):
    for cl in range(MAPWIDTH):       
        
        randomNumber = random.randint(0, 14)
        if randomNumber == 1 or randomNumber == 2:
            title = BIN_GLASS
            Q_glass +=1
        elif randomNumber == 3 or randomNumber == 4:
            title = BIN_PAPER
            Q_paper +=1
        elif randomNumber ==5 or randomNumber ==6:
            title = BIN_PLASTIC
            Q_plastic +=1
        elif randomNumber ==7 or randomNumber ==8:
            title = BIN_ORGANIC
            Q_organic +=1
        elif randomNumber ==9 or randomNumber ==10:
            title = BIN_WASTE
            Q_waste +=1
        else:
            title = HOME
            Q_homes +=1

      
        tilemap[rw][cl] = title #랜덤한 사진을 tilemap에 넣어줌 (배경을 구성)

        if title ==BIN_GLASS:
            trash_Pos.append(rw)
            trash_Pos.append(cl)
            #trash_Pos.remove(1)
        #print('hello')
        
pygame.init()
pygame.display.set_caption("Autonuous waiter")
TILWSIZE1 = 125 # 가로 창 사이즈
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILWSIZE1, MAPHIGHT*TILWSIZE))
DISPLAYSURF.fill((255, 255, 255))

#scr = pygame.display.set_mode((MAPWIDTH*TILWSIZE, MAPHIGHT*TILWSIZE))
#scr.fill((255, 255, 255))

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

Q_player=0

while True:
#    scr.blit(BackGround.image, BackGround.rect)
    DISPLAYSURF.blit(BackGround.image, BackGround.rect)
    pygame.draw.rect(DISPLAYSURF, (GREEN), (800, 700, 100, 100)) #시작점
    pygame.draw.rect(DISPLAYSURF, (BROWN), (800, 400, 100, 100)) #끝점

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

            
#여기가 캐릭터 이동(키보드 입력으로)
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT and (playerPos[0] < MAPWIDTH - 1 or (playerPos[0]==7 and playerPos[1]==4)):
                playerPos[0] +=1
                Q_player +=1
            if event.key == K_LEFT and playerPos[0] > 0:
                playerPos[0] -=1
                Q_player +=1
            if event.key == K_UP and playerPos[1] > 0 and playerPos[0] < MAPWIDTH:
                playerPos[1] -=1
                Q_player +=1
            if event.key == K_DOWN and playerPos[1] < MAPHIGHT - 1 and playerPos[0] < MAPWIDTH:
                playerPos[1] +=1
                Q_player +=1


#여기가 테이블 배치 (반복문으로 테이블 배치)
    for row in range(MAPHIGHT):
        for column in range(MAPWIDTH):
            #trash_Pos
            if row % 2 == 0:
                #rect는 직사각형을 그리는 함수 
                pygame.draw.rect(pygame.image.load('images1.png'), (BLACK), (500, 500, 200, 200))
                #DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILWSIZE, row*TILWSIZE))#오른쪽 값 두개가 그림이 나타나는 좌표
                #pygame.draw.rect(DISPLAYSURF.blit(textures[tilemap[row][column]], (100, 100), (GREEN), (500, 500, 100, 100))
            
    TILWSIZE2 = 10
    
#이 반복문은 동작 안함. 
    for p in range(0, len(trash_Pos)-1):
        if(playerPos[0]==trash_Pos[p] and playerPos[1]==trash_Pos[p+1]):
            trashcounter +=1
            print(playerPos[0], playerPos[1], trash_Pos[p], trash_Pos[p+1])
            print(trash_Pos)

    pygame.time.delay(10)
    DISPLAYSURF.blit(PLAYER, (playerPos[0]*TILWSIZE, playerPos[1]*TILWSIZE))
    #DISPLAYSURF.blit(PLAYER, (playerPos[0]*400, playerPos[1]*500))
#    print('Player Position:  ', playerPos)
    print(trashcounter)



#동작 없음
    pygame.draw.rect(DISPLAYSURF, WHITE, (805, 248, 180, 42))
#    DISPLAYSURF.blit(textsurface6,(805,250))

#없으면 화면이 안뜸
    pygame.display.update()
