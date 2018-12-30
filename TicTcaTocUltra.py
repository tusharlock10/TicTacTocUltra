import tj

import pygame, random
from pygame.locals import *


RES=[900]*2
tile_len = RES[0] // 9

FPS = 60
TILE_ACTIVE = tj.colors["SKY BLUE"]

TILE_INACTIVE = [5, 5, 25]
pygame.init()
screen = pygame.display.set_mode(RES)
pygame.display.set_caption("Tic Tac Toe ULTRA")
clock = pygame.time.Clock()


def cycle(L):
    x=L.pop(0)
    L=L+[x]
    return L

def transform(color1, color2, skip=1):
    # This function transforms color1 into color2
    L=[] 
    if (color1[0]<color2[0]):i=list(range(color1[0], color2[0]+1, skip))
    else:i=list(range(color2[0], color1[0]+1, skip))[::-1]
    if i==[]:i=[color1[0]]
  
    if (color1[1]<color2[1]):j=list(range(color1[1], color2[1]+1))
    else:j=list(range(color2[1], color1[1]+1, skip))[::-1]
    if j==[]:j=[color1[1]]

    if (color1[2]<color2[2]):k=list(range(color1[2], color2[2]+1, skip))
    else:k=list(range(color2[2], color1[2]+1, skip))[::-1]
    if k==[]:k=[color1[2]]

    x=max(len(i), len(j), len(k))
    for m in range(len(i), x):i+=[i[-1]]
    for m in range(len(j), x):j+=[j[-1]]
    for m in range(len(k), x):k+=[k[-1]]

    for m in range(x):
        l=[i[m], j[m], k[m]]
        L+=[l]
    return L


def VIBGYOR():
    V=(128,0,128)
    I=(75,0,130)
    B=(0,0,255)
    G=(0,255,0)
    Y=(255,255,0)
    O=(255,165,0)
    R=(255,0,0)
    L=transform(V,I,2)+transform(I,B,2)+transform(B,G,2)+transform(G,Y,2)+transform(Y,O,2)+transform(O,R,2)+transform(R,V,2)
    return L

   
AllColors=VIBGYOR()

AllColors2=transform([255,0,0], [0,255,0])+transform([0,255,0], [0,0,255])+transform([0,0,255], [255,0,0])




