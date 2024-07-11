# IMPORTS
import sys
import pygame
import checker
from checker import Checker
from square import *

# IMAGES GENERATION
bg = pygame.image.load("images/bg.png")
red_checker = pygame.image.load("images/red_checker.jpg")
blue_checker = pygame.image.load("images/blue_checker.jpg")
red_checker_2 = pygame.image.load("images/red_checker_2.jpg")
blue_checker_2 = pygame.image.load("images/blue_checker_2.jpg")
blue_queen = pygame.image.load("images/blue_queen.jpg")
blue_queen_2 = pygame.image.load("images/blue_queen_2.jpg")
red_queen = pygame.image.load("images/red_queen.jpg")
red_queen_2 = pygame.image.load("images/red_queen_2.jpg")

# COLOR GENERATION
black = pygame.Color(0, 0, 0)
red = pygame.Color(237, 27, 36)
blue = pygame.Color(0, 163, 232)
turn = 'blue'
eated = None
Global_has_to_eat = False

# DISPLAY GENERATION
gameDisplay = pygame.display.set_mode((900, 600))
pygame.init()
pygame.display.set_caption("Checkers")
gameExit = False
gameDisplay.fill('white')
pygame.draw.rect(gameDisplay, black, (750, 0, 150, 600))
pygame.draw.rect(gameDisplay, black, (0, 0, 150, 600))

# RED DAMA CREATION
dr1 = Checker((225, 0), red, 'red')
dr2 = Checker((375, 0), red, 'red')
dr3 = Checker((525, 0), red, 'red')
dr4 = Checker((675, 0), red, 'red')
dr5 = Checker((150, 75), red, 'red')
dr6 = Checker((300, 75), red, 'red')
dr7 = Checker((450, 75), red, 'red')
dr8 = Checker((600, 75), red, 'red')
dr9 = Checker((225, 150), red, 'red')
dr10 = Checker((375, 150), red, 'red')
dr11 = Checker((525, 150), red, 'red')
dr12 = Checker((675, 150), red, 'red')

# BLUE DAMA CREATION
db1 = Checker((150, 375), blue, 'blue')
db2 = Checker((300, 375), blue, 'blue')
db3 = Checker((450, 375), blue, 'blue')
db4 = Checker((600, 375), blue, 'blue')
db5 = Checker((225, 450), blue, 'blue')
db6 = Checker((375, 450), blue, 'blue')
db7 = Checker((525, 450), blue, 'blue')
db8 = Checker((675, 450), blue, 'blue')
db9 = Checker((150, 525), blue, 'blue')
db10 = Checker((300, 525), blue, 'blue')
db11 = Checker((450, 525), blue, 'blue')
db12 = Checker((600, 525), blue, 'blue')

# BOARD CREATION
s1 = Square((150, 225))
s2 = Square((300, 225))
s3 = Square((450, 225))
s4 = Square((600, 225))
s5 = Square((225, 300))
s6 = Square((375, 300))
s7 = Square((525, 300))
s8 = Square((675, 300))

# SQUARE LIST
square_list = [s1, s2, s3, s4, s5, s6, s7, s8]

# ALL DAMA LIST
checker_list = [dr1, dr2, dr3, dr4, dr5, dr6, dr7, dr8, dr9, dr10, dr11, dr12, db1, db2, db3, db4, db5, db6, db7, db8,
                db9,
                db10, db11, db12]

# RED DAMA LIST
red_checker_list = [dr1, dr2, dr3, dr4, dr5, dr6, dr7, dr8, dr9, dr10, dr11, dr12]

# BLUE DAMA LIST
blue_checker_list = [db1, db2, db3, db4, db5, db6, db7, db8, db9, db10, db11, db12]


def blue_checker_click_checks():
    for i in checker_list:
        i.check_click()


def board_click_checks():
    for i in square_list:
        i.check_click()


pygame.display.update()

while not gameExit:

    board_click_checks()
    blue_checker_click_checks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

################################################################
# TODO
#
# ERROR IN EATING,  IN DAMA.SELECT(), SELF.AUX_LIST NOT WORKING WELL (IT AFFECTS TO EATING AND THE SQUARE PAINTING)
#
# QUEEN ONLY GOES 2 SQUARES AT A TIME AND CAN'T EAT IN DISTANCE
# QUEEN OBLIGATION TO EAT NEEDS SELF.LIST FIXED, IT USES GET_LIST() IT NEED TO USE THE QUEEN() LIST METHOD
#
#
#
################################################################
