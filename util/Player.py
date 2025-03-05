#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.key
import util.PlayerShot as PlayerShot

from util.PlayerShot import PlayerShot
from util.Entity import Entity
from util.Const import ENTITY_SPEED
from util.Const import WIN_HEIGHT, WIN_WIDTH
from util.Const import PLAYER_KEY_SHOOT
from util.Const import ENTITY_SHOT_DELAY

class Player(Entity):
    def __init__(self, name:str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

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

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
