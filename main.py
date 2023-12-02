# IMPORTS
import pygame
import sys

# IMAGES GENERATION
bg = pygame.image.load("images/bg.png")
damar = pygame.image.load("images/dama_roja.jpg")
damab = pygame.image.load("images/dama_blue.jpg")
damar2 = pygame.image.load("images/dama_roja2.jpg")
damab2 = pygame.image.load("images/dama_blue2.jpg")
queenb = pygame.image.load("images/queen_blue.jpg")
queenb2 = pygame.image.load("images/queen_blue2.jpg")
queenr = pygame.image.load("images/queen_roja.jpg")
queenr2 = pygame.image.load("images/queen_roja2.jpg")

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
        global turn, eated, Global_has_to_eat
        for i in dama_list:
            if i.selected is True:
                for b in square_list:
                    if b in i.list:
                        if b is self:
                            if turn == i.turn:
                                if Global_has_to_eat == True:
                                    if i.has_to_eat == True:
                                        aux_pos = self.pos
                                        name = Square(i.pos)
                                        square_list.append(name)
                                        i.pos = aux_pos
                                        i.top_rect = pygame.Rect(self.pos, (75, 75))
                                        if i.color == blue:
                                            if i.pos[1] == 0:
                                                i.queen()
                                        elif i.color == red:
                                            if i.pos[1] == 525:
                                                i.queen()
                                        if turn == 'blue':
                                            turn = 'red'
                                        elif turn == 'red':
                                            turn = 'blue'
                                        for i in dama_list:
                                            i.has_to_eat = False
                                        Global_has_to_eat = False
                                else:
                                    aux_pos = self.pos
                                    name = Square(i.pos)
                                    square_list.append(name)
                                    i.pos = aux_pos
                                    i.top_rect = pygame.Rect(self.pos, (75, 75))
                                    if i.color == blue:
                                        if i.pos[1] == 0:
                                            i.queen()
                                    elif i.color == red:
                                        if i.pos[1] == 525:
                                            i.queen()
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
                                        i.top_rect = pygame.Rect(c.pos, (75, 75))
                                        c.pos = (-75, 0)
                                        c.top_rect = pygame.Rect(c.pos, (75, 75))
                                        pygame.draw.rect(gameDisplay, black, (750, 0, 150, 600))
                                        pygame.draw.rect(gameDisplay, black, (0, 0, 150, 600))
                                        if i.is_queen is True:
                                            i.queen_double_eat()
                                        else:
                                            i.double_eat()
                                if i.color == blue:
                                    if i.pos[1] == 0:
                                        i.queen()
                                elif i.color == red:
                                    if i.pos[1] == 525:
                                        i.queen()
                                if turn == 'blue':
                                    turn = 'red'
                                elif turn == 'red':
                                    turn = 'blue'
                            Global_has_to_eat = False
                for i in square_list:
                    for b in damab_list:
                        i.rect = pygame.draw.rect(gameDisplay, black, (i.pos[0], i.pos[1], 75, 75))
                        gameDisplay.blit(damab, (b.pos[0], b.pos[1], 10, 10))
                    for b in damar_list:
                        i.rect = pygame.draw.rect(gameDisplay, black, (i.pos[0], i.pos[1], 75, 75))
                        gameDisplay.blit(damar, (b.pos[0], b.pos[1], 10, 10))