class TicTacToe:
    global tile_len

    def __init__(self, RES):
        self.L = self.getList()
        self.grid = []  # self.makeGrid()
        self.currentBigTile = -1
        self.color=AllColors[0]
        self.gridColor=AllColors2[0]
        self.Dict = {
            0: [0, 1, 2, 9, 10, 11, 18, 19, 20],
            1: [27, 28, 29, 36, 37, 38, 45, 46, 47],
            2: [54, 55, 56, 63, 64, 65, 72, 73, 74],
            3: [3, 4, 5, 12, 13, 14, 21, 22, 23],
            4: [30, 31, 32, 39, 40, 41, 48, 49, 50],
            5: [57, 58, 59, 66, 67, 68, 75, 76, 77],
            6: [6, 7, 8, 15, 16, 17, 24, 25, 26],
            7: [33, 34, 35, 42, 43, 44, 51, 52, 53],
            8: [60, 61, 62, 69, 70, 71, 78, 79, 80]}

        self.bigTiles = {0: [0, 0], 1: [300, 0], 2: [600, 0],
                         3: [0, 300], 4: [300, 300], 5: [600, 300],
                         6: [0, 600], 7: [300, 600], 8: [600, 600]}
    @staticmethod
    def __transpose(i):
        d={0:0, 1:3, 2:6, 3:1, 4:4, 5:7, 6:2, 7:5, 8:8}
        return d[i]

    def teller(self, Tile_Num):  # Takes a tile number and returns the big tile to which it belongs
        for i in self.Dict:
            if Tile_Num in self.Dict[i]:
                return i

    def getList(self):
        L = []
        for i in range(81):
            L += [" "]
        return L

    def makeGridTiles(self, screen):
        L = []
        tl = tile_len
        color = TILE_INACTIVE

        for i in range(9):
            for j in range(9):
                coord = [tl * i, tl * j]
                Tile = pygame.draw.rect(screen, color, [coord[0], coord[1], tl, tl])
                L += [Tile]
        self.grid = L

    def drawActiveTiles(self):
        bigTileList=self.Dict[self.currentBigTile]
        tl = tile_len
        color=TILE_ACTIVE

        for i in bigTileList:
            Tile=self.grid[i]
            coord=[Tile.x, Tile.y]
            Tile = pygame.draw.rect(screen, color, [coord[0], coord[1], tl, tl])
            Type=self.L[i]
            if Type=="X":self.draw_X(i)
            if Type=="O":self.draw_O(i)



    def makeGridLines(self, screen):
        color=self.gridColor
        tl = tile_len
        for i in range(1, 9):
            width = 2
            if i % 3 == 0:
                width = 4
            pygame.draw.line(screen, color, [i * tl, 0], [i * tl, RES[0]], width)

        for j in range(1, 9):
            width = 2
            if j % 3 == 0:
                width = 4
            pygame.draw.line(screen, color, [0, j * tl], [RES[0], j * tl], width)

    def check_collision(self, mouse_pos, mouse_click):
        if not mouse_click: return [False, -1]

        for i in range(len(self.grid)):
            Tile = self.grid[i]

            if Tile.collidepoint(mouse_pos):
                return [True, i]

    def draw_X(self, Tile_Num, clock=None):  # i is the tile number   
        tl = tile_len
        bigTile_Num=self.teller(Tile_Num)
        color2=TILE_INACTIVE
        self.L[Tile_Num]="X"
        
        if bigTile_Num==self.currentBigTile:color2=TILE_ACTIVE
            
        Tile = self.grid[Tile_Num]
        a = (tl // 2) - 10
        center = [int(Tile.x + (tl // 2)), int(Tile.y + (tl // 2))]
        #T.drawActiveTiles()
        for i in range(0,(tl // 2) - 10,2):
            c1 = [center[0] - i, center[1] - i]
            c2 = [center[0] + i, center[1] + i]
            c3 = [center[0] + i, center[1] - i]
            c4 = [center[0] - i, center[1] + i]
            pygame.draw.line(screen, self.color, c1, c2, 7)
            pygame.draw.line(screen, self.color, c3, c4, 7)
            pygame.draw.circle(screen, color2, center, a, 6)
            if clock!=None:
                T.makeGridLines(screen)
                #T.drawActiveTiles()
                pygame.display.update()
                clock.tick(60)

    def draw_O(self, Tile_Num, clock=None):
        tl = tile_len
        a = (tl // 2) - 10
        bigTile_Num=self.teller(Tile_Num)
        color2=TILE_INACTIVE
        self.L[Tile_Num]="O"
        
        if bigTile_Num==self.currentBigTile:color2=TILE_ACTIVE
        Tile = self.grid[Tile_Num]
        center = [int(Tile.x + (tl // 2)), int(Tile.y + (tl // 2))]
        c1 = [center[0] - a, center[1] - a]
        c2 = [center[0] + a, center[1] + a]
        c3 = [center[0] + a, center[1] - a]
        c4 = [center[0] - a, center[1] + a]
        #T.drawActiveTiles()
        for i in range(7, (tl // 2) - 10, 2):
            pygame.draw.rect(screen, color2, [Tile.x + 5, Tile.y + 5, tl - 10, tl - 10])
            pygame.draw.circle(screen, self.color, center, i, 6)
            pygame.draw.line(screen, color2, c1, c2, 7)
            pygame.draw.line(screen, color2, c3, c4, 7)

            if clock!=None:
                T.makeGridLines(screen)
                pygame.display.update()
                clock.tick(60)

    def drawAllSymbols(self):
        
        for Tile_Num in range(len(self.L)):
            symbol=self.L[Tile_Num]
            if symbol==" ":continue
            if symbol=="X":self.draw_X(Tile_Num)
            if symbol=="O":self.draw_O(Tile_Num)

    def getNextBigTile(self, Tile_Num):
        bigTile_List=self.Dict[self.teller(Tile_Num)]
        x=bigTile_List.index(Tile_Num)
        x=self.__transpose(x)
        return x

    def check_Winner(self):
        wins=[[0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6], [0,3,6], [1,4,7], [2,5,8]]
        text=False
        
        for bigTile_Num in self.Dict:
            bigTile_List=self.Dict[bigTile_Num]
            for win in wins:
                w1,w2,w3=win[0], win[1], win[2]
                Tile_Num1=bigTile_List[w1]
                Tile_Num2=bigTile_List[w2]
                Tile_Num3=bigTile_List[w3]
                s1, s2, s3= self.L[Tile_Num1], self.L[Tile_Num2], self.L[Tile_Num3]
                s=s1+s2+s3
                if s=="XXX":
                    screen.fill(TILE_INACTIVE)
                    self.draw_X(40)
                    text="X"
                    
                if s=="OOO":
                    screen.fill(TILE_INACTIVE)
                    self.draw_O(40)
                    text="O"

        if text!=False:
            
            font=pygame.font.SysFont(None, 120)
            t=font.render("WON", True, self.color)
            screen.blit(t, [RES[0]//2-110, RES[1]//2+50])
            return text
        else:return False
                
                
            
            
        


run = True


T = TicTacToe(RES)

mouse_pos = 0
mouse_click = False
n = []
Turn=random.choice(["O","X"])
screen.fill(TILE_INACTIVE)
T.makeGridTiles(screen)
T.makeGridLines(screen)
pygame.display.update()
Won=False

while run:
    screen.fill(TILE_INACTIVE)
    for e in pygame.event.get():
        if e.type == QUIT: run = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE: run = False

        if e.type == MOUSEMOTION:
            mouse_pos = e.pos
        if e.type == MOUSEBUTTONDOWN:
            mouse_click = True
            has_not_clicked=True
        if e.type == MOUSEBUTTONUP:
            mouse_click = False

    Collision = T.check_collision(mouse_pos, mouse_click)
    is_clicked = Collision[0]
    Tile_Num = Collision[1]

    

    if (is_clicked and has_not_clicked) and (T.L[Tile_Num]==" "):
        if (T.currentBigTile==-1) or (T.teller(Tile_Num)==T.currentBigTile):
            T.makeGridLines(screen)
            T.currentBigTile=T.getNextBigTile(Tile_Num)
            if Turn=="X":
                T.draw_O(Tile_Num, clock)
                Turn="O"
            elif Turn=="O":
                T.draw_X(Tile_Num, clock)
                Turn="X"
            has_not_clicked=False
            Won=T.check_Winner()
            
            
    if T.currentBigTile==-1:continue
    T.gridColor=AllColors2[0]
    T.color=AllColors[0]
    AllColors=cycle(AllColors)
    AllColors2=cycle(AllColors2)

    
    T.drawActiveTiles()
            
    T.drawAllSymbols()
    T.makeGridLines(screen)

    #Won=T.check_Winner()
    T.check_Winner()

        
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
