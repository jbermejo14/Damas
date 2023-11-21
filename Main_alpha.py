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
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
turn = 1


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


    def __init__(self, posy, posx, pulsado):
        self.pulsado = pulsado
        self.top_rect = pygame.Rect((posy, posx),(75, 75))
        self.posy = posy
        self.posx = posx
        self.rect = pygame.draw.rect(gameDisplay, black, (self.posy, self.posx, 75, 75))


    def check_click(self):
        posm = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(posm):
            if pygame.mouse.get_pressed()[0] is True:
                self.select()
                

    def select(self):
        self.pulsado = True
        if self.pulsado == True:
            for i in square_list:
                if i.pulsado is True:
                    if i is not self:
                        i.pulsado = False


        for i in dama_list:
            if i.selected is True:
                for b in square_list:
                    if b in i.list:
                        if b is self:
                            global turn
                            aux_posy = self.posy
                            aux_posx = self.posx
                            name = 's' + str(len(square_list) + 1)
                            name = Square(i.posy, i.posx, False)
                            square_list.append(name)
                            i.posx = aux_posx
                            i.posy = aux_posy
                            i.top_rect = pygame.Rect((self.posy, self.posx), (75, 75))

                    if b in i.list2:
                        if b is self:
                            aux_posy = self.posy
                            aux_posx = self.posx
                            name = 's' + str(len(square_list) + 1)
                            name = Square(i.posy, i.posx, False)
                            square_list.append(name)
                            i.posx = aux_posx
                            i.posy = aux_posy
                            i.top_rect = pygame.Rect((self.posy, self.posx),(75, 75))


# DAMA CLASS
class Dama:

    def __init__(self, posy, posx, color, selected):
        self.list = []
        self.list2 = []
        self.selected = selected
        self.posy = posy
        self.posx = posx
        self.top_rect = pygame.Rect((self.posy, self.posx),(75, 75))
        self.color = color

        if self.color is red:
            gameDisplay.blit(damar, (self.posy, self.posx, 10, 10))
        elif self.color is blue:
            gameDisplay.blit(damab, (self.posy, self.posx, 10, 10))

        pygame.display.update()
    

    def check_click(self):
        global turn
        posm = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(posm):
            if pygame.mouse.get_pressed()[0] is True:
                self.select()
        
            else:
                if self.color is red:
                    gameDisplay.blit(damar, (self.posy, self.posx, 10, 10))
                elif self.color is blue:
                    gameDisplay.blit(damab, (self.posy, self.posx, 10, 10))
                pygame.display.update()

        
    def get_list(self):
            
            pos_list = []
            if self.color is blue:
                pos_list.append((self.posy - 75, self.posx - 75))
                pos_list.append((self.posy + 75, self.posx - 75))
            elif self.color is red:
                pos_list.append((self.posy + 75, self.posx + 75))
                pos_list.append((self.posy - 75, self.posx + 75))
            return pos_list

    def get_list2(self):
            
            pos_list = []
            if self.color is red:
                pos_list.append((self.posy - 75, self.posx - 75))
                pos_list.append((self.posy + 75, self.posx - 75))
            elif self.color is blue:
                pos_list.append((self.posy + 75, self.posx + 75))
                pos_list.append((self.posy - 75, self.posx + 75))
            return pos_list

    def select(self):
        self.selected = True
        aux_posx = ''
        aux_posy = ''
        self.list = self.get_list()
        for i in dama_list:
            aux_posy = i.posy
            aux_posx = i.posx
            if self.list[0] == (aux_posy, aux_posx):
                self.list[0] = i
            elif self.list[1] == (aux_posy, aux_posx):
                self.list[1] = i

        for i in square_list:
            aux_posy2 = i.posy
            aux_posx2 = i.posx
            if self.list[0] == (aux_posy2, aux_posx2):
                self.list[0] = i
            elif self.list[1] == (aux_posy2, aux_posx2):
                self.list[1] = i

          # TODO FINISH DAMA TOUCHING AND EATING
        for i in self.list:
            if isinstance(i, Dama) is True:
                self.list2 = i.get_list2()
                for b in square_list:
                    aux_posy2 = b.posy
                    aux_posx2 = b.posx
                    if self.list2[0] == (aux_posy2, aux_posx2):
                        self.list2[0] = b
                    elif self.list2[1] == (aux_posy2, aux_posx2):
                        self.list2[1] = b
                if self.list[0] == i:
                    for b in self.list2:
                        if isinstance(b, Square) is True:
                            if self.list2[0] == b:
                                print('izq')
                                print(self.list2)
                elif self.list[1] == i:
                    for b in self.list2:
                        if isinstance(b, Square) is True:
                            if self.list2[1] == b:
                                print('drch')
                                print(self.list2[1].posy, self.list2[1].posx)
                        
        if pygame.mouse.get_pressed()[0] is True:
            self.selected = True

        if self.selected == True:
        
            if self.color is red:
                gameDisplay.blit(damar2, (self.posy, self.posx, 10, 10))
            elif self.color is blue:
                gameDisplay.blit(damab2, (self.posy, self.posx, 10, 10))
            
            for i in dama_list:
                if i.selected is True:
                    if i is not self:
                        i.selected = False
                          
        pygame.display.update()


# RED DAMA CREATION
dr1 = Dama(225, 0, red, False)
dr2 = Dama(375, 0, red, False)
dr3 = Dama(525, 0, red, False)
dr4 = Dama(675, 0, red, False)
dr5 = Dama(150, 75, red, False)
dr6 = Dama(300, 75, red, False)
dr7 = Dama(450, 75, red, False)
dr8 = Dama(600, 75, red, False)
dr9 = Dama(225, 150, red, False)
dr10 = Dama(375, 150, red, False)
dr11 = Dama(525, 150, red, False)
dr12 = Dama(675, 150, red, False)


# BLUE DAMA CREATION
db1 = Dama(150, 375, blue, False)
db2 = Dama(300, 375, blue, False)
db3 = Dama(450, 375, blue, False)
db4 = Dama(600, 375, blue, False)
db5 = Dama(225, 450, blue, False)
db6 = Dama(375, 450, blue, False)
db7 = Dama(525, 450, blue, False)
db8 = Dama(675, 450, blue, False)
db9 = Dama(150, 525, blue, False)
db10 = Dama(300, 525, blue, False)
db11 = Dama(450, 525, blue, False)
db12 = Dama(600, 525, blue, False)


# BOARD CREATION
s1 = Square(150, 225, False)
s2 = Square(300, 225, False)
s3 = Square(450, 225, False)
s4 = Square(600, 225, False)
s5 = Square(225, 300, False)
s6 = Square(375, 300, False)
s7 = Square(525, 300, False)
s8 = Square(675, 300, False)


# SQUARE LIST
square_list = [s1, s2, s3, s4, s5, s6, s7, s8]

# ALL DAMA LIST
dama_list = [dr1, dr2, dr3, dr4, dr5, dr6, dr7, dr8, dr9, dr10, dr11, dr12, db1, db2, db3, db4, db5, db6, db7, db8, db9, db10, db11, db12]

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#TODO FINISH EATING AND TURNOS(IT CAN WAIT)