#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.key

from util.Entity import Entity
from util.Const import ENTITY_SPEED
from util.Const import WIN_HEIGHT, WIN_WIDTH

class Player(Entity):
    def __init__(self, name:str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:  #ele para até o topo (subir)
            self.rect.centery -= ENTITY_SPEED[self.name]  
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:  #descer
            self.rect.centery += ENTITY_SPEED[self.name]  
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:  #esquerda
            self.rect.centerx -= ENTITY_SPEED[self.name]  #eixo X
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:  #direita
            self.rect.centerx += ENTITY_SPEED[self.name]  
        pass