# DAMA CLASS
class Dama:

    def __init__(self, pos, color, turn):
        self.has_to_eat = False
        self.turn = turn
        self.list = []
        self.list2 = []
        self.aux_list = []
        self.selected = False
        self.pos = pos
        self.top_rect = pygame.Rect(self.pos, (75, 75))
        self.color = color
        self.is_queen = False

        if self.color is red:
            gameDisplay.blit(damar, (self.pos[0], self.pos[1], 10, 10))
        elif self.color is blue:
            gameDisplay.blit(damab, (self.pos[0], self.pos[1], 10, 10))

        pygame.display.update()

    def check_has_to_eat(self):
        global Global_has_to_eat
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

                if self.color is red:
                    if i.color is blue:
                        if self.list[0] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[0] == b:
                                        print(self.pos, "Has to eat")
                                        self.has_to_eat = True
                                        Global_has_to_eat = True
                        elif self.list[1] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[1] == b:
                                        print(self.pos, "Has to eat")
                                        self.has_to_eat = True
                                        Global_has_to_eat = True

                elif self.color is blue:
                    if i.color is red:
                        if self.list[0] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[0] == b:
                                        print(self.pos, "Has to eat")
                                        self.has_to_eat = True
                                        Global_has_to_eat = True

                        elif self.list[1] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[1] == b:
                                        print(self.pos, "Has to eat")
                                        self.has_to_eat = True
                                        Global_has_to_eat = True

    def queen_check_has_to_eat(self):
        global Global_has_to_eat
        self.aux_list = []
        self.list = []
        self.selected = True

        self.list.append((self.pos[0] - 75, self.pos[1] - 75))
        self.list.append((self.pos[0] + 75, self.pos[1] - 75))
        self.list.append((self.pos[0] + 75, self.pos[1] + 75))
        self.list.append((self.pos[0] - 75, self.pos[1] + 75))

        for i in square_list:
            if self.list[0] == i.pos:
                self.list.append((self.pos[0] - 150, self.pos[1] - 150))
            elif self.list[1] == i.pos:
                self.list.append((self.pos[0] + 150, self.pos[1] - 150))
            elif self.list[2] == i.pos:
                self.list.append((self.pos[0] + 150, self.pos[1] + 150))
            elif self.list[3] == i.pos:
                self.list.append((self.pos[0] - 150, self.pos[1] + 150))

        for i in dama_list:
            aux_pos = i.pos
            if self.list[0] == aux_pos:
                self.list[0] = i
            elif self.list[1] == aux_pos:
                self.list[1] = i
            elif self.list[2] == aux_pos:
                self.list[2] = i
            elif self.list[3] == aux_pos:
                self.list[3] = i

        print(self.list)
        n = 0
        for i in self.list:
            for b in square_list:
                if self.list[n] == b.pos:
                    self.list[n] = b
            n = n + 1
            print(n)

        for i in self.list:
            if isinstance(i, Dama) is True:
                self.list2 = i.get_list_queen2()
                for b in square_list:
                    aux_pos2 = b.pos
                    if self.list2[0] == aux_pos2:
                        self.list2[0] = b
                    elif self.list2[1] == aux_pos2:
                        self.list2[1] = b
                    elif self.list2[2] == aux_pos2:
                        self.list2[2] = b
                    elif self.list2[3] == aux_pos2:
                        self.list2[3] = b

                for b in dama_list:
                    aux_pos2 = b.pos
                    if self.list2[0] == aux_pos2:
                        self.list2[0] = b
                    elif self.list2[1] == aux_pos2:
                        self.list2[1] = b
                    elif self.list2[2] == aux_pos2:
                        self.list2[2] = b
                    elif self.list2[3] == aux_pos2:
                        self.list2[3] = b

                if self.color is red:
                    if i.color is blue:
                        if self.list[0] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[0] == b:
                                        self.has_to_eat = True
                                        Global_has_to_eat = True

                        elif self.list[1] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[1] == b:
                                        self.has_to_eat = True
                                        Global_has_to_eat = True

                        elif self.list[2] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[2] == b:
                                        self.has_to_eat = True
                                        Global_has_to_eat = True

                        elif self.list[3] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[3] == b:
                                        self.has_to_eat = True
                                        Global_has_to_eat = True

                elif self.color is blue:
                    if i.color is red:
                        if self.list[0] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[0] == b:
                                        self.has_to_eat = True
                                        Global_has_to_eat = True

                        elif self.list[1] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[1] == b:
                                        self.has_to_eat = True
                                        Global_has_to_eat = True

                        elif self.list[2] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[2] == b:
                                        self.has_to_eat = True
                                        Global_has_to_eat = True

                        elif self.list[3] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[3] == b:
                                        self.has_to_eat = True
                                        Global_has_to_eat = True

    def check_click(self):
        posm = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(posm):
            if pygame.mouse.get_pressed()[0] is True:
                if self.is_queen is True:
                    self.queen()
                elif self.is_queen is False:
                    self.select()
            else:
                if self.is_queen is True:
                    if self.color is red:
                        gameDisplay.blit(queenr, (self.pos[0], self.pos[1], 10, 10))
                    elif self.color is blue:
                        gameDisplay.blit(queenb, (self.pos[0], self.pos[1], 10, 10))

                elif self.is_queen is False:
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

    def get_list_queen(self):
        pos_list = [(self.pos[0] - 75, self.pos[1] - 75), (self.pos[0] + 75, self.pos[1] - 75),
                    (self.pos[0] + 75, self.pos[1] + 75), (self.pos[0] - 75, self.pos[1] + 75)]
        return pos_list

    def get_list_queen2(self):
        pos_list = [(self.pos[0] - 75, self.pos[1] - 75), (self.pos[0] + 75, self.pos[1] - 75),
                    (self.pos[0] + 75, self.pos[1] + 75), (self.pos[0] - 75, self.pos[1] + 75)]
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

    def queen_double_eat(self):
        global eated, turn
        self.aux_list = []
        self.selected = True
        self.list = self.get_list_queen()
        for i in dama_list:
            aux_pos = i.pos
            if self.list[0] == aux_pos:
                self.list[0] = i
            elif self.list[1] == aux_pos:
                self.list[1] = i
            elif self.list[2] == aux_pos:
                self.list[2] = i
            elif self.list[3] == aux_pos:
                self.list[3] = i

        for i in square_list:
            aux_pos2 = i.pos
            if self.list[0] == aux_pos2:
                self.list[0] = i
            elif self.list[1] == aux_pos2:
                self.list[1] = i
            elif self.list[2] == aux_pos2:
                self.list[2] = i
            elif self.list[3] == aux_pos2:
                self.list[3] = i

        for i in self.list:
            if isinstance(i, Dama) is True:
                if self.color is red:
                    self.list2 = i.get_list_queen2()
                    for b in square_list:
                        aux_pos2 = b.pos
                        if self.list2[0] == aux_pos2:
                            self.list2[0] = b
                        elif self.list2[1] == aux_pos2:
                            self.list2[1] = b
                        elif self.list2[2] == aux_pos2:
                            self.list2[2] = b
                        elif self.list2[3] == aux_pos2:
                            self.list2[3] = b

                    for b in dama_list:
                        aux_pos2 = b.pos
                        if self.list2[0] == aux_pos2:
                            self.list2[0] = b
                        elif self.list2[1] == aux_pos2:
                            self.list2[1] = b
                        elif self.list2[2] == aux_pos2:
                            self.list2[2] = b
                        elif self.list2[3] == aux_pos2:
                            self.list2[3] = b

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

                        elif self.list[2] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[2] == b:
                                        self.aux_list.append(b)

                        elif self.list[3] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[3] == b:
                                        self.aux_list.append(b)

                elif self.color is blue:
                    if i.color is red:
                        self.list2 = i.get_list_queen2()
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

                        elif self.list[2] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[2] == b:
                                        self.aux_list.append(b)

                        elif self.list[3] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[3] == b:
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
            i.check_has_to_eat()
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
        if self.color is blue:
            if turn is 'blue':
                if pygame.mouse.get_pressed()[0] is True:
                    for i in square_list:
                        if i in self.list:
                            i.rect = pygame.draw.rect(gameDisplay, blue, (i.pos[0], i.pos[1], 75, 75))
                        elif i in self.aux_list:
                            i.rect = pygame.draw.rect(gameDisplay, blue, (i.pos[0], i.pos[1], 75, 75))
                        else:
                            for b in damab_list:
                                i.rect = pygame.draw.rect(gameDisplay, black, (i.pos[0], i.pos[1], 75, 75))
                                gameDisplay.blit(damab, (b.pos[0], b.pos[1], 10, 10))
                            for b in damar_list:
                                i.rect = pygame.draw.rect(gameDisplay, black, (i.pos[0], i.pos[1], 75, 75))
                                gameDisplay.blit(damar, (b.pos[0], b.pos[1], 10, 10))
                    gameDisplay.blit(damab2, (self.pos[0], self.pos[1], 10, 10))
                    pygame.display.update()

        elif self.color is red:
            if turn is 'red':
                if pygame.mouse.get_pressed()[0] is True:
                    for i in square_list:
                        if i in self.list:
                            i.rect = pygame.draw.rect(gameDisplay, blue, (i.pos[0], i.pos[1], 75, 75))
                        elif i in self.aux_list:
                            i.rect = pygame.draw.rect(gameDisplay, blue, (i.pos[0], i.pos[1], 75, 75))
                        else:
                            for b in damab_list:
                                i.rect = pygame.draw.rect(gameDisplay, black, (i.pos[0], i.pos[1], 75, 75))
                                gameDisplay.blit(damab, (b.pos[0], b.pos[1], 10, 10))
                            for b in damar_list:
                                i.rect = pygame.draw.rect(gameDisplay, black, (i.pos[0], i.pos[1], 75, 75))
                                gameDisplay.blit(damar, (b.pos[0], b.pos[1], 10, 10))
                    gameDisplay.blit(damar2, (self.pos[0], self.pos[1], 10, 10))

        for i in dama_list:
            if i is not self:
                i.selected = False

        pygame.display.update()

    def queen(self):
        self.is_queen = True
        global turn, eated
        self.aux_list = []
        self.list = []
        self.selected = True

        self.list.append((self.pos[0] - 75, self.pos[1] - 75))
        self.list.append((self.pos[0] + 75, self.pos[1] - 75))
        self.list.append((self.pos[0] + 75, self.pos[1] + 75))
        self.list.append((self.pos[0] - 75, self.pos[1] + 75))

        for i in square_list:
            if self.list[0] == i.pos:
                self.list.append((self.pos[0] - 150, self.pos[1] - 150))
            elif self.list[1] == i.pos:
                self.list.append((self.pos[0] + 150, self.pos[1] - 150))
            elif self.list[2] == i.pos:
                self.list.append((self.pos[0] + 150, self.pos[1] + 150))
            elif self.list[3] == i.pos:
                self.list.append((self.pos[0] - 150, self.pos[1] + 150))

        for i in dama_list:
            i.queen_check_has_to_eat()
            aux_pos = i.pos
            if self.list[0] == aux_pos:
                self.list[0] = i
            elif self.list[1] == aux_pos:
                self.list[1] = i
            elif self.list[2] == aux_pos:
                self.list[2] = i
            elif self.list[3] == aux_pos:
                self.list[3] = i

        print(self.list)
        n = 0
        for i in self.list:
            for b in square_list:
                if self.list[n] == b.pos:
                    self.list[n] = b
            n = n + 1
            print(n)

        for i in self.list:
            if isinstance(i, Dama) is True:
                self.list2 = i.get_list_queen2()
                for b in square_list:
                    aux_pos2 = b.pos
                    if self.list2[0] == aux_pos2:
                        self.list2[0] = b
                    elif self.list2[1] == aux_pos2:
                        self.list2[1] = b
                    elif self.list2[2] == aux_pos2:
                        self.list2[2] = b
                    elif self.list2[3] == aux_pos2:
                        self.list2[3] = b

                for b in dama_list:
                    aux_pos2 = b.pos
                    if self.list2[0] == aux_pos2:
                        self.list2[0] = b
                    elif self.list2[1] == aux_pos2:
                        self.list2[1] = b
                    elif self.list2[2] == aux_pos2:
                        self.list2[2] = b
                    elif self.list2[3] == aux_pos2:
                        self.list2[3] = b

                if self.color is red:
                    if i.color is blue:
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

                        elif self.list[2] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[2] == b:
                                        self.aux_list.append(b)
                                        eated = i.pos

                        elif self.list[3] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[3] == b:
                                        self.aux_list.append(b)
                                        eated = i.pos

                elif self.color is blue:
                    if i.color is red:
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

                        elif self.list[2] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[2] == b:
                                        self.aux_list.append(b)
                                        eated = i.pos

                        elif self.list[3] == i:
                            for b in self.list2:
                                if isinstance(b, Square) is True:
                                    if self.list2[3] == b:
                                        self.aux_list.append(b)
                                        eated = i.pos
        for i in dama_list:
            if i.selected is True:
                if i is not self:
                    i.selected = False

        if pygame.mouse.get_pressed()[0] is True:
            if self.is_queen is True:
                if self.color is red:
                    gameDisplay.blit(queenr2, (self.pos[0], self.pos[1], 10, 10))
                elif self.color is blue:
                    gameDisplay.blit(queenb2, (self.pos[0], self.pos[1], 10, 10))
            elif self.is_queen is False:
                if self.color is red:
                    gameDisplay.blit(damar2, (self.pos[0], self.pos[1], 10, 10))
                elif self.color is blue:
                    gameDisplay.blit(damab2, (self.pos[0], self.pos[1], 10, 10))

        pygame.display.update()


