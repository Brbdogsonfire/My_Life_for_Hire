import pygame as pg
import sys
from map import *
from settings import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_objects import *
from object_handler import *
import math

pg.init()

#game loop

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    #begin game
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = Raycasting(self)
        self.object_handler = ObjectHandler(self)
        

        # updates
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler()

        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        

    #drawing self
    def draw(self):
        # self.screen.fill('black')
        self.object_renderer.draw()

        # self.map.draw()
        # self.player.draw()

    #event check, button presses and exitting
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                pg.quit()
                sys.exit
        
        #the power behind the throne
    def run(self):
        while True:
            pg.init()
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()       
    game.run()
   
pg.quit()
sys.exit