# IMPORTS
import pygame
import sys
import time

# IMAGES GENERATION
bg = pygame.image.load("images/bg.png")
damar = pygame.image.load("images/dama_roja.jpg")
damab = pygame.image.load("images/dama_blue.jpg")
damar2 = pygame.image.load("images/dama_roja2.jpg")
damab2 = pygame.image.load("images/dama_blue2.jpg")

# COLOR GENERATION
black = pygame.Color(0, 0, 0)
red = pygame.Color(237, 27, 36)
blue = pygame.Color(0, 163, 232)
turn = 'blue'
red_counter = 0
blue_counter = 0
eated = None

# DISPLAY GENERATION
gameDisplay = pygame.display.set_mode((900, 600))
pygame.init()
pygame.display.set_caption("Damas")
gameExit = False
gameDisplay.fill('white')
pygame.draw.rect(gameDisplay, black, (750, 0, 150, 600))
pygame.draw.rect(gameDisplay, black, (0, 0, 150, 600))

# SQUARE CLASS
class Square:
    def __init__(self, pos):
        self.top_rect = pygame.Rect(pos, (75, 75))
        self.pos = pos
        self.rect = pygame.draw.rect(gameDisplay, black, (self.pos[0], self.pos[1], 75, 75))

    def check_click(self):
        posm = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(posm):
            if pygame.mouse.get_pressed()[0] is True:
                self.select()

    def select(self):
        global turn, eated, red_counter, blue_counter
        for i in dama_list:
            if i.selected is True:
                for b in square_list:
                    if b in i.list:
                        if b is self:
                            if turn == i.turn:
                                aux_pos = self.pos
                                name = Square(i.pos)
                                square_list.append(name)
                                i.pos = aux_pos
                                i.top_rect = pygame.Rect(self.pos, (75, 75))
                                if i.color == blue:
                                    if i.pos[1] == 0:
                                        print("Heeey")
                                elif i.color == red:
                                    if i.pos[1] == 525:
                                        print("Heeey")
                                if turn == 'blue':
                                    turn = 'red'
                                elif turn == 'red':
                                    turn = 'blue'

                    if b in i.aux_list:
                        if b is self:
                            if turn == i.turn:
                                aux_pos = self.pos
                                name = Square(i.pos)
                                square_list.append(name)
                                i.pos = aux_pos
                                i.top_rect = pygame.Rect(self.pos, (75, 75))
                                for c in dama_list:
                                    if c.pos == eated:
                                        name = Square(c.pos)
                                        square_list.append(name)
                                        c.pos = (0, 0)
                                        c.top_rect = pygame.Rect(c.pos, (75, 75))
                                        if turn == 'blue':
                                            red_counter = red_counter + 1
                                            print(red_counter)
                                        elif turn == 'red':
                                            blue_counter = blue_counter + 1
                                            print(blue_counter)
                                        pygame.draw.rect(gameDisplay, black, (750, 0, 150, 600))
                                        pygame.draw.rect(gameDisplay, black, (0, 0, 150, 600))
                                        i.double_eat()
                                if i.color == blue:
                                    if i.pos[1] == 0:
                                        print("Heeey")
                                elif i.color == red:
                                    if i.pos[1] == 525:
                                        print("Heeey")
                                if turn == 'blue':
                                    turn = 'red'
                                elif turn == 'red':
                                    turn = 'blue'

