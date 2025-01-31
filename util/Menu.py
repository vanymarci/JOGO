#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame import font
import util

from util.Const import WIN_WIDTH, MENU_OPTION, COLOR_ORANGE, COLOR_WHITE, COLOR_YELLOW

class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(text_size=50, text="Mountain", text_color=(
            util.COLOR_ORANGE), text_center_pos=(((util.WIN_WIDTH / 2),70)))

            self.menu_text(text_size=50, text="Shooter", text_color=(
            util.COLOR_ORANGE),text_center_pos=(((util.WIN_WIDTH / 2),120)))
            
            for i in range(len(util.MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=20, text=util.MENU_OPTION[i], text_color=(
                    util.COLOR_YELLOW), text_center_pos=(((util.WIN_WIDTH / 2),180 + 30 * i )))

                else:
                    self.menu_text(text_size=20, text=util.MENU_OPTION[i], text_color=(
                    util.COLOR_WHITE), text_center_pos=(((util.WIN_WIDTH / 2),180 + 30 * i )))
            
            pygame.display.flip()

# Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()  # close window
                   quit()   # end pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # tecla para baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: # tecla pra cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) -1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(
            text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)