import pygame
from main import *


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
        for i in checker_list:
            if i.selected is True:
                for b in square_list:
                    if b in i.list:
                        if b is self:
                            if turn == i.turn:
                                if main.Global_has_to_eat:
                                    if i.has_to_eat:
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
                                        for i in checker_list:
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
                                for c in checker_list:
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
                    for b in blue_checker_list:
                        i.rect = pygame.draw.rect(gameDisplay, black, (i.pos[0], i.pos[1], 75, 75))
                        gameDisplay.blit(blue_checker, (b.pos[0], b.pos[1], 10, 10))
                    for b in red_checker_list:
                        i.rect = pygame.draw.rect(gameDisplay, black, (i.pos[0], i.pos[1], 75, 75))
                        gameDisplay.blit(red_checker, (b.pos[0], b.pos[1], 10, 10))
