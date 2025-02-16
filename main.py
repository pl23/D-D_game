from config import *
import pygame as pg
from player import *
from background_tile import *
from foreground_tile import *
from entity import *
from hud import *
import sys, random




class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(WIN_size)
        self.clock = pg.time.Clock()
        self.running = True
        
     

    def start(self):
        self.playing = True
        self.background_tiles_layer = pg.sprite.LayeredUpdates()
        self.foreground_tiles_layer = pg.sprite.LayeredUpdates()
        self.entitys_layer = pg.sprite.LayeredUpdates()
        self.player_layer = pg.sprite.LayeredUpdates()
        self.hud_layer = pg.sprite.LayeredUpdates()
        self.player = player(self, 1, 2)
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
        

    def clear_screen(self):
        self.screen.fill((0,0,0))
        
    def update(self):
        self.clear_screen()
        self.background_tiles_layer.update()
        self.foreground_tiles_layer.update()
        self.entitys_layer.update()
        self.player_layer.update()
        self.hud_layer.update()
    
    def draw(self):
        self.screen.fill((0,0,0))
        self.background_tiles_layer.draw(self.screen)
        self.foreground_tiles_layer.draw(self.screen)
        self.entitys_layer.draw(self.screen)
        self.player_layer.draw(self.screen)
        self.hud_layer.draw(self.screen)
        pg.display.flip()
        self.clock.tick(fps)
        pg.display.update()
    
    def game_loop(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
            
        self.running = False
        pg.quit()


if __name__ == '__main__':
    game = Game()
    game.start()
    print("Game Started")
    while game.running:
        game.game_loop()
    sys.exit()
