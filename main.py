# IMPORTS
import pygame
import button
import sys


gameDisplay = pygame.display.set_mode((600, 600))
bg = pygame.image.load("images/bg.png")
daman = pygame.image.load("images/dama_roja.jpg")

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# DISPLAY GENERTATION
pygame.init()
pygame.display.set_caption("Damas")
gameExit = False


class Square:
    def __init__(self, posy, posx):
        self.posy = posy
        self.posx = posx
        self.rect = pygame.draw.rect(gameDisplay, white, (self.posy, self.posx, 75, 75))

class Dama:
    def __init__(self, posy, posx):
        self.posy = posy
        self.posx = posx

    def creation(self):
        gameDisplay.blit(daman, (self.posy, self.posx, 10, 10))
        pygame.display.update()
    
    def clicked(self):
        posm = pygame.mouse.get_pos()
        print(posm)


def check_creation():
    y = 0
    x = 0

    # ROW 0 
    for i in range(4):
        i = Dama(y, x)
        i.creation()
        y = y + 150
        pygame.display.update()
        print(i.posy, i.posx)

def board_creation():
    y = 0
    x = 0

    # ROW 0 
    for i in range(4):
        i = Square(y, x)
        i.rect
        y = y + 150
        pygame.display.update()
        print(i.posy, i.posx)

board_creation()
# check_creation()

daman1 = Dama

while not gameExit:
    posm = pygame.mouse.get_pos()
    print(posm)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            posm == 
