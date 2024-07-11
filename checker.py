import pygame

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

class Checker:

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
            gameDisplay.blit(red_checker, (self.pos[0], self.pos[1], 10, 10))
        elif self.color is blue:
            gameDisplay.blit(blue_checker, (self.pos[0], self.pos[1], 10, 10))

        pygame.display.update()

    def check_has_to_eat(self):
        self.list = self.get_list()
        for i in checker_list:
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
            if isinstance(i, Checker) is True:
                self.list2 = i.get_list2()
                for b in square_list:
                    aux_pos2 = b.pos
                    if self.list2[0] == aux_pos2:
                        self.list2[0] = b
                    elif self.list2[1] == aux_pos2:
                        self.list2[1] = b

                for b in checker_list:
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
                                        main.Global_has_to_eat = True
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

        for i in checker_list:
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
            if isinstance(i, Checker) is True:
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

                for b in checker_list:
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
                        gameDisplay.blit(red_queen, (self.pos[0], self.pos[1], 10, 10))
                    elif self.color is blue:
                        gameDisplay.blit(blue_queen, (self.pos[0], self.pos[1], 10, 10))

                elif self.is_queen is False:
                    if self.color is red:
                        gameDisplay.blit(red_checker, (self.pos[0], self.pos[1], 10, 10))
                    elif self.color is blue:
                        gameDisplay.blit(blue_checker, (self.pos[0], self.pos[1], 10, 10))

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
        for i in checker_list:
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
            if isinstance(i, Checker) is True:
                if self.color is red:
                    if i.color is blue:
                        self.list2 = i.get_list2()
                        for b in square_list:
                            aux_pos2 = b.pos
                            if self.list2[0] == aux_pos2:
                                self.list2[0] = b
                            elif self.list2[1] == aux_pos2:
                                self.list2[1] = b

                        for b in checker_list:
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

                        for b in checker_list:
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
        for i in checker_list:
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
            if isinstance(i, Checker) is True:
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

                    for b in checker_list:
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

                        for b in checker_list:
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
        for i in checker_list:
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
            if isinstance(i, Checker) is True:
                if self.color is red:
                    if i.color is blue:
                        self.list2 = i.get_list2()
                        for b in square_list:
                            aux_pos2 = b.pos
                            if self.list2[0] == aux_pos2:
                                self.list2[0] = b
                            elif self.list2[1] == aux_pos2:
                                self.list2[1] = b

                        for b in checker_list:
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

                        for b in checker_list:
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
                            for b in blue_checker_list:
                                i.rect = pygame.draw.rect(gameDisplay, black, (i.pos[0], i.pos[1], 75, 75))
                                gameDisplay.blit(blue_checker, (b.pos[0], b.pos[1], 10, 10))
                            for b in red_checker_list:
                                i.rect = pygame.draw.rect(gameDisplay, black, (i.pos[0], i.pos[1], 75, 75))
                                gameDisplay.blit(red_checker, (b.pos[0], b.pos[1], 10, 10))
                    gameDisplay.blit(blue_checker_2, (self.pos[0], self.pos[1], 10, 10))
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
                            for b in blue_checker_list:
                                i.rect = pygame.draw.rect(gameDisplay, black, (i.pos[0], i.pos[1], 75, 75))
                                gameDisplay.blit(blue_checker, (b.pos[0], b.pos[1], 10, 10))
                            for b in red_checker_list:
                                i.rect = pygame.draw.rect(gameDisplay, black, (i.pos[0], i.pos[1], 75, 75))
                                gameDisplay.blit(red_checker, (b.pos[0], b.pos[1], 10, 10))
                    gameDisplay.blit(red_checker_2, (self.pos[0], self.pos[1], 10, 10))

        for i in checker_list:
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

        for i in checker_list:
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
            if isinstance(i, Checker) is True:
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

                for b in checker_list:
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
        for i in checker_list:
            if i.selected is True:
                if i is not self:
                    i.selected = False

        if pygame.mouse.get_pressed()[0] is True:
            if self.is_queen is True:
                if self.color is red:
                    gameDisplay.blit(red_queen_2, (self.pos[0], self.pos[1], 10, 10))
                elif self.color is blue:
                    gameDisplay.blit(blue_queen_2, (self.pos[0], self.pos[1], 10, 10))
            elif self.is_queen is False:
                if self.color is red:
                    gameDisplay.blit(red_checker_2, (self.pos[0], self.pos[1], 10, 10))
                elif self.color is blue:
                    gameDisplay.blit(blue_checker_2, (self.pos[0], self.pos[1], 10, 10))

        pygame.display.update()
