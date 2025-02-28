#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from util.Background import Background
from util.Const import WIN_WIDTH, WIN_HEIGHT
from util.Player import Player
from util.Enemy import Enemy

class EntityFactory:

    @staticmethod
    def get_entity(entity_name:str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg= []
                for i in range(7):
                    list_bg.append(Background(name=f'Level1Bg{i}',position=(0,0)))
                    list_bg.append(Background(name=f'Level1Bg{i}',position=(WIN_WIDTH,0)))
                return list_bg
            case 'Player1':
                return Player(name='Player1', position=(10, WIN_HEIGHT / 2))  #posição que estará o jogador
            case 'Enemy1':
                return Enemy(name='Enemy1', position=(WIN_WIDTH + 10, random.randint(40,WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy(name='Enemy2', position=(WIN_WIDTH + 10, random.randint(40,WIN_HEIGHT -40)))

