#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import util
from util.Const import MENU_OPTION
from util.Level import Level
from util.Menu import Menu

class Game:
    def __init__(self):

        pygame.init()
        self.window = pygame.display.set_mode(
            size=(util.WIN_WIDTH, util.WIN_HEIGHT))

    def run(self):

        while True:
            menu = util.Menu(self.window)
            menu_return = menu.run()
            
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit ()
            else:
                pass

