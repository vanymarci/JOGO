#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from util.Const import WIN_WIDTH, MENU_OPTION, COLOR_ORANGE, COLOR_WHITE

class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(COLOR_ORANGE, text_size=50, text="Mountain", text_center_pos=((WIN_WIDTH / 2),70))
            self.menu_text(COLOR_ORANGE, text_size=50, text="Shooter", text_center_pos=((WIN_WIDTH / 2),120))
            
            for i in range(len(MENU_OPTION)):
                self.menu_text(MENU_OPTION[i], COLOR_WHITE, text_size=20, text_center_pos=((WIN_WIDTH / 2),200 * 25 * i ))
            
            pygame.display.flip()

# Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()  # close window
                   quit()   # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, antialias=True, text_color=tuple).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)