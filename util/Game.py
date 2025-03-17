#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import util
from util.Const import MENU_OPTION
from util.Level import Level
from util.Menu import Menu
from util.Score import Score

class Game:
    def __init__(self):

        pygame.init()
        self.window = pygame.display.set_mode(
            size=(util.WIN_WIDTH, util.WIN_HEIGHT))

    def run(self):

        while True:
            score = Score(self.window)
            menu = util.Menu(self.window)
            menu_return = menu.run()
            
            if menu_return in [MENU_OPTION[0]]:
                player_score = [0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    score.save(menu_return, player_score)


            elif menu_return == MENU_OPTION[1]:
                score.show()

            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit ()
            else:
                pass

