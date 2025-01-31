#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from util.Const import WIN_WIDTH, WIN_HEIGHT
from util.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            