# RED DAMA CREATION
dr1 = Dama((225, 0), red, 'red')
dr2 = Dama((375, 0), red, 'red')
dr3 = Dama((525, 0), red, 'red')
dr4 = Dama((675, 0), red, 'red')
dr5 = Dama((150, 75), red, 'red')
dr6 = Dama((300, 75), red, 'red')
dr7 = Dama((450, 75), red, 'red')
dr8 = Dama((600, 75), red, 'red')
dr9 = Dama((225, 150), red, 'red')
dr10 = Dama((375, 150), red, 'red')
dr11 = Dama((525, 150), red, 'red')
dr12 = Dama((675, 150), red, 'red')

# BLUE DAMA CREATION
db1 = Dama((150, 375), blue, 'blue')
db2 = Dama((300, 375), blue, 'blue')
db3 = Dama((450, 375), blue, 'blue')
db4 = Dama((600, 375), blue, 'blue')
db5 = Dama((225, 450), blue, 'blue')
db6 = Dama((375, 450), blue, 'blue')
db7 = Dama((525, 450), blue, 'blue')
db8 = Dama((675, 450), blue, 'blue')
db9 = Dama((150, 525), blue, 'blue')
db10 = Dama((300, 525), blue, 'blue')
db11 = Dama((450, 525), blue, 'blue')
db12 = Dama((600, 525), blue, 'blue')

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
