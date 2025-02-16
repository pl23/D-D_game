import pygame as pg
from config import *
import math, random


class player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = Player_layer
        self.groups = self.game.player_layer
        pg.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * tile_res
        self.y = y * tile_res
        self.width = tile_res
        self.height = tile_res

        self.image = pg.Surface([self.width, self.height])
        self.image.fill((255,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
      pass
      