# DAMA CLASS
class Dama:

    def __init__(self, pos, color, selected, turn):
        self.turn = turn
        self.list = []
        self.list2 = []
        self.aux_list = []
        self.selected = selected
        self.pos = pos
        self.top_rect = pygame.Rect(self.pos, (75, 75))
        self.color = color

        if self.color is red:
            gameDisplay.blit(damar, (self.pos[0], self.pos[1], 10, 10))
        elif self.color is blue:
            gameDisplay.blit(damab, (self.pos[0], self.pos[1], 10, 10))

        pygame.display.update()

    def check_click(self):
        posm = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(posm):
            if pygame.mouse.get_pressed()[0] is True:
                self.select()
            else:
                if self.color is red:
                    gameDisplay.blit(damar, (self.pos[0], self.pos[1], 10, 10))
                elif self.color is blue:
                    gameDisplay.blit(damab, (self.pos[0], self.pos[1], 10, 10))
                pygame.display.update()

    def get_list(self):
        pos_list = []
        if self.color is blue:
            pos_list.append((self.pos[0] - 75, self.pos[1] - 75))
            pos_list.append((self.pos[0] + 75, self.pos[1] - 75))
        elif self.color is red:
            pos_list.append((self.pos[0] + 75, self.pos[1] + 75))
            pos_list.append((self.pos[0] - 75, self.pos[1] + 75))
        return pos_list

    def get_list2(self):
        pos_list = []
        if self.color is red:
            pos_list.append((self.pos[0] - 75, self.pos[1] - 75))
            pos_list.append((self.pos[0] + 75, self.pos[1] - 75))
        elif self.color is blue:
            pos_list.append((self.pos[0] + 75, self.pos[1] + 75))
            pos_list.append((self.pos[0] - 75, self.pos[1] + 75))
        return pos_list

    def double_eat(self):
        global eated, turn
        self.aux_list = []
        self.selected = True
        self.list = self.get_list()
        for i in dama_list:
            aux_pos = i.pos
            if self.list[0] == aux_pos:
                self.list[0] = i
            elif self.list[1] == aux_pos:
                self.list[1] = i

        for i in square_list:
            aux_pos2 = i.pos
            if self.list[0] == aux_pos2:
                self.list[0] = i
            elif self.list[1] == aux_pos2:
                self.list[1] = i

        for i in self.list:
            if isinstance(i, Dama) is True:
                if self.color is red:
                    if i.color is blue:
                        self.list2 = i.get_list2()
                        for b in square_list:
                            aux_pos2 = b.pos
                            if self.list2[0] == aux_pos2:
                                self.list2[0] = b
                            elif self.list2[1] == aux_pos2:
                                self.list2[1] = b

                        for b in dama_list:
                            aux_pos2 = b.pos
                            if self.list2[0] == aux_pos2:
                                self.list2[0] = i
                            elif self.list2[1] == aux_pos2:
                                self.list2[1] = i

                        if self.list[0] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[0] == b:
                                        self.aux_list.append(b)

                        elif self.list[1] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[1] == b:
                                        self.aux_list.append(b)

                elif self.color is blue:
                    if i.color is red:
                        self.list2 = i.get_list2()
                        for b in square_list:
                            aux_pos2 = b.pos
                            if self.list2[0] == aux_pos2:
                                self.list2[0] = b
                            elif self.list2[1] == aux_pos2:
                                self.list2[1] = b

                        for b in dama_list:
                            aux_pos2 = b.pos
                            if self.list2[0] == aux_pos2:
                                self.list2[0] = i
                            elif self.list2[1] == aux_pos2:
                                self.list2[1] = i

                        if self.list[0] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[0] == b:
                                        self.aux_list.append(b)

                        elif self.list[1] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[1] == b:
                                        self.aux_list.append(b)

        for i in self.aux_list:
            if isinstance(i, Square) is True:
                self.selected = True
            if turn == 'blue':
                turn = 'red'
            elif turn == 'red':
                turn = 'blue'

    def select(self):
        global turn, eated
        self.aux_list = []
        self.selected = True
        self.list = self.get_list()
        for i in dama_list:
            aux_pos = i.pos
            if self.list[0] == aux_pos:
                self.list[0] = i
            elif self.list[1] == aux_pos:
                self.list[1] = i

        for i in square_list:
            aux_pos2 = i.pos
            if self.list[0] == aux_pos2:
                self.list[0] = i
            elif self.list[1] == aux_pos2:
                self.list[1] = i

        for i in self.list:
            if isinstance(i, Dama) is True:
                if self.color is red:
                    if i.color is blue:
                        self.list2 = i.get_list2()
                        for b in square_list:
                            aux_pos2 = b.pos
                            if self.list2[0] == aux_pos2:
                                self.list2[0] = b
                            elif self.list2[1] == aux_pos2:
                                self.list2[1] = b

                        for b in dama_list:
                            aux_pos2 = b.pos
                            if self.list2[0] == aux_pos2:
                                self.list2[0] = i
                            elif self.list2[1] == aux_pos2:
                                self.list2[1] = i

                        if self.list[0] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[0] == b:
                                        self.aux_list.append(b)
                                        eated = i.pos

                        elif self.list[1] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[1] == b:
                                        self.aux_list.append(b)
                                        eated = i.pos

                elif self.color is blue:
                    if i.color is red:
                        self.list2 = i.get_list2()
                        for b in square_list:
                            aux_pos2 = b.pos
                            if self.list2[0] == aux_pos2:
                                self.list2[0] = b
                            elif self.list2[1] == aux_pos2:
                                self.list2[1] = b

                        for b in dama_list:
                            aux_pos2 = b.pos
                            if self.list2[0] == aux_pos2:
                                self.list2[0] = i
                            elif self.list2[1] == aux_pos2:
                                self.list2[1] = i

                        if self.list[0] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[0] == b:
                                        self.aux_list.append(b)
                                        eated = i.pos

                        elif self.list[1] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[1] == b:
                                        self.aux_list.append(b)
                                        eated = i.pos
        for i in dama_list:
            if i.selected is True:
                if i is not self:
                    i.selected = False
        if pygame.mouse.get_pressed()[0] is True:
            if self.color is red:
                gameDisplay.blit(damar2, (self.pos[0], self.pos[1], 10, 10))
            elif self.color is blue:
                gameDisplay.blit(damab2, (self.pos[0], self.pos[1], 10, 10))

        pygame.display.update()

# RED DAMA CREATION
dr1 = Dama((225, 0), red, False, 'red')
dr2 = Dama((375, 0), red, False, 'red')
dr3 = Dama((525, 0), red, False, 'red')
dr4 = Dama((675, 0), red, False, 'red')
dr5 = Dama((150, 75), red, False, 'red')
dr6 = Dama((300, 75), red, False, 'red')
dr7 = Dama((450, 75), red, False, 'red')
dr8 = Dama((600, 75), red, False, 'red')
dr9 = Dama((225, 150), red, False, 'red')
dr10 = Dama((375, 150), red, False, 'red')
dr11 = Dama((525, 150), red, False, 'red')
dr12 = Dama((675, 150), red, False, 'red')

# BLUE DAMA CREATION
db1 = Dama((150, 375), blue, False, 'blue')
db2 = Dama((300, 375), blue, False, 'blue')
db3 = Dama((450, 375), blue, False, 'blue')
db4 = Dama((600, 375), blue, False, 'blue')
db5 = Dama((225, 450), blue, False, 'blue')
db6 = Dama((375, 450), blue, False, 'blue')
db7 = Dama((525, 450), blue, False, 'blue')
db8 = Dama((675, 450), blue, False, 'blue')
db9 = Dama((150, 525), blue, False, 'blue')
db10 = Dama((300, 525), blue, False, 'blue')
db11 = Dama((450, 525), blue, False, 'blue')
db12 = Dama((600, 525), blue, False, 'blue')

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
dama_list = [dr1, dr2, dr3, dr4, dr5, dr6, dr7, dr8, dr9, dr10, dr11, dr12, db1, db2, db3, db4, db5, db6, db7, db8, db9,
             db10, db11, db12]

# RED DAMA LIST
damar_list = [dr1, dr2, dr3, dr4, dr5, dr6, dr7, dr8, dr9, dr10, dr11, dr12]

# BLUE DAMA LIST
damab_list = [db1, db2, db3, db4, db5, db6, db7, db8, db9, db10, db11, db12]

def damab_click_checks():
    for i in dama_list:
        i.check_click()

def board_click_checks():
    for i in square_list:
        i.check_click()

pygame.display.update()

while not gameExit:

    board_click_checks()
    damab_click_checks()

    font = pygame.font.SysFont(None, 150)
    img1 = font.render(str(red_counter), True, blue)
    gameDisplay.blit(img1, (800, 260))

    img2 = font.render(str(blue_counter), True, red)
    gameDisplay.blit(img2, (50, 260))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

################################################################
# TODO
#
# Add Queen
#
###################################################################